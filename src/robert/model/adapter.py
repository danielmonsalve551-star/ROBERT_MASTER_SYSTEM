"""Provider translation boundary. Adapters translate; they never govern or execute tools."""

from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from pydantic import ValidationError

from robert.audit.redaction import redact_sensitive_values
from robert.contracts.base import JsonObject
from robert.contracts.model import ModelRequest, ModelResponse
from robert.contracts.tool import ToolRequest
from robert.model.errors import ModelErrorType, ModelProviderError
from robert.model.inputs import ProviderModelOutput, snapshot


@runtime_checkable
class ModelProvider(Protocol):
    """Injected provider port. Stage 6 ships no network client or credentials."""

    def complete(self, payload: JsonObject) -> Mapping[str, object]: ...


class ModelAdapter(Protocol):
    model_id: str
    provider: str
    model_version: str
    adapter_id: str
    adapter_version: str

    def invoke(self, request: ModelRequest) -> "AdaptedModelResult": ...


class AdaptedModelResult:
    """Immutable-by-construction result containing data-only ToolRequest values."""

    __slots__ = ("response", "tool_requests")

    def __init__(self, response: ModelResponse, tool_requests: tuple[ToolRequest, ...]) -> None:
        self.response = snapshot(ModelResponse, response)
        self.tool_requests = tuple(snapshot(ToolRequest, item) for item in tool_requests)


class StructuredProviderAdapter:
    """Provider-neutral structured adapter around one explicitly injected provider port."""

    def __init__(
        self,
        client: ModelProvider,
        *,
        model_id: str,
        provider: str,
        model_version: str,
        adapter_id: str,
        adapter_version: str = "0.1",
    ) -> None:
        self._client = client
        self.model_id = model_id
        self.provider = provider
        self.model_version = model_version
        self.adapter_id = adapter_id
        self.adapter_version = adapter_version

    def invoke(self, request: ModelRequest) -> AdaptedModelResult:
        request = snapshot(ModelRequest, request)
        payload = self._translate_request(request)
        try:
            raw = self._client.complete(payload)
        except ModelProviderError as exc:
            error = exc.normalized
            raise ModelProviderError(
                error.error_type,
                _SAFE_PROVIDER_MESSAGES[error.error_type],
                retryable=error.retryable,
                fallback_allowed=error.fallback_allowed,
                details=redact_sensitive_values(error.details),
            ) from exc
        except TimeoutError as exc:
            raise ModelProviderError(
                ModelErrorType.TIMEOUT,
                "provider request timed out",
                retryable=True,
                fallback_allowed=True,
            ) from exc
        except Exception as exc:
            raise ModelProviderError(
                ModelErrorType.UNKNOWN_PROVIDER_ERROR,
                "provider request failed",
                retryable=False,
                fallback_allowed=True,
            ) from exc
        try:
            normalized = ProviderModelOutput.model_validate(dict(raw), strict=True)
        except (ValidationError, TypeError, ValueError) as exc:
            raise ModelProviderError(
                ModelErrorType.INVALID_RESPONSE,
                "provider returned an invalid structured response",
                retryable=False,
                fallback_allowed=True,
            ) from exc
        tool_requests = tuple(
            self._tool_request(request, item) for item in normalized.tool_requests
        )
        response = ModelResponse(
            contract_version="0.1",
            request_id=request.request_id,
            task_id=request.task_id,
            model_id=self.model_id,
            provider=self.provider,
            status=normalized.status,
            output=normalized.output,
            structured_output=normalized.structured_output,
            reasoning_summary_if_available=normalized.reasoning_summary_if_available,
            tool_requests=[item.request_id for item in tool_requests],
            memory_candidates=list(normalized.memory_candidates),
            validation_requests=list(normalized.validation_requests),
            confidence_if_applicable=normalized.confidence_if_applicable,
            citations_or_evidence=list(normalized.citations_or_evidence),
            warnings=list(normalized.warnings),
            errors=[],
            usage_metadata={
                **normalized.usage_metadata,
                "model_version": self.model_version,
                "adapter_id": self.adapter_id,
                "adapter_version": self.adapter_version,
            },
        )
        return AdaptedModelResult(response, tool_requests)

    def _translate_request(self, request: ModelRequest) -> JsonObject:
        return {
            "request_id": request.request_id,
            "task_id": request.task_id,
            "model_role": request.model_role,
            "objective": request.objective,
            "instructions": list(request.instructions),
            "context": request.context,
            "inputs": request.inputs,
            "constraints": list(request.constraints),
            "output_contract": request.output_contract,
            "tool_request_allowed": request.tool_request_allowed,
            "memory_write_allowed": False,
            "validation_requirements": list(request.validation_requirements),
            "sensitivity": request.sensitivity,
        }

    def _tool_request(self, request, draft):
        return ToolRequest(
            contract_version="0.1",
            request_id=draft.request_id,
            task_id=request.task_id,
            requester=f"MODEL:{self.model_id}",
            tool_capability=draft.tool_capability,
            operation=draft.operation,
            target=draft.target,
            inputs=draft.inputs,
            purpose=draft.purpose,
            expected_result=draft.expected_result,
            permission_requirements=["ORCHESTRATOR_PERMISSION_CHECK_REQUIRED"],
            scope_requirements=["ORCHESTRATOR_SCOPE_CHECK_REQUIRED"],
            risk_context={"authority": "NONE", "source": "UNTRUSTED_MODEL_OUTPUT"},
            approval_requirements=["SEPARATE_AUTHORIZATION_IF_REQUIRED"],
            side_effect_class="REQUEST_ONLY_NO_EXECUTION",
            data_sensitivity=request.sensitivity,
            timeout_policy={},
            retry_policy={},
            validation_requirements=list(request.validation_requirements),
        )


_SAFE_PROVIDER_MESSAGES = {
    ModelErrorType.TIMEOUT: "provider request timed out",
    ModelErrorType.RATE_LIMIT: "provider rate limit reached",
    ModelErrorType.AUTH_FAILURE: "provider authentication failed",
    ModelErrorType.SERVICE_UNAVAILABLE: "provider service unavailable",
    ModelErrorType.INVALID_RESPONSE: "provider returned an invalid response",
    ModelErrorType.CONTEXT_LIMIT: "provider context limit exceeded",
    ModelErrorType.CONTENT_REJECTION: "provider rejected the content",
    ModelErrorType.TOOL_FAILURE: "provider tool translation failed",
    ModelErrorType.UNKNOWN_PROVIDER_ERROR: "provider request failed",
    ModelErrorType.NO_ELIGIBLE_MODEL: "no eligible model",
    ModelErrorType.REQUEST_REJECTED: "model request rejected",
}
