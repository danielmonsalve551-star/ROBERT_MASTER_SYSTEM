"""Reuse Stage 3 checks with current trusted context; validation creates no permissions."""

from datetime import datetime

from robert.audit.redaction import redact_sensitive_values
from robert.contracts.base import PermissionStatus, ScopeStatus, ValidationType
from robert.contracts.validation import ValidationRequest
from robert.governance.checks import assess_risk, check_permission, check_scope, check_security
from robert.governance.inputs import GovernanceRequest, PermissionGrant, SecurityContext
from robert.governance.policy import OPERATION_POLICIES
from robert.validation.findings import CheckFinding
from robert.validation.inputs import ValidationTarget


def validate_context(
    kind: ValidationType,
    request: ValidationRequest,
    target: ValidationTarget,
    *,
    governance: GovernanceRequest | None,
    grant: PermissionGrant | None,
    security: SecurityContext | None,
    now: datetime,
) -> CheckFinding:
    key = f"context:{kind.value.lower()}"
    if governance is not None and (governance.task_id, governance.requester, governance.target) != (
        request.task_id,
        request.requester,
        request.target_ref,
    ):
        return CheckFinding(
            key, kind.value, "FAIL", "Governance context is bound to another request"
        )
    if kind == ValidationType.SECURITY:
        if security is None or not security.verified:
            return CheckFinding(
                key, kind.value, "UNKNOWN", "Trusted security context is unavailable"
            )
        failure = check_security(security)
        if failure:
            return CheckFinding(key, kind.value, "FAIL", failure[1])
        if redact_sensitive_values(target.payload) != target.payload:
            return CheckFinding(
                key, kind.value, "FAIL", "Known sensitive-data patterns require safeguards"
            )
        if (
            "execution_authority" in target.payload
            and target.payload["execution_authority"] != "NONE"
        ):
            return CheckFinding(
                key, kind.value, "FAIL", "Payload attempts to increase execution authority"
            )
        if "autonomy_level" in target.payload and (
            type(target.payload["autonomy_level"]) is not int
            or target.payload["autonomy_level"] != 0
        ):
            return CheckFinding(key, kind.value, "FAIL", "Payload attempts to increase autonomy")
        operation = target.payload.get("operation")
        policy = OPERATION_POLICIES.get(operation) if isinstance(operation, str) else None
        if policy and policy.execution_required:
            return CheckFinding(key, kind.value, "FAIL", "Payload requests a disabled capability")
        if governance and OPERATION_POLICIES[governance.operation].execution_required:
            return CheckFinding(
                key, kind.value, "FAIL", "Governance operation requires disabled execution"
            )
        phase = target.payload.get("phase")
        if "phase" in target.payload and not (
            (type(phase) is int and phase == 10) or (type(phase) is str and phase == "10")
        ):
            return CheckFinding(
                key, kind.value, "FAIL", "Payload phase is outside the current boundary"
            )
        return CheckFinding(
            key, kind.value, "PASS", "Available deterministic security checks passed"
        )
    if governance is None:
        return CheckFinding(
            key, kind.value, "UNKNOWN", "Current trusted governance request is missing"
        )
    permission = check_permission(governance, grant, now)
    if permission.status != PermissionStatus.ALLOWED:
        return CheckFinding(key, kind.value, "FAIL", permission.reason)
    if kind == ValidationType.SCOPE:
        assert grant is not None
        scope = check_scope(governance, grant)
        if scope.status != ScopeStatus.WITHIN_SCOPE:
            return CheckFinding(
                key, kind.value, "FAIL", "Requested operation exceeds authorized scope"
            )
        if assess_risk(governance).risk_level > grant.max_risk:
            return CheckFinding(
                key, kind.value, "FAIL", "Operation risk exceeds the granted ceiling"
            )
    return CheckFinding(
        key, kind.value, "PASS", "Current Stage 3 context check passed; no authority granted"
    )
