"""Closed Stage 7 runtime vocabulary; canonical wire contracts remain in contracts/skill.py."""

import json
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from robert.contracts.base import Identifier, JsonObject, NonEmptyString


class SkillInput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, allow_inf_nan=False)


class SkillStatus(StrEnum):
    IMPLEMENTED = "IMPLEMENTED"
    AVAILABLE = "AVAILABLE"
    DISABLED = "DISABLED"


class SkillCategory(StrEnum):
    ANALYSIS = "ANALYSIS"
    RESEARCH = "RESEARCH"
    ARCHITECTURE = "ARCHITECTURE"
    SECURITY = "SECURITY"
    MEMORY = "MEMORY"
    CODE = "CODE"
    TESTING = "TESTING"
    STRATEGY = "STRATEGY"
    VALIDATION = "VALIDATION"
    DOCUMENTATION = "DOCUMENTATION"


class SkillOutputContract(SkillInput):
    required: tuple[NonEmptyString, ...] = Field(min_length=1)
    allow_additional: bool = Field(default=False, strict=True)

    @model_validator(mode="after")
    def check_unique(self) -> "SkillOutputContract":
        if len(set(self.required)) != len(self.required):
            raise ValueError("required output fields must be unique")
        return self


class SkillManifest(SkillInput):
    skill_id: Identifier
    name: NonEmptyString
    version: NonEmptyString
    purpose: NonEmptyString
    category: SkillCategory
    capabilities: tuple[NonEmptyString, ...] = Field(min_length=1)
    required_inputs: tuple[NonEmptyString, ...] = ()
    required_context: tuple[NonEmptyString, ...] = ()
    constraints: tuple[JsonValue, ...] = ()
    tool_requirements: tuple[NonEmptyString, ...] = ()
    model_requirements: tuple[NonEmptyString, ...] = ()
    memory_requirements: tuple[JsonValue, ...] = ()
    output_contract: SkillOutputContract
    validation_requirements: tuple[JsonValue, ...] = ()
    failure_modes: tuple[NonEmptyString, ...] = Field(min_length=1)
    compatible_requesters: tuple[NonEmptyString, ...] = Field(min_length=1)
    dependencies: tuple[Identifier, ...] = ()
    overlap_notes: NonEmptyString
    status: SkillStatus
    external_effects_allowed: bool = Field(default=False, strict=True)

    @model_validator(mode="after")
    def check_manifest(self) -> "SkillManifest":
        for values, name in (
            (self.capabilities, "capabilities"),
            (self.required_inputs, "required inputs"),
            (self.required_context, "required context"),
            (self.tool_requirements, "tool requirements"),
            (self.model_requirements, "model requirements"),
            (self.compatible_requesters, "compatible requesters"),
            (self.dependencies, "dependencies"),
        ):
            if len(set(values)) != len(values):
                raise ValueError(f"{name} must be unique")
        if "*" in self.compatible_requesters:
            raise ValueError("compatible requesters must be explicit")
        if self.external_effects_allowed:
            raise ValueError("external effects are not supported in Stage 7")
        return self


class SkillProcedureOutput(SkillInput):
    output: JsonValue
    derived_data: JsonObject = {}
    tool_requests: tuple[Identifier, ...] = ()
    model_requests: tuple[Identifier, ...] = ()
    memory_candidates: tuple[Identifier, ...] = ()
    validation_requests: tuple[Identifier, ...] = ()
    warnings: tuple[JsonValue, ...] = ()


def snapshot[Model: BaseModel](model: type[Model], value: Model) -> Model:
    return model.model_validate_json(
        json.dumps(value.model_dump(mode="json"), ensure_ascii=False, allow_nan=False),
        strict=True,
    )
