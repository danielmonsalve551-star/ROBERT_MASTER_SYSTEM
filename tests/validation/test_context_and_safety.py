from datetime import datetime

import pytest
from pydantic import ValidationError

from robert.audit import AuditWriter
from robert.governance import Operation, SecurityContext
from robert.validation import ValidationHandler, ValidationTarget
from tests.validation.conftest import rule, with_request

VERIFIED = SecurityContext(verified=True)


@pytest.mark.parametrize("kind", ["PERMISSION", "SCOPE"])
def test_current_governance_context_is_reused(
    handler, validation_request, target, governance, grant, kind
):
    request = with_request(validation_request, validation_types=[kind])
    result = handler.validate(request, target, governance=governance, grant=grant)
    assert result.status == "PASS"
    assert grant.consumed is False and grant.revoked is False


@pytest.mark.parametrize("kind", ["PERMISSION", "SCOPE", "SECURITY"])
def test_missing_trusted_context_is_inconclusive(handler, validation_request, target, kind):
    result = handler.validate(with_request(validation_request, validation_types=[kind]), target)
    assert result.status == "INCONCLUSIVE" and result.blocking


@pytest.mark.parametrize("kind", ["PERMISSION", "SCOPE"])
@pytest.mark.parametrize(
    "field,value",
    [("revoked", True), ("consumed", True), ("task_id", "other"), ("target", "other")],
)
def test_stale_or_unbound_permission_fails(
    handler, validation_request, target, governance, grant, kind, field, value
):
    result = handler.validate(
        with_request(validation_request, validation_types=[kind]),
        target,
        governance=governance,
        grant=grant.model_copy(update={field: value}),
    )
    assert result.status == "FAIL" and result.blocking


def test_permission_expiry_is_checked_at_validation_time(
    handler, validation_request, target, governance, grant, now
):
    result = handler.validate(
        with_request(validation_request, validation_types=["PERMISSION"]),
        target,
        governance=governance,
        grant=grant.model_copy(update={"expires_at": now}),
    )
    assert result.status == "FAIL"


def test_out_of_scope_operation_fails(handler, validation_request, target, governance, grant):
    governance = governance.model_copy(
        update={"scope": governance.scope.model_copy(update={"sections": ("other",)})}
    )
    result = handler.validate(
        with_request(validation_request, validation_types=["SCOPE"]),
        target,
        governance=governance,
        grant=grant,
    )
    assert result.status == "FAIL"


@pytest.mark.parametrize(
    "field,value", [("task_id", "other"), ("requester", "OTHER"), ("target", "other")]
)
def test_context_for_another_validation_target_fails(
    handler, validation_request, target, governance, grant, field, value
):
    result = handler.validate(
        with_request(validation_request, validation_types=["SECURITY"]),
        target,
        governance=governance.model_copy(update={field: value}),
        grant=grant,
        security=VERIFIED,
    )
    assert result.status == "FAIL"


@pytest.mark.parametrize("field", ["paused", "critical_conflict", "sensitive_data"])
def test_security_signals_block(handler, validation_request, target, field):
    security = SecurityContext(verified=True, **{field: True})
    result = handler.validate(
        with_request(validation_request, validation_types=["SECURITY"]), target, security=security
    )
    assert result.status == "FAIL" and result.blocking


@pytest.mark.parametrize(
    "field,value",
    [
        ("apiKey", "FAKE-SECRET"),
        ("notes", "Bearer FAKE-TOKEN"),
        ("execution_authority", "FULL"),
        ("autonomy_level", 1),
        ("phase", "11"),
        ("operation", "EXTERNAL_ACTION"),
        ("operation", "RUN_CODE"),
        ("operation", "CONNECT_TOOL"),
        ("operation", "ACTIVATE_AGENT"),
    ],
)
def test_security_rejects_sensitive_or_disabled_payload_features(
    handler, validation_request, target, field, value
):
    target.payload[field] = value
    result = handler.validate(
        with_request(validation_request, validation_types=["SECURITY"]), target, security=VERIFIED
    )
    assert result.status == "FAIL" and result.blocking


def test_security_checks_cannot_be_downgraded_to_optional(handler, validation_request, target):
    request = with_request(
        validation_request,
        validation_types=["SECURITY"],
        criteria=[rule(kind="SECURITY", required=False, path=("missing",))],
    )
    result = handler.validate(request, target, security=VERIFIED)
    assert result.status == "FAIL" and result.blocking


def test_all_eight_initial_dimensions_can_run_together(
    handler, validation_request, target, governance, grant, store
):
    consistency = rule(
        "FIELD_EQUALS", kind="CONSISTENCY", path=("created_by",), other_path=["original_request"]
    )
    consistency["criterion_id"] = "consistency_test"
    request = with_request(
        validation_request,
        validation_types=[
            "RULE",
            "CANONICAL",
            "STRUCTURE",
            "COMPLETENESS",
            "CONSISTENCY",
            "SECURITY",
            "SCOPE",
            "PERMISSION",
        ],
        criteria=[rule(), consistency],
    )
    result = handler.validate(
        request, target, governance=governance, grant=grant, security=VERIFIED
    )
    assert result.status == "PASS" and not result.blocking
    assert {check["validation_type"] for check in result.checks} == set(request.validation_types)
    assert store.read_events()[0].result["approved"] is False


def test_input_snapshot_isolated_before_clock_callback(store, validation_request, target, now):
    def clock():
        target.payload.clear()
        return now

    result = ValidationHandler(AuditWriter(store), clock=clock).validate(validation_request, target)
    assert result.status == "PASS"
    assert target.payload == {}


def test_nan_payload_cannot_become_a_valid_null(target):
    payload = target.model_dump(mode="json")
    payload["payload"]["risk"] = float("nan")
    with pytest.raises(ValidationError):
        ValidationTarget.model_validate(payload)


def test_target_data_is_not_trimmed_or_rewritten(target):
    data = target.model_dump(mode="json")
    data["payload"]["objective"] = "  preserve exact bytes  "
    assert ValidationTarget.model_validate(data).payload["objective"] == "  preserve exact bytes  "


def test_naive_clock_is_rejected(store, validation_request, target):
    handler = ValidationHandler(AuditWriter(store), clock=lambda: datetime(2026, 9, 3))
    with pytest.raises(ValueError, match="timezone-aware"):
        handler.validate(validation_request, target)


def test_external_governance_operation_does_not_pass_security(
    handler, validation_request, target, governance
):
    result = handler.validate(
        with_request(validation_request, validation_types=["SECURITY"]),
        target,
        governance=governance.model_copy(update={"operation": Operation.EXTERNAL_ACTION}),
        security=VERIFIED,
    )
    assert result.status == "FAIL"
