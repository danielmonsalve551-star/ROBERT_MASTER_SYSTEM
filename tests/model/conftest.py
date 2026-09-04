from collections.abc import Mapping
from datetime import UTC, datetime

import pytest

from robert.audit import AuditWriter, JsonLinesAuditStore
from robert.contracts.base import JsonObject
from robert.contracts.model import ModelRequest
from robert.model import (
    ModelAvailability,
    ModelCapability,
    ModelInterface,
    ModelProfile,
    ModelRegistry,
    ModelRequirements,
    ModelRouter,
    ModelRuntimeState,
    StructuredProviderAdapter,
)


class FakeProvider:
    def __init__(self, result: Mapping[str, object] | Exception):
        self.result = result
        self.requests: list[JsonObject] = []

    def complete(self, payload: JsonObject) -> Mapping[str, object]:
        self.requests.append(payload)
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


@pytest.fixture
def now():
    return datetime(2026, 9, 4, 12, tzinfo=UTC)


@pytest.fixture
def store(tmp_path):
    return JsonLinesAuditStore(tmp_path / "model_audit.jsonl")


@pytest.fixture
def writer(store):
    return AuditWriter(store)


@pytest.fixture
def model_request():
    return ModelRequest(
        contract_version="0.1",
        request_id="model_request_1",
        task_id="task_model_1",
        model_role="AUTHORIZED_ROBERT_COMPONENT",
        provider_requirement=None,
        objective="Return a structured summary",
        instructions=["Use only supplied context"],
        context={"document_ref": "document_1"},
        inputs={"topic": "architecture"},
        constraints=["MODEL_OUTPUT_IS_NOT_TRUTH"],
        output_contract={
            "type": "object",
            "required": ["summary"],
            "properties": {"summary": {"type": "string"}},
            "additionalProperties": False,
        },
        tool_request_allowed=False,
        memory_write_allowed=False,
        validation_requirements=["CANONICAL"],
        sensitivity="INTERNAL",
    )


@pytest.fixture
def requirements():
    return ModelRequirements(
        required_capabilities=(ModelCapability.REASONING,),
        preferred_capabilities=(ModelCapability.SUMMARIZATION,),
        context_units=100,
        structured_output_required=True,
    )


def make_profile(
    model_id="model_primary",
    provider="SANDBOX_PROVIDER",
    adapter_id="adapter_primary",
    priority=10,
    capabilities=None,
    allowed_sensitivities=("PUBLIC", "INTERNAL"),
):
    capabilities = capabilities or (
        ModelCapability.REASONING,
        ModelCapability.SUMMARIZATION,
        ModelCapability.STRUCTURED_OUTPUT,
    )
    return ModelProfile(
        model_id=model_id,
        provider=provider,
        model_family="STRUCTURED_TEST",
        model_name=model_id,
        model_version="2026-09-04",
        adapter_id=adapter_id,
        capabilities=capabilities,
        context_window=1000,
        tool_support=ModelCapability.TOOL_CALLING in capabilities,
        structured_output_support=ModelCapability.STRUCTURED_OUTPUT in capabilities,
        allowed_sensitivities=allowed_sensitivities,
        priority=priority,
    )


def make_state(model_id="model_primary", availability=ModelAvailability.AVAILABLE, **updates):
    return ModelRuntimeState(
        model_id=model_id,
        availability=availability,
        health="HEALTHY",
        **updates,
    )


def success_output(**updates):
    output = {
        "status": "COMPLETED",
        "output": {"summary": "Stage 6 response"},
        "structured_output": {"summary": "Stage 6 response"},
        "reasoning_summary_if_available": "Based on supplied architecture context",
        "tool_requests": (),
        "memory_candidates": (),
        "validation_requests": ("validation_1",),
        "confidence_if_applicable": 0.9,
        "citations_or_evidence": ("document_1",),
        "warnings": (),
        "usage_metadata": {"input_units": 100, "output_units": 20},
    }
    output.update(updates)
    return output


def build_interface(writer, provider, *, profile=None, state=None):
    profile = profile or make_profile()
    state = state or make_state(profile.model_id)
    registry = ModelRegistry((profile,), (state,))
    adapter = StructuredProviderAdapter(
        provider,
        model_id=profile.model_id,
        provider=profile.provider,
        model_version=profile.model_version,
        adapter_id=profile.adapter_id,
    )
    return ModelInterface(
        ModelRouter(registry),
        (adapter,),
        writer,
        authorized_requesters=("ORCHESTRATOR", "VALIDATOR"),
    )
