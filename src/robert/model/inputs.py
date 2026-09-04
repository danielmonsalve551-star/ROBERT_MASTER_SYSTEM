"""Closed Stage 6 runtime vocabulary; canonical wire contracts remain in contracts/model.py."""

import json
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from robert.contracts.base import Identifier, JsonObject, NonEmptyString


class ModelInput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, allow_inf_nan=False)


class ModelCapability(StrEnum):
    REASONING = "reasoning"
    LONG_CONTEXT = "long_context"
    CODING = "coding"
    DOCUMENT_ANALYSIS = "document_analysis"
    VISION = "vision"
    STRUCTURED_OUTPUT = "structured_output"
    TOOL_CALLING = "tool_calling"
    MULTILINGUAL = "multilingual"
    SUMMARIZATION = "summarization"
    CRITIQUE = "critique"
    PLANNING = "planning"


class ModelAvailability(StrEnum):
    AVAILABLE = "AVAILABLE"
    DEGRADED = "DEGRADED"
    UNAVAILABLE = "UNAVAILABLE"
    DISABLED = "DISABLED"


class ModelProfile(ModelInput):
    model_id: Identifier
    provider: NonEmptyString
    model_family: NonEmptyString
    model_name: NonEmptyString
    model_version: NonEmptyString
    adapter_id: Identifier
    capabilities: tuple[ModelCapability, ...] = Field(min_length=1)
    limitations: tuple[NonEmptyString, ...] = ()
    context_window: int = Field(gt=0, strict=True)
    modalities: tuple[NonEmptyString, ...] = ("text",)
    tool_support: bool = Field(default=False, strict=True)
    structured_output_support: bool = Field(default=False, strict=True)
    allowed_sensitivities: tuple[NonEmptyString, ...] = Field(min_length=1)
    priority: int = Field(default=0, ge=0, le=100, strict=True)

    @model_validator(mode="after")
    def check_profile(self) -> "ModelProfile":
        for values, name in (
            (self.capabilities, "capabilities"),
            (self.modalities, "modalities"),
            (self.allowed_sensitivities, "allowed_sensitivities"),
        ):
            if len(set(values)) != len(values):
                raise ValueError(f"{name} must be unique")
        if self.tool_support != (ModelCapability.TOOL_CALLING in self.capabilities):
            raise ValueError("tool_support must match the tool_calling capability")
        if self.structured_output_support != (
            ModelCapability.STRUCTURED_OUTPUT in self.capabilities
        ):
            raise ValueError("structured_output_support must match its capability")
        return self


class ModelRuntimeState(ModelInput):
    model_id: Identifier
    availability: ModelAvailability
    health: NonEmptyString
    latency_ms: int | None = Field(default=None, ge=0, strict=True)
    rate_limited: bool = Field(default=False, strict=True)


class ModelRequirements(ModelInput):
    required_capabilities: tuple[ModelCapability, ...] = ()
    preferred_capabilities: tuple[ModelCapability, ...] = ()
    context_units: int = Field(default=0, ge=0, strict=True)
    structured_output_required: bool = Field(default=False, strict=True)
    max_attempts: int = Field(default=1, ge=1, le=3, strict=True)

    @model_validator(mode="after")
    def check_requirements(self) -> "ModelRequirements":
        if len(set(self.required_capabilities)) != len(self.required_capabilities):
            raise ValueError("required capabilities must be unique")
        if len(set(self.preferred_capabilities)) != len(self.preferred_capabilities):
            raise ValueError("preferred capabilities must be unique")
        return self


class ModelSelection(ModelInput):
    model_id: Identifier
    provider: NonEmptyString
    adapter_id: Identifier
    selection_reason: NonEmptyString


class ModelToolRequestDraft(ModelInput):
    request_id: Identifier
    tool_capability: NonEmptyString
    operation: NonEmptyString
    target: JsonValue
    inputs: JsonObject
    purpose: NonEmptyString
    expected_result: JsonObject


class ProviderModelOutput(ModelInput):
    status: Literal["COMPLETED", "REFUSED"]
    output: JsonValue
    structured_output: JsonObject | None = None
    reasoning_summary_if_available: NonEmptyString | None = None
    tool_requests: tuple[ModelToolRequestDraft, ...] = ()
    memory_candidates: tuple[Identifier, ...] = ()
    validation_requests: tuple[Identifier, ...] = ()
    confidence_if_applicable: float | None = Field(default=None, ge=0, le=1, strict=True)
    citations_or_evidence: tuple[Identifier, ...] = ()
    warnings: tuple[JsonValue, ...] = ()
    usage_metadata: JsonObject = {}

    @model_validator(mode="after")
    def check_output(self) -> "ProviderModelOutput":
        for values, name in (
            (self.tool_requests, "tool requests"),
            (self.memory_candidates, "memory candidates"),
            (self.validation_requests, "validation requests"),
            (self.citations_or_evidence, "citations or evidence"),
        ):
            identities = [getattr(item, "request_id", item) for item in values]
            if len(set(identities)) != len(identities):
                raise ValueError(f"{name} must have unique identities")
        if self.status == "REFUSED" and self.tool_requests:
            raise ValueError("a refused response cannot request tools")
        return self


def snapshot[Model: BaseModel](model: type[Model], value: Model) -> Model:
    """Detach nested values and reject non-JSON or non-finite provider data."""
    return model.model_validate_json(
        json.dumps(value.model_dump(mode="json"), ensure_ascii=False, allow_nan=False),
        strict=True,
    )
