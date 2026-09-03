import pytest

from robert.audit import AuditWriteError, AuditWriter
from robert.contracts.audit import EvidenceRef
from robert.contracts.base import ValidationType
from robert.contracts.registry import CONTRACT_REGISTRY
from robert.contracts.validation import ValidationResult
from robert.validation import ValidationHandler, ValidationTarget
from tests.contracts.schema_samples import build_valid_payload
from tests.validation.conftest import rule, with_request


def test_valid_contract_result_is_canonical_and_audited(handler, validation_request, target, store):
    result = handler.validate(validation_request, target)
    assert result.status == "PASS"
    assert result.blocking is False
    assert ValidationResult.model_validate_json(result.model_dump_json()) == result
    event = store.read_events()[0]
    assert result.audit_reference == event.event_id
    assert event.result["approved"] is False
    assert event.result["execution_authority"] == "NONE"
    assert event.result["executed"] is False
    assert result.requester == validation_request.requester
    assert result.confidence is None and result.limitations and result.recommended_next_step


@pytest.mark.parametrize("registration", CONTRACT_REGISTRY, ids=lambda r: r.name.value)
def test_all_registered_contracts_validate_without_a_parallel_schema(
    handler, validation_request, registration
):
    payload = build_valid_payload(registration.model.model_json_schema())
    if "task_id" in payload:
        payload["task_id"] = "task_test"
    request = with_request(
        validation_request,
        target_type=registration.name.value,
        expected_contract={"name": registration.name.value, "version": "0.1"},
    )
    target = ValidationTarget(
        target_ref=request.target_ref,
        task_id=request.task_id,
        target_type=request.target_type,
        payload=payload,
    )
    assert handler.validate(request, target).status == "PASS"


@pytest.mark.parametrize(
    "field,value",
    [
        ("contract_version", "9.9"),
        ("status", "UNKNOWN"),
        ("objective", 123),
        ("unknown_field", True),
        ("created_at", "not-a-date"),
    ],
)
def test_invalid_contract_values_fail_without_coercion(
    handler, validation_request, target, field, value
):
    target.payload[field] = value
    assert handler.validate(validation_request, target).status == "FAIL"


@pytest.mark.parametrize("kind", ["STRUCTURE", "COMPLETENESS"])
def test_missing_required_fields_fail(handler, validation_request, target, kind):
    target.payload.pop("objective")
    result = handler.validate(with_request(validation_request, validation_types=[kind]), target)
    assert result.status == "FAIL" and result.blocking


def test_structure_rejects_wrong_value_types(handler, validation_request, target):
    target.payload["context_refs"] = "not-an-array"
    assert (
        handler.validate(
            with_request(validation_request, validation_types=["STRUCTURE"]), target
        ).status
        == "FAIL"
    )


@pytest.mark.parametrize(
    "field,value", [("task_id", "other"), ("target_ref", "other"), ("target_type", "OTHER")]
)
def test_mismatched_target_binding_fails(handler, validation_request, target, field, value):
    altered = target.model_copy(update={field: value})
    result = handler.validate(validation_request, altered)
    assert result.status == "FAIL" and result.blocking


def test_required_rule_failure_is_blocking(handler, validation_request, target):
    request = with_request(
        validation_request, validation_types=["RULE"], criteria=[rule(path=("missing",))]
    )
    result = handler.validate(request, target)
    assert result.status == "FAIL" and result.blocking
    assert any(item["status"] == "FAIL" for item in result.checks)


def test_optional_rule_failure_is_a_warning(handler, validation_request, target):
    request = with_request(
        validation_request,
        validation_types=["RULE"],
        criteria=[rule(required=False, path=("missing",))],
    )
    result = handler.validate(request, target)
    assert result.status == "PASS_WITH_WARNINGS" and not result.blocking
    assert result.issues[0]["kind"] == "WARNING"


@pytest.mark.parametrize("required", [True, False])
def test_conflicts_are_carried_in_issues(handler, validation_request, target, required):
    criterion = rule("FIELD_EQUALS", kind="CONSISTENCY", other_path=["task_id"], required=required)
    request = with_request(
        validation_request, validation_types=["CONSISTENCY"], criteria=[criterion]
    )
    result = handler.validate(request, target)
    assert result.status == ("FAIL" if required else "PASS_WITH_WARNINGS")
    assert result.issues[0]["kind"] == ("CONFLICT" if required else "WARNING")
    assert result.issues[0]["conflict"] is True


@pytest.mark.parametrize(
    "kind",
    [
        kind.value
        for kind in ValidationType
        if kind.value in ("EVIDENCE", "SOURCE", "MEMORY", "MODEL_OUTPUT")
    ],
)
def test_unavailable_validation_capability_is_inconclusive(
    handler, validation_request, target, kind
):
    result = handler.validate(with_request(validation_request, validation_types=[kind]), target)
    assert result.status == "INCONCLUSIVE" and result.blocking


@pytest.mark.parametrize(
    "field,value",
    [
        ("validation_types", []),
        ("validation_types", ["CANONICAL", "CANONICAL"]),
        ("reviewer_roles", []),
        ("reviewer_roles", ["MODEL"]),
        ("reviewer_roles", ["RULE_SYSTEM", "AGENT"]),
        ("expected_contract", {}),
        ("expected_contract", {"name": "UNKNOWN", "version": "0.1"}),
        ("expected_contract", {"name": "TASK", "version": "9.9"}),
        ("blocking_policy", {"fail_closed": False}),
        ("blocking_policy", {"skip_security": True}),
        ("permission_context", {"status": "ALLOWED"}),
        ("scope_context", {"status": "WITHIN_SCOPE"}),
        ("risk_context", {"risk_level": 0}),
    ],
)
def test_missing_or_unsupported_request_requirements_never_pass(
    handler, validation_request, target, field, value
):
    result = handler.validate(with_request(validation_request, **{field: value}), target)
    assert result.status == "INCONCLUSIVE" and result.blocking


def test_evidence_and_sources_preserve_supplied_references(
    handler, validation_request, target, now
):
    ref = EvidenceRef(
        contract_version="0.1",
        ref_id="source_test",
        source_type="DOCUMENT",
        source_location="local:document",
        source_authority="USER",
        created_at=now,
        freshness="SUPPLIED",
    )
    request = with_request(
        validation_request,
        evidence_requirements=["source_test"],
        source_requirements=["source_test"],
    )
    result = handler.validate(
        request, target.model_copy(update={"evidence": (ref,), "sources": (ref,)})
    )
    assert result.status == "PASS"
    assert result.evidence[0]["ref_id"] == result.sources[0]["ref_id"] == "source_test"
    assert any("not independently" in item for item in result.limitations)


@pytest.mark.parametrize("field", ["evidence_requirements", "source_requirements"])
def test_missing_evidence_or_source_is_not_invented(handler, validation_request, target, field):
    result = handler.validate(with_request(validation_request, **{field: ["missing"]}), target)
    assert result.status == "INCONCLUSIVE" and result.blocking
    assert result.confidence is None


def test_audit_failure_prevents_returning_pass(validation_request, target):
    class UnavailableStore:
        def append(self, payload):
            raise OSError("synthetic failure")

    with pytest.raises(AuditWriteError):
        ValidationHandler(AuditWriter(UnavailableStore())).validate(validation_request, target)


def test_payload_and_pydantic_error_values_are_not_copied_to_audit(
    handler, validation_request, target, store
):
    target.payload["status"] = "FAKE_PRIVATE_VALUE"
    result = handler.validate(validation_request, target)
    assert "FAKE_PRIVATE_VALUE" not in result.model_dump_json()
    assert "FAKE_PRIVATE_VALUE" not in store.file_path.read_text()
