from datetime import UTC, datetime, timedelta

import pytest

from robert.audit import AuditWriter, JsonLinesAuditStore
from robert.contracts.memory import MemoryRecord, MemoryRetrievalRequest
from robert.governance.inputs import OperationScope, PermissionGrant, SecurityContext
from robert.memory import InMemoryMemoryRepository, MemoryRetriever


@pytest.fixture
def now():
    return datetime(2026, 9, 3, 12, tzinfo=UTC)


@pytest.fixture
def scope():
    return OperationScope(
        project="ROBERT_MASTER_SYSTEM", sections=("architecture",), phase=10, mode="MANUAL"
    )


@pytest.fixture
def record(now, scope):
    return MemoryRecord(
        contract_version="0.1",
        memory_id="memory_test",
        content={"preference": "clear names"},
        memory_type="SEMANTIC",
        retention="PERSISTENT",
        created_at=now - timedelta(days=2),
        updated_at=now - timedelta(days=1),
        source="manual:approved_convention",
        authority_metadata={
            "readers": ["USER"],
            "confidence": 0.9,
            "confidence_source": "USER_EXPLICIT",
        },
        scope=scope.model_dump(mode="json"),
        sensitivity="INTERNAL",
        evidence_refs=["evidence_1"],
        decision_refs=["decision_1"],
        validation_state={"status": "PASS", "verified_at": now.isoformat()},
        status="ACTIVE",
    )


@pytest.fixture
def retrieval_request(scope):
    return MemoryRetrievalRequest(
        contract_version="0.1",
        request_id="retrieval_1",
        task_id="task_test",
        requester="USER",
        query="clear names",
        memory_types=["SEMANTIC"],
        retention_classes=["PERSISTENT"],
        scope=scope.model_dump(mode="json"),
        freshness_requirement={"max_age_seconds": 86400},
        confidence_requirement=0.8,
        sensitivity_constraints=["INTERNAL"],
        max_results=3,
        purpose="Apply the project naming convention",
    )


@pytest.fixture
def grant(now, scope):
    return make_grant(now, scope, "memory_repository")


def make_grant(now, scope, target, operation="READ_DOCUMENT", **updates):
    data = dict(
        grant_id="grant_memory",
        task_id="task_test",
        requester="USER",
        issued_by="USER",
        operation=operation,
        target=target,
        scope=scope,
        max_risk=2,
        issued_at=now - timedelta(hours=1),
        expires_at=now + timedelta(hours=1),
    )
    data.update(updates)
    return PermissionGrant(**data)


@pytest.fixture
def security():
    return SecurityContext(verified=True)


@pytest.fixture
def store(tmp_path):
    return JsonLinesAuditStore(tmp_path / "memory_audit.jsonl")


@pytest.fixture
def writer(store):
    return AuditWriter(store)


@pytest.fixture
def repository(record):
    return InMemoryMemoryRepository("memory_repository", [record])


@pytest.fixture
def retriever(repository, writer, now):
    return MemoryRetriever(repository, writer, clock=lambda: now)


def changed(model, **updates):
    data = model.model_dump(mode="json")
    data.update(updates)
    return type(model).model_validate(data)
