from datetime import timedelta

import pytest

from robert.audit import AuditWriteError
from robert.contracts.memory import MemoryRetrievalResult
from robert.memory import InMemoryMemoryRepository, MemoryRepositoryError, MemoryRetriever
from tests.memory.conftest import changed


def test_authorized_retrieval_is_canonical_and_audited(
    retriever, retrieval_request, grant, security, store
):
    result = retriever.retrieve(retrieval_request, grant=grant, security=security)
    assert result.status == "SUCCESS"
    assert [r.memory_id for r in result.records] == ["memory_test"]
    assert MemoryRetrievalResult.model_validate_json(result.model_dump_json()) == result
    events = store.read_events()
    assert result.audit_reference == events[-1].event_id
    assert events[-1].result["persisted_memory"] is False
    assert "clear names" not in " ".join(e.model_dump_json() for e in events)
    assert result.records[0].source == "manual:approved_convention"
    assert result.records[0].decision_refs == ["decision_1"]


@pytest.mark.parametrize(
    "field,value",
    [
        ("requester", "OTHER"),
        ("task_id", "task_other"),
        ("target", "other_repository"),
        ("operation", "PREPARE_DRAFT"),
        ("revoked", True),
        ("consumed", True),
    ],
)
def test_denied_permission_never_calls_repository(
    repository, writer, now, retrieval_request, grant, security, field, value
):
    def forbidden(scope):
        pytest.fail("repository was accessed before authorization")

    repository.read = forbidden
    result = MemoryRetriever(repository, writer, clock=lambda: now).retrieve(
        retrieval_request, grant=changed(grant, **{field: value}), security=security
    )
    assert result.status == "DENIED" and not result.records


def test_no_grant_no_access(retriever, retrieval_request, security):
    assert retriever.retrieve(retrieval_request, security=security).status == "DENIED"


@pytest.mark.parametrize("flag", ["paused", "critical_conflict", "sensitive_data"])
def test_security_blocks(retriever, retrieval_request, grant, security, flag):
    assert (
        retriever.retrieve(
            retrieval_request, grant=grant, security=changed(security, **{flag: True})
        ).status
        == "DENIED"
    )


def test_missing_security_blocks(retriever, retrieval_request, grant):
    assert retriever.retrieve(retrieval_request, grant=grant).status == "DENIED"


def test_expired_permission_blocks(retriever, retrieval_request, grant, security, now):
    grant = changed(
        grant, issued_at=(now - timedelta(days=1)).isoformat(), expires_at=now.isoformat()
    )
    assert retriever.retrieve(retrieval_request, grant=grant, security=security).status == "DENIED"


@pytest.mark.parametrize(
    "field,value",
    [
        ("query", "*"),
        ("query", " " * 2),
        ("query", "a" * 2001),
        ("purpose", "  "),
        ("memory_types", []),
        ("memory_types", ["SEMANTIC", "SEMANTIC"]),
        ("retention_classes", []),
        ("retention_classes", ["PERSISTENT", "PERSISTENT"]),
        ("sensitivity_constraints", []),
        ("sensitivity_constraints", ["SECRET"]),
        ("sensitivity_constraints", [{"allow_all": True}]),
        ("max_results", 51),
        ("freshness_requirement", {"max_age_seconds": True}),
        ("freshness_requirement", {"max_age_seconds": -1}),
        ("freshness_requirement", {"allow_stale": True}),
        ("scope", {}),
    ],
)
def test_unknown_or_unbounded_requests_fail_closed(
    retriever, retrieval_request, grant, security, field, value
):
    result = retriever.retrieve(
        changed(retrieval_request, **{field: value}), grant=grant, security=security
    )
    assert result.status == "INCONCLUSIVE" and not result.records


@pytest.mark.parametrize(
    "field,value",
    [
        ("project", "OTHER_PROJECT"),
        ("sections", ["secret"]),
        ("sections", ["*"]),
        ("phase", 11),
        ("mode", "SANDBOX"),
    ],
)
def test_request_cannot_expand_scope(retriever, retrieval_request, grant, security, field, value):
    scope = {**retrieval_request.scope, field: value}
    assert (
        retriever.retrieve(
            changed(retrieval_request, scope=scope), grant=grant, security=security
        ).status
        == "DENIED"
    )


@pytest.mark.parametrize(
    "field,value",
    [
        (
            "scope",
            {"project": "OTHER", "sections": ["architecture"], "phase": 10, "mode": "MANUAL"},
        ),
        (
            "scope",
            {
                "project": "ROBERT_MASTER_SYSTEM",
                "sections": ["secret"],
                "phase": 10,
                "mode": "MANUAL",
            },
        ),
        ("authority_metadata", {"readers": ["OTHER"]}),
        ("authority_metadata", {"readers": ["*"]}),
        ("authority_metadata", {"readers": ["USER"], "confidence": 0.99}),
        (
            "authority_metadata",
            {"readers": ["USER"], "confidence": 0.1, "confidence_source": "USER_EXPLICIT"},
        ),
        ("authority_metadata", {"readers": ["USER"], "admin": True}),
        ("sensitivity", "SECRET"),
        ("sensitivity", "PRIVATE"),
        ("sensitivity", "UNKNOWN"),
        ("retention", "TEMPORARY"),
        ("memory_type", "CORE"),
        ("status", "REVOKED"),
        ("status", "DELETED"),
        ("status", "SUPERSEDED"),
        ("status", "STALE"),
        ("status", "ARCHIVED"),
        ("source", "  "),
        ("content", {"password": "this-is-sensitive"}),
        ("validation_state", {"status": "PASS"}),
        ("validation_state", {"status": "APPROVED"}),
    ],
)
def test_ineligible_records_disclose_no_ids(
    record, writer, now, retrieval_request, grant, security, field, value
):
    altered = changed(record, **{field: value})
    repository = InMemoryMemoryRepository("memory_repository", [altered])
    result = MemoryRetriever(repository, writer, clock=lambda: now).retrieve(
        retrieval_request, grant=grant, security=security
    )
    assert result.status == "EMPTY" and not result.records and not result.conflicts
    assert record.memory_id not in result.model_dump_json()


@pytest.mark.parametrize(
    "case",
    [
        "expired",
        "future_update",
        "future_validation",
        "stale",
        "unverified",
        "wrong_task",
        "temporary_without_expiry",
    ],
)
def test_temporal_and_task_filters(record, writer, now, retrieval_request, grant, security, case):
    metadata = dict(record.authority_metadata)
    state = dict(record.validation_state)
    updates = {}
    if case == "expired":
        metadata["expires_at"] = now.isoformat()
    elif case == "future_update":
        updates["updated_at"] = (now + timedelta(days=1)).isoformat()
    elif case == "future_validation":
        state["verified_at"] = (now + timedelta(seconds=1)).isoformat()
    elif case == "stale":
        state["verified_at"] = (now - timedelta(days=1)).isoformat()
        retrieval_request = changed(retrieval_request, freshness_requirement={"max_age_seconds": 1})
    elif case == "unverified":
        state["status"] = "UNVERIFIED"
    elif case == "wrong_task":
        metadata["task_id"] = "task_other"
    elif case == "temporary_without_expiry":
        updates["retention"] = "TEMPORARY"
        retrieval_request = changed(retrieval_request, retention_classes=["TEMPORARY"])
    altered = changed(record, authority_metadata=metadata, validation_state=state, **updates)
    result = MemoryRetriever(
        InMemoryMemoryRepository("memory_repository", [altered]), writer, clock=lambda: now
    ).retrieve(retrieval_request, grant=grant, security=security)
    assert result.status == "EMPTY"


@pytest.mark.parametrize("retention", ["ACTIVE", "TEMPORARY", "PERSISTENT"])
def test_retention_and_type_are_independent(
    record, writer, now, retrieval_request, grant, security, retention
):
    record = changed(
        record,
        retention=retention,
        authority_metadata={
            **record.authority_metadata,
            "task_id": retrieval_request.task_id,
            "expires_at": (now + timedelta(days=1)).isoformat(),
        },
    )
    retrieval_request = changed(retrieval_request, retention_classes=[retention])
    result = MemoryRetriever(
        InMemoryMemoryRepository("memory_repository", [record]), writer, clock=lambda: now
    ).retrieve(retrieval_request, grant=grant, security=security)
    assert result.status == "SUCCESS" and result.records[0].memory_type == "SEMANTIC"


def test_conflicts_excluded_and_not_resolved(
    record, writer, now, retrieval_request, grant, security
):
    record = changed(
        record,
        validation_state={
            **record.validation_state,
            "status": "CONFLICTED",
            "conflict_refs": ["private_other_record"],
        },
    )
    result = MemoryRetriever(
        InMemoryMemoryRepository("memory_repository", [record]), writer, clock=lambda: now
    ).retrieve(retrieval_request, grant=grant, security=security)
    assert result.status == "EMPTY" and result.conflicts[0]["memory_id"] == record.memory_id
    assert "private_other_record" not in result.model_dump_json()


def test_lexical_ranking_limit_and_exact_duplicate_minimization(
    record, writer, now, retrieval_request, grant, security
):
    records = [
        changed(record, memory_id="z"),
        changed(record, memory_id="a"),
        changed(record, memory_id="b", content="names"),
        changed(record, memory_id="c", content="unrelated"),
    ]
    retriever = MemoryRetriever(
        InMemoryMemoryRepository("memory_repository", reversed(records)), writer, clock=lambda: now
    )
    result = retriever.retrieve(retrieval_request, grant=grant, security=security)
    assert [r.memory_id for r in result.records] == ["a", "b"]
    assert result.ranking_metadata["rank_is_authority"] is False
    assert (
        len(
            retriever.retrieve(
                changed(retrieval_request, max_results=1), grant=grant, security=security
            ).records
        )
        == 1
    )


def test_repository_is_detached_and_read_only(
    record, repository, retriever, retrieval_request, grant, security
):
    record.content["preference"] = "mutated seed"
    first = retriever.retrieve(retrieval_request, grant=grant, security=security)
    first.records[0].content["preference"] = "mutated result"
    assert retriever.retrieve(retrieval_request, grant=grant, security=security).records[
        0
    ].content == {"preference": "clear names"}
    for method in ("add", "save", "write", "delete", "update"):
        assert not hasattr(repository, method)


def test_duplicate_record_ids_rejected(record):
    with pytest.raises(ValueError, match="duplicate"):
        InMemoryMemoryRepository("repo", [record, record])


def test_backend_failure_is_inconclusive_without_exception_payload(
    repository, writer, now, retrieval_request, grant, security
):
    def fail(scope):
        raise MemoryRepositoryError("secret backend contents")

    repository.read = fail
    result = MemoryRetriever(repository, writer, clock=lambda: now).retrieve(
        retrieval_request, grant=grant, security=security
    )
    assert (
        result.status == "INCONCLUSIVE"
        and "secret backend contents" not in result.model_dump_json()
    )


def test_audit_failure_prevents_result(
    retriever, retrieval_request, grant, security, writer, monkeypatch
):
    def fail(event):
        raise AuditWriteError("offline")

    monkeypatch.setattr(writer, "write", fail)
    with pytest.raises(AuditWriteError):
        retriever.retrieve(retrieval_request, grant=grant, security=security)


def test_nonfinite_payload_cannot_enter_repository(record):
    record.content["score"] = float("nan")
    with pytest.raises(ValueError):
        InMemoryMemoryRepository("repo", [record])
