import pytest

from robert.audit import AuditWriteError
from robert.contracts.memory import MemoryCandidate, MemoryRecord
from robert.governance.inputs import GovernanceRequest
from robert.memory import CandidateDraft, MemoryCandidateService
from tests.memory.conftest import changed, make_grant


@pytest.fixture
def draft(scope):
    return CandidateDraft(
        task_id="task_test",
        source="MODEL_OUTPUT",
        content={"preference": "clear names"},
        memory_type="SEMANTIC",
        proposed_retention="PERSISTENT",
        reason="Reusable naming preference",
        confidence=0.8,
        sensitivity="INTERNAL",
        scope=scope,
    )


@pytest.fixture
def service(writer, now):
    return MemoryCandidateService(writer, clock=lambda: now)


def candidate_context(candidate, scope, now):
    governance = GovernanceRequest(
        request_id="candidate_review",
        task_id=candidate.task_id,
        requester="USER",
        operation="PREPARE_DRAFT",
        target=candidate.candidate_id,
        scope=scope,
    )
    return governance, make_grant(now, scope, candidate.candidate_id, "PREPARE_DRAFT")


def test_model_output_remains_candidate_after_pass(service, draft, scope, now, security, store):
    candidate = service.create(draft, requester="USER")
    governance, grant = candidate_context(candidate, scope, now)
    result = service.validate(
        candidate, requester="USER", governance=governance, grant=grant, security=security
    )
    assert result.status == "PASS" and not result.blocking
    assert isinstance(candidate, MemoryCandidate) and not isinstance(candidate, MemoryRecord)
    assert candidate.validation_state == {"status": "PENDING"}
    assert candidate.source == "MODEL_OUTPUT"
    assert result.confidence is None
    events = store.read_events()
    assert events[0].output_refs == [candidate.candidate_id]
    assert events[0].result["persisted_memory"] is False
    assert "clear names" not in " ".join(e.model_dump_json() for e in events)
    assert result.audit_reference == events[-1].event_id


@pytest.mark.parametrize(
    "field,value",
    [
        ("source", "  "),
        ("reason", "  "),
        ("content", {}),
        ("content", None),
        ("sensitivity", "SECRET"),
        ("sensitivity", "UNKNOWN"),
        ("content", {"password": "private-value"}),
        ("conflict_state", {"status": "CONFLICTED"}),
        ("conflict_state", {"status": "NONE_REPORTED", "skip_checks": True}),
        ("validation_state", {"status": "APPROVED"}),
    ],
)
def test_invalid_candidates_never_pass(service, draft, scope, now, security, field, value):
    candidate = changed(service.create(draft, requester="USER"), **{field: value})
    governance, grant = candidate_context(candidate, scope, now)
    result = service.validate(
        candidate, requester="USER", governance=governance, grant=grant, security=security
    )
    assert result.status == "FAIL" and result.blocking


def test_untrusted_missing_context_is_inconclusive(service, draft):
    candidate = service.create(draft, requester="USER")
    result = service.validate(candidate, requester="USER")
    assert result.status == "INCONCLUSIVE" and result.blocking


def test_scope_mismatch_fails(service, draft, scope, now, security):
    candidate = service.create(
        changed(draft, scope={**scope.model_dump(mode="json"), "project": "OTHER"}),
        requester="USER",
    )
    governance, grant = candidate_context(candidate, scope, now)
    assert (
        service.validate(
            candidate, requester="USER", governance=governance, grant=grant, security=security
        ).status
        == "FAIL"
    )


@pytest.mark.parametrize("risk", [3, 4])
def test_high_or_critical_risk_not_approved_by_candidate_validation(
    service, draft, scope, now, security, risk
):
    candidate = service.create(draft, requester="USER")
    governance, grant = candidate_context(candidate, scope, now)
    with pytest.raises(PermissionError):
        service.validate(
            candidate,
            requester="USER",
            governance=changed(governance, declared_risk=risk),
            grant=changed(grant, max_risk=4),
            security=security,
        )


def test_candidate_creation_audit_failure_prevents_return(service, draft, writer, monkeypatch):
    def fail(event):
        raise AuditWriteError("offline")

    monkeypatch.setattr(writer, "write", fail)
    with pytest.raises(AuditWriteError):
        service.create(draft, requester="USER")


def test_candidate_creation_detaches_payload(service, draft):
    candidate = service.create(draft, requester="USER")
    draft.content["preference"] = "mutated"
    assert candidate.content == {"preference": "clear names"}
    assert not hasattr(service, "promote") and not hasattr(service, "save")
