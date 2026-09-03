from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from robert.audit import AuditWriter, JsonLinesAuditStore
from robert.governance import (
    GovernanceEngine,
    GovernanceRequest,
    Operation,
    OperationScope,
    PermissionGrant,
)


@pytest.fixture
def now():
    return datetime(2026, 9, 3, 12, tzinfo=UTC)


@pytest.fixture
def request_data():
    return GovernanceRequest(
        request_id="request_test",
        task_id="task_test",
        requester="USER",
        operation=Operation.PREPARE_DRAFT,
        target="README.md",
        scope=OperationScope(
            project="ROBERT_MASTER_SYSTEM", sections=("summary",), phase=10, mode="MANUAL"
        ),
    )


@pytest.fixture
def grant(request_data, now):
    return PermissionGrant(
        grant_id="grant_test",
        task_id=request_data.task_id,
        requester="USER",
        issued_by="USER",
        operation=request_data.operation,
        target=request_data.target,
        scope=request_data.scope,
        max_risk=3,
        issued_at=now - timedelta(hours=1),
        expires_at=now + timedelta(hours=1),
    )


@pytest.fixture
def audit_store(tmp_path: Path):
    return JsonLinesAuditStore(tmp_path / "governance.jsonl")


@pytest.fixture
def engine(audit_store, now):
    return GovernanceEngine(AuditWriter(audit_store), clock=lambda: now)
