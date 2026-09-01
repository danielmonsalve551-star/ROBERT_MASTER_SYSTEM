"""Permission, scope, risk, and approval governance contracts."""

from pydantic import JsonValue

from robert.contracts.base import (
    ApprovalStatus,
    CanonicalContract,
    Identifier,
    JsonObject,
    NonEmptyString,
    PermissionStatus,
    RiskLevel,
    ScopeStatus,
    UtcDateTime,
)


class PermissionCheck(CanonicalContract):
    check_id: Identifier
    task_id: Identifier
    requester: NonEmptyString
    operation: NonEmptyString
    resource: JsonValue
    required_permission: NonEmptyString
    existing_permissions: list[NonEmptyString]
    status: PermissionStatus
    reason: NonEmptyString
    expires_at: UtcDateTime | None


class ScopeCheck(CanonicalContract):
    check_id: Identifier
    task_id: Identifier
    requested_scope: JsonObject
    authorized_scope: JsonObject
    status: ScopeStatus
    violations: list[JsonValue]
    constraints: list[JsonValue]


class RiskAssessment(CanonicalContract):
    assessment_id: Identifier
    task_id: Identifier
    operation: NonEmptyString
    target: JsonValue
    risk_level: RiskLevel
    risk_factors: list[JsonValue]
    side_effect_class: NonEmptyString
    reversibility: NonEmptyString
    sensitivity: NonEmptyString
    external_impact: JsonObject
    mitigations: list[JsonValue]
    status: NonEmptyString


class ApprovalRequest(CanonicalContract):
    approval_id: Identifier
    task_id: Identifier
    operation: NonEmptyString
    target: JsonValue
    purpose: NonEmptyString
    scope: JsonObject
    risk: JsonObject
    side_effects: list[JsonValue]
    requested_by: NonEmptyString
    required_approver: NonEmptyString
    expires_at: UtcDateTime | None
    context_summary: NonEmptyString


class ApprovalResult(CanonicalContract):
    approval_id: Identifier
    task_id: Identifier
    status: ApprovalStatus
    approved_by: NonEmptyString | None
    approved_at: UtcDateTime | None
    authorized_operation: NonEmptyString | None
    authorized_target: JsonValue | None
    authorized_scope: JsonObject | None
    conditions: list[JsonValue]
    expires_at: UtcDateTime | None
    reason: NonEmptyString
