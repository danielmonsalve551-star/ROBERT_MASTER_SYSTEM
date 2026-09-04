"""Audited ModelRequest → adapter → validated ModelResponse boundary."""

import json
from collections.abc import Mapping
from typing import Literal

from pydantic import BaseModel, ConfigDict

from robert.audit import AuditEventBuilder, AuditWriter
from robert.audit.redaction import redact_sensitive_values
from robert.contracts.base import JsonObject
from robert.contracts.model import ModelRequest, ModelResponse
from robert.contracts.tool import ToolRequest
from robert.model.adapter import ModelAdapter
from robert.model.errors import (
    ModelErrorType,
    ModelProviderError,
    ModelRoutingError,
    NormalizedModelError,
)
from robert.model.inputs import ModelRequirements, ModelSelection, snapshot
from robert.model.router import ModelRouter


class ModelCallResult(BaseModel):
    """Data-only call result. Tool requests are requests, never executed actions."""

    model_config = ConfigDict(extra="forbid", frozen=True, allow_inf_nan=False)

    response: ModelResponse
    tool_requests: tuple[ToolRequest, ...] = ()
    attempted_models: tuple[str, ...] = ()


class ModelInterface:
    def __init__(
        self,
        router: ModelRouter,
        adapters: tuple[ModelAdapter, ...],
        writer: AuditWriter,
        *,
        authorized_requesters: tuple[str, ...],
    ) -> None:
        if len({item.model_id for item in adapters}) != len(adapters):
            raise ValueError("duplicate model adapter")
        self._router = router
        self._adapters = {item.model_id: item for item in adapters}
        self._writer = writer
        if (
            not authorized_requesters
            or "*" in authorized_requesters
            or len(set(authorized_requesters)) != len(authorized_requesters)
            or any(not item.strip() for item in authorized_requesters)
        ):
            raise ValueError("authorized requesters must be explicit and unique")
        self._authorized_requesters = frozenset(authorized_requesters)

    def send(
        self,
        request: ModelRequest,
        *,
        requester: str,
        requirements: ModelRequirements | None = None,
    ) -> ModelCallResult:
        request = snapshot(ModelRequest, request)
        requirements = snapshot(ModelRequirements, requirements or ModelRequirements())
        rejected = self._request_error(request, requester)
        if rejected is not None:
            return self._error_result(request, requester, rejected, (), None)
        try:
            selections = self._router.rank(request, requirements)
        except ModelRoutingError:
            error = NormalizedModelError(
                error_type=ModelErrorType.NO_ELIGIBLE_MODEL,
                provider_error="no eligible model",
                retryable=False,
                fallback_allowed=False,
                details={},
            )
            return self._error_result(request, requester, error, (), None)
        attempted = []
        last_error = None
        last_selection = None
        for selection in selections[: requirements.max_attempts]:
            last_selection = selection
            attempted.append(selection.model_id)
            adapter = self._adapters.get(selection.model_id)
            if adapter is None or (
                adapter.provider != selection.provider or adapter.adapter_id != selection.adapter_id
            ):
                last_error = NormalizedModelError(
                    error_type=ModelErrorType.SERVICE_UNAVAILABLE,
                    provider_error="selected model adapter is unavailable or mismatched",
                    retryable=False,
                    fallback_allowed=True,
                    details={},
                )
            else:
                try:
                    result = adapter.invoke(request)
                    self._validate_result(request, requirements, selection, result)
                except ModelProviderError as exc:
                    last_error = exc.normalized
                else:
                    event = self._audit(
                        request,
                        requester,
                        selection,
                        status=result.response.status,
                        attempted=tuple(attempted),
                        tool_requests=result.tool_requests,
                        error=None,
                    )
                    response = result.response.model_copy(
                        update={
                            "usage_metadata": {
                                **result.response.usage_metadata,
                                "audit_reference": event.event_id,
                                "model_output_is_authority": False,
                                "tool_requests_executed": False,
                                "memory_written": False,
                            }
                        }
                    )
                    return ModelCallResult(
                        response=response,
                        tool_requests=result.tool_requests,
                        attempted_models=tuple(attempted),
                    )
            if last_error is None or not last_error.fallback_allowed:
                break
        assert last_error is not None
        return self._error_result(request, requester, last_error, tuple(attempted), last_selection)

    def _request_error(self, request: ModelRequest, requester: str) -> NormalizedModelError | None:
        if requester not in self._authorized_requesters:
            return self._rejection("requester is not authorized to use the model interface")
        if request.memory_write_allowed:
            return self._rejection("automatic model-originated memory writes are not authorized")
        if redact_sensitive_values(request.model_dump(mode="json")) != request.model_dump(
            mode="json"
        ):
            return self._rejection("request contains protected sensitive-data patterns")
        serialized = json.dumps(
            [request.instructions, request.constraints], ensure_ascii=False
        ).casefold()
        if "chain of thought" in serialized or "private reasoning" in serialized:
            return self._rejection("private reasoning traces cannot be required")
        try:
            self._validate_output_contract(request.output_contract)
        except ValueError:
            return self._rejection("output contract uses an unsupported schema shape")
        return None

    @staticmethod
    def _rejection(message: str) -> NormalizedModelError:
        return NormalizedModelError(
            error_type=ModelErrorType.REQUEST_REJECTED,
            provider_error=message,
            retryable=False,
            fallback_allowed=False,
            details={},
        )

    def _validate_result(self, request, requirements, selection, result):
        response = snapshot(ModelResponse, result.response)
        tool_requests = tuple(snapshot(ToolRequest, item) for item in result.tool_requests)
        if redact_sensitive_values(response.model_dump(mode="json")) != response.model_dump(
            mode="json"
        ) or any(
            redact_sensitive_values(item.model_dump(mode="json")) != item.model_dump(mode="json")
            for item in tool_requests
        ):
            self._invalid("provider response contains protected sensitive-data patterns")
        if (response.request_id, response.task_id) != (request.request_id, request.task_id):
            self._invalid("response binding mismatch")
        if (response.model_id, response.provider) != (selection.model_id, selection.provider):
            self._invalid("response model identity mismatch")
        if response.tool_requests != [item.request_id for item in tool_requests]:
            self._invalid("tool request references do not match structured requests")
        if any(item.task_id != request.task_id for item in tool_requests):
            self._invalid("tool request task binding mismatch")
        if tool_requests and not request.tool_request_allowed:
            self._invalid("model requested a tool outside the request boundary")
        if response.status == "COMPLETED" and response.errors:
            self._invalid("completed response cannot contain errors")
        if response.status not in ("COMPLETED", "REFUSED"):
            self._invalid("unsupported response status")
        if requirements.structured_output_required and response.structured_output is None:
            self._invalid("required structured output is missing")
        if request.output_contract:
            if response.structured_output is None:
                self._invalid("output contract requires structured output")
            assert response.structured_output is not None
            if not self._matches_output_contract(
                response.structured_output, request.output_contract
            ):
                self._invalid("structured output does not match the output contract")

    @staticmethod
    def _invalid(message):
        raise ModelProviderError(
            ModelErrorType.INVALID_RESPONSE,
            message,
            retryable=False,
            fallback_allowed=True,
        )

    @staticmethod
    def _validate_output_contract(contract: JsonObject) -> None:
        if not contract:
            return
        allowed = {"type", "required", "properties", "additionalProperties"}
        if set(contract) - allowed or contract.get("type") != "object":
            raise ValueError("unsupported output contract")
        required = contract.get("required", [])
        properties = contract.get("properties", {})
        if (
            not isinstance(required, list)
            or any(not isinstance(item, str) or not item for item in required)
            or len(set(required)) != len(required)
            or not isinstance(properties, dict)
            or not set(required).issubset(properties)
            or contract.get("additionalProperties", True) not in (True, False)
        ):
            raise ValueError("invalid output contract")
        supported_types = {"string", "integer", "number", "boolean", "object", "array", "null"}
        for value in properties.values():
            if not isinstance(value, dict) or set(value) != {"type"}:
                raise ValueError("unsupported property contract")
            if value["type"] not in supported_types:
                raise ValueError("unsupported property type")

    @staticmethod
    def _matches_output_contract(output: JsonObject, contract: JsonObject) -> bool:
        required = contract.get("required", [])
        properties = contract.get("properties", {})
        if any(key not in output for key in required):
            return False
        if contract.get("additionalProperties", True) is False and set(output) - set(properties):
            return False
        return all(
            key not in output or _matches_json_type(output[key], rule["type"])
            for key, rule in properties.items()
        )

    def _error_result(self, request, requester, error, attempted, selection):
        event = self._audit(
            request,
            requester,
            selection,
            status="ERROR",
            attempted=attempted,
            tool_requests=(),
            error=error,
        )
        response = ModelResponse(
            contract_version="0.1",
            request_id=request.request_id,
            task_id=request.task_id,
            model_id=selection.model_id if selection else "UNSELECTED",
            provider=selection.provider
            if selection
            else request.provider_requirement or "UNSELECTED",
            status="ERROR",
            output=None,
            structured_output=None,
            reasoning_summary_if_available=None,
            tool_requests=[],
            memory_candidates=[],
            validation_requests=[],
            confidence_if_applicable=None,
            citations_or_evidence=[],
            warnings=["MODEL OUTPUT IS NOT AUTHORITY"],
            errors=[error.model_dump(mode="json")],
            usage_metadata={
                "audit_reference": event.event_id,
                "model_output_is_authority": False,
                "tool_requests_executed": False,
                "memory_written": False,
            },
        )
        return ModelCallResult(response=response, attempted_models=attempted)

    def _audit(
        self,
        request: ModelRequest,
        requester: str,
        selection: ModelSelection | None,
        *,
        status: str,
        attempted: tuple[str, ...],
        tool_requests: tuple[ToolRequest, ...],
        error: NormalizedModelError | None,
    ):
        return self._writer.write(
            AuditEventBuilder().build(
                task_id=request.task_id,
                event_type="MODEL_CALL_COMPLETED" if status != "ERROR" else "MODEL_CALL_FAILED",
                actor=requester,
                component="MODEL_INTERFACE",
                action="PROCESS_MODEL_REQUEST",
                target=selection.model_id if selection else "MODEL_ROUTER",
                input_refs=[request.request_id],
                output_refs=[item.request_id for item in tool_requests],
                validation_state={"status": "PASS" if status != "ERROR" else "FAIL"},
                result={
                    "status": status,
                    "tool_request_count": len(tool_requests),
                    "tool_requests_executed": False,
                    "memory_written": False,
                    "execution_authority": "NONE",
                },
                metadata={
                    "provider": selection.provider if selection else "UNSELECTED",
                    "adapter_id": selection.adapter_id if selection else "UNSELECTED",
                    "selection_reason": selection.selection_reason if selection else "NO_SELECTION",
                    "attempted_models": list(attempted),
                    "error_type": error.error_type.value if error else None,
                },
            )
        )


def _matches_json_type(
    value: object,
    expected: Literal["string", "integer", "number", "boolean", "object", "array", "null"],
) -> bool:
    checks = {
        "string": lambda item: isinstance(item, str),
        "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
        "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
        "boolean": lambda item: isinstance(item, bool),
        "object": lambda item: isinstance(item, Mapping),
        "array": lambda item: isinstance(item, list),
        "null": lambda item: item is None,
    }
    return checks[expected](value)
