"""Internal validation adapters and declarative criteria; no new wire contracts."""

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from robert.contracts.audit import EvidenceRef
from robert.contracts.base import (
    ContractName,
    Identifier,
    JsonObject,
    NonEmptyString,
    ValidationType,
)


class ValidationInput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, allow_inf_nan=False)


class ValidationTarget(ValidationInput):
    target_ref: Identifier
    task_id: Identifier
    target_type: NonEmptyString
    payload: JsonObject
    evidence: tuple[EvidenceRef, ...] = ()
    sources: tuple[EvidenceRef, ...] = ()


class ContractExpectation(ValidationInput):
    name: ContractName
    version: Literal["0.1"]


class RuleMethod(StrEnum):
    EXISTS = "EXISTS"
    NON_EMPTY = "NON_EMPTY"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    ONE_OF = "ONE_OF"
    TYPE = "TYPE"
    FIELD_EQUALS = "FIELD_EQUALS"


class ValidationCriterion(ValidationInput):
    criterion_id: Identifier
    validation_type: ValidationType
    method: RuleMethod
    path: tuple[NonEmptyString, ...] = Field(min_length=1)
    expected: JsonValue = None
    other_path: tuple[NonEmptyString, ...] | None = None
    required: bool = Field(default=True, strict=True)

    @model_validator(mode="after")
    def check_arguments(self) -> "ValidationCriterion":
        if (
            self.method
            in (
                RuleMethod.EQUALS,
                RuleMethod.NOT_EQUALS,
                RuleMethod.ONE_OF,
                RuleMethod.TYPE,
            )
            and "expected" not in self.model_fields_set
        ):
            raise ValueError("method requires an explicit expected value")
        if self.method == RuleMethod.ONE_OF and not isinstance(self.expected, list):
            raise ValueError("ONE_OF expects a list")
        if self.method == RuleMethod.TYPE and self.expected not in (
            "string",
            "integer",
            "number",
            "boolean",
            "object",
            "array",
            "null",
        ):
            raise ValueError("unsupported type name")
        if self.method == RuleMethod.FIELD_EQUALS and not self.other_path:
            raise ValueError("FIELD_EQUALS requires other_path")
        if self.other_path is not None and self.method != RuleMethod.FIELD_EQUALS:
            raise ValueError("other_path is only valid for FIELD_EQUALS")
        return self
