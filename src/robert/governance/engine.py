"""Stage 3 fail-closed governance; produces outcomes, never performs actions."""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Literal

from robert.audit.catalog import ErrorAndBlockingEvent as Event
from robert.audit.event_builder import AuditEventBuilder
from robert.audit.outcome_builder import ErrorAndBlockBuilder
from robert.audit.writer import AuditWriter
from robert.contracts.audit import AuditEvent
from robert.contracts.base import PermissionStatus, RiskLevel, ScopeStatus
from robert.contracts.errors import Block
from robert.contracts.governance import ApprovalResult, PermissionCheck, RiskAssessment, ScopeCheck
from robert.governance.checks import (
    assess_risk,
    check_approval,
    check_permission,
    check_scope,
    check_security,
)
from robert.governance.inputs import GovernanceRequest, Operation, PermissionGrant, SecurityContext
from robert.governance.policy import OPERATION_POLICIES


@dataclass(frozen=True)
class GovernanceOutcome:
    """Internal result grouping existing canonical contracts; not an execution permit."""

    status: Literal["ALLOWED", "BLOCKED"]
    checked_gates: tuple[str, ...]
    permission: PermissionCheck
    scope: ScopeCheck | None
    risk: RiskAssessment | None
    block: Block | None
    audit: AuditEvent

    @property
    def execution_authority(self) -> Literal["NONE"]:
        return "NONE"

    @property
    def external_execution_allowed(self) -> Literal[False]:
        return False


class GovernanceEngine:
    def __init__(self, writer: AuditWriter, *, clock: Callable[[], datetime] | None = None) -> None:
        self._writer = writer
        self._clock = clock or (lambda: datetime.now(UTC))

    def evaluate(
        self,
        request: GovernanceRequest,
        *,
        grant: PermissionGrant | None = None,
        approval: ApprovalResult | None = None,
        security: SecurityContext | None = None,
    ) -> GovernanceOutcome:
        # Revalidate and detach inputs: Pydantic frozen models are not deeply immutable.
        request = GovernanceRequest.model_validate_json(request.model_dump_json())
        grant = PermissionGrant.model_validate_json(grant.model_dump_json()) if grant else None
        approval = (
            ApprovalResult.model_validate_json(approval.model_dump_json()) if approval else None
        )
        security = (
            SecurityContext.model_validate_json(security.model_dump_json())
            if security
            else SecurityContext()
        )
        now = self._clock()
        if now.tzinfo is None or now.utcoffset() is None:
            raise ValueError("governance clock must be timezone-aware")
        gates = ["PERMISSION"]
        permission = check_permission(request, grant, now)
        scope = None
        risk = None
        failure = None
        if permission.status != PermissionStatus.ALLOWED:
            failure = (Event.AUTOMATIC_BLOCK, permission.reason)
        else:
            assert grant is not None
            gates.append("SCOPE")
            scope = check_scope(request, grant)
            if scope.status != ScopeStatus.WITHIN_SCOPE:
                event = Event.INCORRECT_PHASE if request.scope.phase != 10 else Event.OUT_OF_SCOPE
                failure = (event, "Requested scope exceeds permission")
        if failure is None:
            assert grant is not None
            gates.append("RISK")
            risk = assess_risk(request)
            if risk.risk_level == RiskLevel.CRITICAL:
                failure = (Event.CRITICAL_RISK, "Critical risk cannot pass Stage 3")
            elif risk.risk_level > grant.max_risk:
                failure = (Event.OUT_OF_SCOPE, "Risk exceeds the granted ceiling")
        if failure is None:
            gates.append("SECURITY")
            failure = check_security(security)
        if failure is None:
            assert risk is not None
            gates.append("APPROVAL")
            reason = check_approval(request, approval, risk, now)
            if reason:
                failure = (Event.FORMAL_APPROVAL_REQUIRED, reason)
        if failure is None:
            gates.append("EXECUTION_AUTHORITY")
            if OPERATION_POLICIES[request.operation].execution_required:
                event = {
                    Operation.CONNECT_TOOL: Event.UNAUTHORIZED_CONNECTION,
                    Operation.ACTIVATE_AGENT: Event.UNAUTHORIZED_AGENT,
                    Operation.AUTOMATE: Event.UNAUTHORIZED_AUTOMATION,
                    Operation.CHANGE_PHASE: Event.INCORRECT_PHASE,
                }.get(request.operation, Event.UNAUTHORIZED_EXECUTION)
                failure = (event, "Execution Authority is NONE; no action will execute")
        block = None
        if failure:
            block = ErrorAndBlockBuilder(clock=lambda: now).build_block(
                task_id=request.task_id,
                event=failure[0],
                source_component="GOVERNANCE_CORE",
                reason=failure[1],
                required_resolution="Resolve the failed gate through human review",
                user_action_required=True,
                approval_required=failure[0] == Event.FORMAL_APPROVAL_REQUIRED,
                related_refs=[request.request_id],
            )
        status = "BLOCKED" if block else "ALLOWED"
        event = AuditEventBuilder(clock=lambda: now).build(
            task_id=request.task_id,
            event_type="GOVERNANCE_EVALUATED",
            actor=request.requester,
            component="GOVERNANCE_CORE",
            action="EVALUATE_GOVERNANCE",
            target=request.target,
            input_refs=[request.request_id] + ([grant.grant_id] if grant else []),
            output_refs=[block.block_id] if block else [],
            permission_state={"status": permission.status.value, "check_id": permission.check_id},
            scope_state={"status": scope.status.value} if scope else {"status": "NOT_CHECKED"},
            risk_state={"level": int(risk.risk_level)} if risk else {"status": "NOT_CHECKED"},
            approval_state={"status": approval.status.value, "approval_id": approval.approval_id}
            if approval
            else {"status": "NOT_SUPPLIED"},
            result={
                "status": status,
                "execution_authority": "NONE",
                "executed": False,
                "block_type": block.block_type if block else None,
            },
            metadata={"checked_gates": gates, "security_verified": security.verified},
        )
        # No ALLOWED result is returned unless durable auditing succeeds.
        persisted = self._writer.write(event)
        return GovernanceOutcome(status, tuple(gates), permission, scope, risk, block, persisted)
