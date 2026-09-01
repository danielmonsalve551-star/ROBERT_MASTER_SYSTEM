"""Validation request and result contracts, separate from approval."""

from pydantic import Field, JsonValue

from robert.contracts.base import (
    CanonicalContract,
    Identifier,
    JsonObject,
    NonEmptyString,
    ReviewerRole,
    UtcDateTime,
    ValidationStatus,
    ValidationType,
)


class ValidationRequest(CanonicalContract):
    validation_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    target_type: NonEmptyString
    target_ref: Identifier
    validation_types: list[ValidationType]
    reviewer_roles: list[ReviewerRole]
    criteria: list[JsonValue]
    constraints: list[JsonValue]
    evidence_requirements: list[JsonValue]
    source_requirements: list[JsonValue]
    canonical_requirements: list[JsonValue]
    security_requirements: list[JsonValue]
    risk_context: JsonObject
    permission_context: JsonObject
    scope_context: JsonObject
    expected_contract: JsonObject
    severity: NonEmptyString
    blocking_policy: JsonObject


class ValidationResult(CanonicalContract):
    validation_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    target_ref: Identifier
    status: ValidationStatus
    checks: list[JsonValue]
    issues: list[JsonValue]
    severity: NonEmptyString
    evidence: list[JsonValue]
    sources: list[JsonValue]
    confidence: float | None = Field(ge=0.0, le=1.0)
    limitations: list[JsonValue]
    recommendations: list[JsonValue]
    recommended_next_step: NonEmptyString | None
    blocking: bool
    reviewer_refs: list[Identifier]
    timestamp: UtcDateTime
    audit_reference: Identifier | None
