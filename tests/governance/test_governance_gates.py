from datetime import timedelta

import pytest
from pydantic import ValidationError

from robert.audit import AuditWriter
from robert.contracts.base import ApprovalStatus, RiskLevel
from robert.contracts.governance import ApprovalResult
from robert.governance import GovernanceEngine, GovernanceRequest, Operation, SecurityContext

VERIFIED = SecurityContext(verified=True)
GATE_ORDER = ("PERMISSION", "SCOPE", "RISK", "SECURITY", "APPROVAL", "EXECUTION_AUTHORITY")


def approval_for(request, now, **overrides):
    values = dict(
        contract_version="0.1",
        approval_id="approval_test",
        task_id=request.task_id,
        status="APPROVED",
        approved_by="USER",
        approved_at=now - timedelta(minutes=5),
        authorized_operation=request.operation.value,
        authorized_target=request.target,
        authorized_scope=request.scope.model_dump(mode="json"),
        conditions=[],
        expires_at=now + timedelta(minutes=5),
        reason="Explicit test approval",
    )
    values.update(overrides)
    return ApprovalResult(**values)


def test_valid_documental_request_passes_all_gates_without_execution(
    engine, request_data, grant, audit_store
):
    outcome = engine.evaluate(request_data, grant=grant, security=VERIFIED)
    assert outcome.status == "ALLOWED"
    assert outcome.checked_gates == GATE_ORDER
    assert outcome.block is None
    assert outcome.execution_authority == "NONE"
    assert outcome.external_execution_allowed is False
    assert audit_store.read_events()[0].result["executed"] is False


def test_missing_permission_blocks_and_records_audit(engine, request_data, audit_store):
    outcome = engine.evaluate(request_data, security=VERIFIED)
    assert outcome.status == "BLOCKED"
    assert outcome.checked_gates == ("PERMISSION",)
    assert outcome.permission.status == "NOT_FOUND"
    assert audit_store.read_events()[0].output_refs == [outcome.block.block_id]


@pytest.mark.parametrize(
    "changes",
    [
        {"revoked": True},
        {"consumed": True},
        {"requester": "OTHER"},
        {"task_id": "other_task"},
        {"target": "OTHER.md"},
        {"operation": Operation.READ_DOCUMENT},
    ],
)
def test_invalid_permission_cannot_continue(engine, request_data, grant, changes):
    outcome = engine.evaluate(
        request_data, grant=grant.model_copy(update=changes), security=VERIFIED
    )
    assert outcome.status == "BLOCKED"
    assert outcome.checked_gates == ("PERMISSION",)


@pytest.mark.parametrize(
    "changes",
    [
        {"sections": ("unauthorized",)},
        {"project": "OTHER"},
        {"phase": 11},
        {"mode": "SANDBOX"},
        {"sections": ("*",)},
    ],
)
def test_changed_scope_blocks(engine, request_data, grant, changes):
    request = request_data.model_copy(
        update={"scope": request_data.scope.model_copy(update=changes)}
    )
    outcome = engine.evaluate(request, grant=grant, security=VERIFIED)
    assert outcome.status == "BLOCKED"
    assert outcome.checked_gates[-1] == "SCOPE"


def test_permission_expiration_boundary_is_exclusive(engine, request_data, grant, now):
    outcome = engine.evaluate(
        request_data, grant=grant.model_copy(update={"expires_at": now}), security=VERIFIED
    )
    assert outcome.permission.status == "EXPIRED"


def test_future_permission_is_not_active(engine, request_data, grant, now):
    future = grant.model_copy(update={"issued_at": now + timedelta(minutes=5)})
    assert (
        engine.evaluate(request_data, grant=future, security=VERIFIED).permission.status
        == "EXPIRED"
    )


def test_policy_floor_prevents_risk_downgrade(engine, request_data, grant):
    outcome = engine.evaluate(
        request_data,
        grant=grant.model_copy(update={"max_risk": RiskLevel.INFORMATIONAL}),
        security=VERIFIED,
    )
    assert outcome.status == "BLOCKED"
    assert outcome.risk.risk_level == 2
    assert outcome.checked_gates[-1] == "RISK"


def test_critical_risk_cannot_be_approved_away(engine, request_data, grant):
    outcome = engine.evaluate(
        request_data.model_copy(update={"declared_risk": RiskLevel.CRITICAL}),
        grant=grant,
        security=VERIFIED,
    )
    assert outcome.block.block_type == "CRITICAL_RISK"


@pytest.mark.parametrize(
    "security,block_type",
    [
        (None, "AUTOMATIC_BLOCK"),
        (SecurityContext(verified=True, paused=True), "MANDATORY_PAUSE"),
        (SecurityContext(verified=True, critical_conflict=True), "CRITICAL_RISK"),
        (SecurityContext(verified=True, sensitive_data=True), "SENSITIVE_DATA_DETECTED"),
    ],
)
def test_unsafe_or_unknown_security_blocks(engine, request_data, grant, security, block_type):
    outcome = engine.evaluate(request_data, grant=grant, security=security)
    assert outcome.block.block_type == block_type
    assert outcome.checked_gates[-1] == "SECURITY"


def test_high_risk_requires_matching_human_approval(engine, request_data, grant, now):
    request = request_data.model_copy(update={"operation": Operation.UPDATE_DOCUMENT})
    permission = grant.model_copy(update={"operation": request.operation})
    denied = engine.evaluate(request, grant=permission, security=VERIFIED)
    assert denied.block.block_type == "FORMAL_APPROVAL_REQUIRED"
    allowed = engine.evaluate(
        request, grant=permission, approval=approval_for(request, now), security=VERIFIED
    )
    assert allowed.status == "ALLOWED"
    assert allowed.audit.result["executed"] is False


@pytest.mark.parametrize(
    "status", [status for status in ApprovalStatus if status != ApprovalStatus.APPROVED]
)
def test_inactive_approval_never_passes(engine, request_data, grant, now, status):
    outcome = engine.evaluate(
        request_data,
        grant=grant,
        security=VERIFIED,
        approval=approval_for(request_data, now, status=status),
    )
    assert outcome.status == "BLOCKED"
    assert outcome.checked_gates[-1] == "APPROVAL"


@pytest.mark.parametrize(
    "overrides",
    [
        {"approved_by": "MODEL"},
        {"approved_at": None},
        {"expires_at": None},
        {"task_id": "other_task"},
        {"authorized_operation": "EXTERNAL_ACTION"},
        {"authorized_target": "OTHER.md"},
        {"authorized_scope": {}},
        {"conditions": ["unknown condition"]},
    ],
)
def test_approval_binding_and_conditions_fail_closed(engine, request_data, grant, now, overrides):
    outcome = engine.evaluate(
        request_data,
        grant=grant,
        security=VERIFIED,
        approval=approval_for(request_data, now, **overrides),
    )
    assert outcome.status == "BLOCKED"


@pytest.mark.parametrize("which", ["expires_at", "approved_at"])
def test_expired_and_future_approvals_block(engine, request_data, grant, now, which):
    value = now if which == "expires_at" else now + timedelta(minutes=1)
    outcome = engine.evaluate(
        request_data,
        grant=grant,
        security=VERIFIED,
        approval=approval_for(request_data, now, **{which: value}),
    )
    assert outcome.status == "BLOCKED"


@pytest.mark.parametrize(
    "operation",
    [
        Operation.EXTERNAL_ACTION,
        Operation.CONNECT_TOOL,
        Operation.RUN_CODE,
        Operation.ACTIVATE_AGENT,
        Operation.AUTOMATE,
        Operation.CHANGE_PHASE,
    ],
)
def test_none_authority_blocks_execution_even_with_approval(
    engine, request_data, grant, now, operation, monkeypatch
):
    monkeypatch.setenv("ROBERT_EXECUTION_AUTHORITY", "FULL")
    request = request_data.model_copy(update={"operation": operation})
    permission = grant.model_copy(update={"operation": operation})
    outcome = engine.evaluate(
        request, grant=permission, security=VERIFIED, approval=approval_for(request, now)
    )
    assert outcome.status == "BLOCKED"
    assert outcome.checked_gates == GATE_ORDER
    assert outcome.external_execution_allowed is False


@pytest.mark.parametrize(
    "field,value", [("operation", "UNKNOWN"), ("execution_authority", "FULL"), ("declared_risk", 5)]
)
def test_invalid_runtime_inputs_rejected(request_data, field, value):
    payload = request_data.model_dump(mode="json")
    payload[field] = value
    with pytest.raises(ValidationError):
        GovernanceRequest.model_validate(payload)


def test_model_copy_cannot_bypass_runtime_validation(engine, request_data, grant):
    with pytest.raises(ValidationError):
        engine.evaluate(
            request_data, grant=grant.model_copy(update={"issued_by": "MODEL"}), security=VERIFIED
        )


@pytest.mark.parametrize("value", [True, "2", 2.0])
def test_risk_input_does_not_coerce_booleans_or_strings(request_data, value):
    payload = request_data.model_dump(mode="json")
    payload["declared_risk"] = value
    with pytest.raises(ValidationError):
        GovernanceRequest.model_validate(payload)


def test_approval_is_detached_before_caller_can_mutate_it(audit_store, request_data, grant, now):
    approval = approval_for(request_data, now)

    def clock():
        approval.authorized_scope.clear()
        return now

    engine = GovernanceEngine(AuditWriter(audit_store), clock=clock)
    outcome = engine.evaluate(request_data, grant=grant, approval=approval, security=VERIFIED)
    assert outcome.status == "ALLOWED"
    assert approval.authorized_scope == {}


def test_mutating_returned_audit_data_cannot_rewrite_history(
    engine, request_data, grant, audit_store
):
    outcome = engine.evaluate(request_data, grant=grant, security=VERIFIED)
    outcome.audit.result["executed"] = True
    assert audit_store.read_events()[0].result["executed"] is False


def test_read_document_passes_with_matching_permission(engine, request_data, grant):
    request = request_data.model_copy(update={"operation": Operation.READ_DOCUMENT})
    permission = grant.model_copy(update={"operation": Operation.READ_DOCUMENT})
    assert engine.evaluate(request, grant=permission, security=VERIFIED).status == "ALLOWED"


def test_delete_request_is_critical_and_blocked(engine, request_data, grant):
    request = request_data.model_copy(update={"operation": Operation.DELETE_RESOURCE})
    permission = grant.model_copy(update={"operation": Operation.DELETE_RESOURCE})
    assert (
        engine.evaluate(request, grant=permission, security=VERIFIED).block.block_type
        == "CRITICAL_RISK"
    )


def test_security_flags_reject_string_coercion():
    with pytest.raises(ValidationError):
        SecurityContext(verified="true")
