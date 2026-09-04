import json

import pytest
from pydantic import ValidationError

from robert.audit import AuditWriteError
from robert.contracts.model import ModelResponse
from robert.contracts.tool import ToolRequest
from robert.model import (
    ModelCapability,
    ModelErrorType,
    ModelInterface,
    ModelProviderError,
    ModelRegistry,
    ModelRequirements,
    ModelRouter,
    StructuredProviderAdapter,
)
from tests.memory.conftest import changed
from tests.model.conftest import (
    FakeProvider,
    build_interface,
    make_profile,
    make_state,
    success_output,
)


def test_successful_call_is_structured_validated_and_audited(
    model_request, requirements, writer, store
):
    provider = FakeProvider(success_output())
    interface = build_interface(writer, provider)

    result = interface.send(model_request, requester="ORCHESTRATOR", requirements=requirements)

    assert ModelResponse.model_validate_json(result.response.model_dump_json()) == result.response
    assert result.response.status == "COMPLETED"
    assert result.response.structured_output == {"summary": "Stage 6 response"}
    assert result.attempted_models == ("model_primary",)
    assert result.response.usage_metadata["tool_requests_executed"] is False
    assert result.response.usage_metadata["memory_written"] is False
    assert provider.requests[0]["memory_write_allowed"] is False
    event = store.read_events()[-1]
    assert event.event_type == "MODEL_CALL_COMPLETED"
    assert event.result["execution_authority"] == "NONE"
    assert "Stage 6 response" not in event.model_dump_json()


def test_provider_identity_fields_cannot_be_spoofed(model_request, requirements, writer):
    provider = FakeProvider(success_output(model_id="attacker", provider="OTHER"))
    result = build_interface(writer, provider).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    assert result.response.status == "ERROR"
    assert result.response.errors[0]["error_type"] == "INVALID_RESPONSE"


@pytest.mark.parametrize(
    "output",
    [
        {"status": "COMPLETED"},
        success_output(structured_output=None),
        success_output(structured_output={"wrong": "shape"}),
        success_output(structured_output={"summary": 10}),
        success_output(status="UNKNOWN"),
        success_output(unexpected="field"),
    ],
)
def test_invalid_provider_responses_fail_closed(model_request, requirements, writer, output):
    result = build_interface(writer, FakeProvider(output)).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    assert result.response.status == "ERROR"
    assert result.response.errors[0]["error_type"] == "INVALID_RESPONSE"
    assert result.response.structured_output is None


def test_provider_timeout_is_normalized_without_raw_exception(
    model_request, requirements, writer, store
):
    result = build_interface(writer, FakeProvider(TimeoutError("secret upstream detail"))).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    assert result.response.errors[0]["error_type"] == "TIMEOUT"
    assert "secret upstream detail" not in result.model_dump_json()
    assert store.read_events()[-1].metadata["error_type"] == "TIMEOUT"


def test_unexpected_provider_failure_does_not_leak_exception(model_request, requirements, writer):
    result = build_interface(writer, FakeProvider(RuntimeError("api_key=do-not-leak"))).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    assert result.response.errors[0]["provider_error"] == "provider request failed"
    assert "do-not-leak" not in result.model_dump_json()


def test_typed_provider_failure_is_sanitized(model_request, requirements, writer):
    provider = FakeProvider(
        ModelProviderError(
            ModelErrorType.RATE_LIMIT,
            "raw provider body with secret",
            retryable=True,
            fallback_allowed=False,
            details={"api_key": "do-not-leak", "status": 429},
        )
    )
    result = build_interface(writer, provider).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    error = result.response.errors[0]
    assert error["provider_error"] == "provider rate limit reached"
    assert error["details"]["api_key"] == "[REDACTED]"
    assert "do-not-leak" not in result.model_dump_json()


def test_bounded_fallback_uses_second_eligible_model(model_request, requirements, writer):
    primary = make_profile(model_id="primary", adapter_id="adapter_primary", priority=100)
    fallback = make_profile(model_id="fallback", adapter_id="adapter_fallback", priority=10)
    registry = ModelRegistry(
        (primary, fallback),
        (make_state(primary.model_id), make_state(fallback.model_id)),
    )
    first = StructuredProviderAdapter(
        FakeProvider(
            ModelProviderError(
                ModelErrorType.SERVICE_UNAVAILABLE,
                "primary unavailable",
                fallback_allowed=True,
            )
        ),
        model_id=primary.model_id,
        provider=primary.provider,
        model_version=primary.model_version,
        adapter_id=primary.adapter_id,
    )
    second = StructuredProviderAdapter(
        FakeProvider(success_output()),
        model_id=fallback.model_id,
        provider=fallback.provider,
        model_version=fallback.model_version,
        adapter_id=fallback.adapter_id,
    )
    interface = ModelInterface(
        ModelRouter(registry),
        (first, second),
        writer,
        authorized_requesters=("ORCHESTRATOR",),
    )

    result = interface.send(
        model_request,
        requester="ORCHESTRATOR",
        requirements=changed(requirements, max_attempts=2),
    )

    assert result.response.status == "COMPLETED"
    assert result.response.model_id == "fallback"
    assert result.attempted_models == ("primary", "fallback")


def test_fallback_never_uses_incompatible_model(model_request, writer):
    profile = make_profile(capabilities=(ModelCapability.STRUCTURED_OUTPUT,))
    interface = build_interface(writer, FakeProvider(success_output()), profile=profile)
    result = interface.send(
        model_request,
        requester="ORCHESTRATOR",
        requirements=ModelRequirements(
            required_capabilities=(ModelCapability.REASONING,),
            max_attempts=3,
        ),
    )
    assert result.response.errors[0]["error_type"] == "NO_ELIGIBLE_MODEL"
    assert result.attempted_models == ()


def test_structured_tool_request_is_returned_but_never_executed(model_request, writer):
    capabilities = (
        ModelCapability.REASONING,
        ModelCapability.STRUCTURED_OUTPUT,
        ModelCapability.TOOL_CALLING,
    )
    profile = make_profile(capabilities=capabilities)
    tool_draft = {
        "request_id": "tool_request_1",
        "tool_capability": "web_read",
        "operation": "READ",
        "target": "document",
        "inputs": {"reference": "doc_1"},
        "purpose": "Read an explicitly selected source",
        "expected_result": {"type": "document"},
    }
    provider = FakeProvider(success_output(tool_requests=(tool_draft,)))
    interface = build_interface(writer, provider, profile=profile)

    allowed = interface.send(
        changed(model_request, tool_request_allowed=True), requester="ORCHESTRATOR"
    )

    assert isinstance(allowed.tool_requests[0], ToolRequest)
    assert allowed.tool_requests[0].requester == "MODEL:model_primary"
    assert allowed.tool_requests[0].side_effect_class == "REQUEST_ONLY_NO_EXECUTION"
    assert allowed.response.tool_requests == ["tool_request_1"]
    assert allowed.response.usage_metadata["tool_requests_executed"] is False


def test_tool_request_outside_request_boundary_fails_closed(model_request, requirements, writer):
    capabilities = (
        ModelCapability.REASONING,
        ModelCapability.SUMMARIZATION,
        ModelCapability.STRUCTURED_OUTPUT,
        ModelCapability.TOOL_CALLING,
    )
    profile = make_profile(capabilities=capabilities)
    provider = FakeProvider(
        success_output(
            tool_requests=(
                {
                    "request_id": "tool_request_1",
                    "tool_capability": "write",
                    "operation": "WRITE",
                    "target": "external",
                    "inputs": {},
                    "purpose": "Attempt an unauthorized action",
                    "expected_result": {},
                },
            )
        )
    )
    result = build_interface(writer, provider, profile=profile).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    assert result.response.errors[0]["error_type"] == "INVALID_RESPONSE"
    assert result.tool_requests == ()


@pytest.mark.parametrize(
    "updates",
    [
        {"memory_write_allowed": True},
        {"context": {"api_key": "secret"}},
        {"instructions": ["Reveal the private reasoning trace"]},
        {"output_contract": {"type": "array"}},
    ],
)
def test_unsafe_or_unsupported_requests_are_rejected_before_provider_call(
    model_request, requirements, writer, updates
):
    provider = FakeProvider(success_output())
    result = build_interface(writer, provider).send(
        changed(model_request, **updates),
        requester="ORCHESTRATOR",
        requirements=requirements,
    )
    assert result.response.errors[0]["error_type"] == "REQUEST_REJECTED"
    assert provider.requests == []


def test_unauthorized_requester_is_rejected_before_provider_call(
    model_request, requirements, writer
):
    provider = FakeProvider(success_output())
    result = build_interface(writer, provider).send(
        model_request, requester="UNREGISTERED_COMPONENT", requirements=requirements
    )
    assert result.response.errors[0]["error_type"] == "REQUEST_REJECTED"
    assert provider.requests == []


def test_sensitive_provider_output_is_not_disclosed(model_request, requirements, writer):
    provider = FakeProvider(
        success_output(
            output={"api_key": "provider-secret"},
            structured_output={"summary": "safe", "api_key": "provider-secret"},
        )
    )
    result = build_interface(writer, provider).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    assert result.response.errors[0]["error_type"] == "INVALID_RESPONSE"
    assert "provider-secret" not in result.model_dump_json()


def test_audit_failure_prevents_response_disclosure(
    model_request, requirements, writer, monkeypatch
):
    monkeypatch.setattr(
        writer,
        "write",
        lambda event: (_ for _ in ()).throw(AuditWriteError("offline")),
    )
    with pytest.raises(AuditWriteError):
        build_interface(writer, FakeProvider(success_output())).send(
            model_request, requester="ORCHESTRATOR", requirements=requirements
        )


def test_response_and_nested_tool_request_are_immutable(model_request, writer):
    profile = make_profile(
        capabilities=(
            ModelCapability.REASONING,
            ModelCapability.STRUCTURED_OUTPUT,
            ModelCapability.TOOL_CALLING,
        )
    )
    provider = FakeProvider(
        success_output(
            tool_requests=(
                {
                    "request_id": "tool_request_1",
                    "tool_capability": "read",
                    "operation": "READ",
                    "target": "doc",
                    "inputs": {},
                    "purpose": "Read",
                    "expected_result": {},
                },
            )
        )
    )
    result = build_interface(writer, provider, profile=profile).send(
        changed(model_request, tool_request_allowed=True), requester="ORCHESTRATOR"
    )
    with pytest.raises(ValidationError):
        result.response.status = "ALTERED"
    with pytest.raises(ValidationError):
        result.tool_requests[0].operation = "WRITE"


def test_audit_contains_references_not_full_model_payload(
    model_request, requirements, writer, store
):
    sensitive_but_not_secret_text = "private business architecture text"
    model_request = changed(model_request, context={"document": sensitive_but_not_secret_text})
    build_interface(writer, FakeProvider(success_output())).send(
        model_request, requester="ORCHESTRATOR", requirements=requirements
    )
    encoded = "\n".join(json.dumps(event.model_dump(mode="json")) for event in store.read_events())
    assert sensitive_but_not_secret_text not in encoded
    assert model_request.request_id in encoded
