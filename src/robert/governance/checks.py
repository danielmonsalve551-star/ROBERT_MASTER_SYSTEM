"""Deterministic Permission → Scope → Risk → Security → Approval checks."""

from datetime import datetime
from uuid import uuid4

from robert.audit.catalog import ErrorAndBlockingEvent as Event
from robert.contracts.base import ApprovalStatus, PermissionStatus, RiskLevel, ScopeStatus
from robert.contracts.governance import ApprovalResult, PermissionCheck, RiskAssessment, ScopeCheck
from robert.governance.inputs import GovernanceRequest, PermissionGrant, SecurityContext
from robert.governance.policy import OPERATION_POLICIES


def check_permission(
    request: GovernanceRequest, grant: PermissionGrant | None, now: datetime
) -> PermissionCheck:
    status = PermissionStatus.NOT_FOUND
    reason = "No explicit permission grant"
    if grant is not None:
        status, reason = PermissionStatus.ALLOWED, "Explicit permission matches request"
        if grant.revoked or grant.consumed:
            status, reason = PermissionStatus.DENIED, "Permission revoked or consumed"
        elif now < grant.issued_at or now >= grant.expires_at:
            status, reason = PermissionStatus.EXPIRED, "Permission outside its validity window"
        elif (grant.task_id, grant.requester, grant.operation, grant.target) != (
            request.task_id,
            request.requester,
            request.operation,
            request.target,
        ):
            status, reason = (
                PermissionStatus.DENIED,
                "Permission does not bind this task/action/target",
            )
    return PermissionCheck(
        contract_version="0.1",
        check_id=f"permission_{uuid4().hex}",
        task_id=request.task_id,
        requester=request.requester,
        operation=request.operation.value,
        resource=request.target,
        required_permission=request.operation.value,
        existing_permissions=[grant.grant_id] if grant else [],
        status=status,
        reason=reason,
        expires_at=grant.expires_at if grant else None,
    )


def check_scope(request: GovernanceRequest, grant: PermissionGrant) -> ScopeCheck:
    requested, authorized = request.scope, grant.scope
    violations = []
    if requested.project != authorized.project:
        violations.append("project mismatch")
    if requested.phase != 10 or requested.phase != authorized.phase:
        violations.append("phase mismatch")
    if requested.mode != authorized.mode:
        violations.append("mode mismatch")
    if not set(requested.sections).issubset(authorized.sections):
        violations.append("section outside explicit scope")
    if "*" in authorized.sections or "*" in requested.sections:
        violations.append("wildcard scope is unsupported")
    return ScopeCheck(
        contract_version="0.1",
        check_id=f"scope_{uuid4().hex}",
        task_id=request.task_id,
        requested_scope=requested.model_dump(mode="json"),
        authorized_scope=authorized.model_dump(mode="json"),
        status=ScopeStatus.OUT_OF_SCOPE if violations else ScopeStatus.WITHIN_SCOPE,
        violations=violations,
        constraints=["EXACT_RESOURCE", "PHASE_10", "STAGE_3_ONLY"],
    )


def assess_risk(request: GovernanceRequest) -> RiskAssessment:
    policy = OPERATION_POLICIES[request.operation]
    level = max(policy.risk_floor, request.declared_risk)
    return RiskAssessment(
        contract_version="0.1",
        assessment_id=f"risk_{uuid4().hex}",
        task_id=request.task_id,
        operation=request.operation.value,
        target=request.target,
        risk_level=level,
        risk_factors=["POLICY_FLOOR", "CALLER_RISK_CAN_ONLY_INCREASE"],
        side_effect_class="EXECUTION_REQUESTED" if policy.execution_required else "DOCUMENTAL",
        reversibility="UNKNOWN" if policy.execution_required else "REVIEWABLE",
        sensitivity="REQUIRES_SECURITY_CHECK",
        external_impact={"execution_required": policy.execution_required},
        mitigations=["MANDATORY_AUDIT", "EXECUTION_AUTHORITY_NONE"],
        status="ASSESSED",
    )


def check_security(context: SecurityContext) -> tuple[Event, str] | None:
    if context.paused:
        return Event.MANDATORY_PAUSE, "User control pause is active"
    if not context.verified:
        return Event.AUTOMATIC_BLOCK, "Security state has not been verified"
    if context.critical_conflict:
        return Event.CRITICAL_RISK, "Critical security conflict"
    if context.sensitive_data:
        return Event.SENSITIVE_DATA_DETECTED, "Sensitive data requires separate safeguards"
    return None


def check_approval(
    request: GovernanceRequest,
    approval: ApprovalResult | None,
    risk: RiskAssessment,
    now: datetime,
) -> str | None:
    required = (
        OPERATION_POLICIES[request.operation].approval_required or risk.risk_level >= RiskLevel.HIGH
    )
    if not required:
        # Explicit rejection/revocation must never be treated as absence of approval.
        if approval is not None and approval.status != ApprovalStatus.APPROVED:
            return "Supplied approval is not active"
        if approval is None:
            return None
    if approval is None or approval.status != ApprovalStatus.APPROVED:
        return "Explicit approval is required"
    if approval.approved_by != "USER":
        return "Approval must come from the verified human authority"
    if approval.approved_at is None or approval.expires_at is None:
        return "Approval requires a bounded validity window"
    if not approval.approved_at <= now < approval.expires_at:
        return "Approval expired or not yet valid"
    if (approval.task_id, approval.authorized_operation, approval.authorized_target) != (
        request.task_id,
        request.operation.value,
        request.target,
    ):
        return "Approval is not bound to this task/action/target"
    if approval.authorized_scope != request.scope.model_dump(mode="json"):
        return "Approval scope does not match request"
    if approval.conditions:
        return "Conditional approval requires an unimplemented condition evaluator"
    return None
