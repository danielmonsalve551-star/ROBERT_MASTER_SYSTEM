from datetime import timedelta

import pytest

from robert.audit import AuditWriteError
from robert.memory import InMemoryMemoryRepository, MemoryRetriever
from tests.memory.conftest import changed


def test_expiration_during_repository_read_blocks_disclosure(
    repository, writer, now, retrieval_request, grant, security
):
    ticks = iter([now, now + timedelta(hours=2)])
    retriever = MemoryRetriever(repository, writer, clock=lambda: next(ticks))
    result = retriever.retrieve(retrieval_request, grant=grant, security=security)
    assert result.status == "DENIED" and not result.records


def test_minimum_verification_date_is_enforced(retriever, retrieval_request, grant, security, now):
    retrieval_request = changed(
        retrieval_request,
        freshness_requirement={"verified_after": (now + timedelta(seconds=1)).isoformat()},
    )
    assert retriever.retrieve(retrieval_request, grant=grant, security=security).status == "EMPTY"


def test_unknown_confidence_allowed_only_without_requirement(
    record, writer, now, retrieval_request, grant, security
):
    record = changed(record, authority_metadata={"readers": ["USER"]})
    retriever = MemoryRetriever(
        InMemoryMemoryRepository("memory_repository", [record]), writer, clock=lambda: now
    )
    assert retriever.retrieve(retrieval_request, grant=grant, security=security).status == "EMPTY"
    assert (
        retriever.retrieve(
            changed(retrieval_request, confidence_requirement=None), grant=grant, security=security
        ).status
        == "SUCCESS"
    )


def test_final_retrieval_audit_failure_prevents_disclosure(
    retriever, retrieval_request, grant, security, writer, monkeypatch
):
    original = writer.write

    def write(event):
        if event.component == "MEMORY_RETRIEVAL":
            raise AuditWriteError("offline")
        return original(event)

    monkeypatch.setattr(writer, "write", write)
    with pytest.raises(AuditWriteError):
        retriever.retrieve(retrieval_request, grant=grant, security=security)


@pytest.mark.parametrize("shape", ["lazy", "duplicate", "too_large", "invalid"])
def test_unreliable_repository_snapshots_are_inconclusive(
    repository, record, writer, now, retrieval_request, grant, security, shape, monkeypatch
):
    snapshots = {
        "lazy": iter([record]),
        "duplicate": (record, record),
        "too_large": (record,) * 10001,
        "invalid": ({"content": "untrusted"},),
    }
    monkeypatch.setattr(repository, "read", lambda scope: snapshots[shape])
    result = MemoryRetriever(repository, writer, clock=lambda: now).retrieve(
        retrieval_request, grant=grant, security=security
    )
    assert result.status == "INCONCLUSIVE" and not result.records


def test_naive_clock_is_rejected(repository, writer, now, retrieval_request):
    with pytest.raises(ValueError, match="timezone-aware"):
        MemoryRetriever(repository, writer, clock=lambda: now.replace(tzinfo=None)).retrieve(
            retrieval_request
        )
