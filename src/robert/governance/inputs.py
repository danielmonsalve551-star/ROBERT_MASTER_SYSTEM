"""Internal trusted-adapter inputs, not new inter-component canonical contracts."""

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from robert.contracts.base import Identifier, NonEmptyString, RiskLevel, UtcDateTime


class Operation(StrEnum):
    READ_DOCUMENT = "READ_DOCUMENT"
    PREPARE_DRAFT = "PREPARE_DRAFT"
    UPDATE_DOCUMENT = "UPDATE_DOCUMENT"
    DELETE_RESOURCE = "DELETE_RESOURCE"
    EXTERNAL_ACTION = "EXTERNAL_ACTION"
    CONNECT_TOOL = "CONNECT_TOOL"
    RUN_CODE = "RUN_CODE"
    ACTIVATE_AGENT = "ACTIVATE_AGENT"
    AUTOMATE = "AUTOMATE"
    CHANGE_PHASE = "CHANGE_PHASE"


class RuntimeInput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, str_strip_whitespace=True)

    @field_validator("declared_risk", "max_risk", mode="before", check_fields=False)
    @classmethod
    def reject_coerced_risk(cls, value):
        if isinstance(value, bool) or not isinstance(value, (int, RiskLevel)):
            raise ValueError("risk must be an integer in the official 0–4 scale")
        return value


class OperationScope(RuntimeInput):
    project: NonEmptyString
    sections: tuple[NonEmptyString, ...] = Field(min_length=1)
    phase: int = Field(ge=1, le=17, strict=True)
    mode: Literal["MANUAL", "SUPERVISED", "SANDBOX"]


class GovernanceRequest(RuntimeInput):
    request_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    operation: Operation
    target: NonEmptyString
    scope: OperationScope
    declared_risk: RiskLevel = RiskLevel.INFORMATIONAL


class PermissionGrant(RuntimeInput):
    """A trusted adapter supplies grants; user payloads cannot manufacture them."""

    grant_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    issued_by: Literal["USER"]
    operation: Operation
    target: NonEmptyString
    scope: OperationScope
    max_risk: RiskLevel
    issued_at: UtcDateTime
    expires_at: UtcDateTime
    revoked: bool = Field(default=False, strict=True)
    consumed: bool = Field(default=False, strict=True)

    @model_validator(mode="after")
    def validate_window(self) -> "PermissionGrant":
        if self.expires_at <= self.issued_at:
            raise ValueError("permission expiration must follow issuance")
        return self


class SecurityContext(RuntimeInput):
    """Trusted security observations; unknown state defaults to denial."""

    verified: bool = Field(default=False, strict=True)
    critical_conflict: bool = Field(default=False, strict=True)
    sensitive_data: bool = Field(default=False, strict=True)
    paused: bool = Field(default=False, strict=True)
