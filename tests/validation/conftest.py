from datetime import UTC, datetime, timedelta

import pytest

from robert.audit import AuditWriter, JsonLinesAuditStore
from robert.contracts.task import Task
from robert.contracts.validation import ValidationRequest
from robert.governance import GovernanceRequest, OperationScope, PermissionGrant
from robert.validation import ValidationHandler, ValidationTarget
from tests.contracts.schema_samples import build_valid_payload


@pytest.fixture
def now():
    return datetime(2026, 9, 3, 12, tzinfo=UTC)


@pytest.fixture
def validation_request():
    payload = build_valid_payload(ValidationRequest.model_json_schema())
    payload.update(
        validation_id="validation_test",
        task_id="task_test",
        requester="USER",
        target_type="TASK",
        target_ref="artifact_test",
        validation_types=["CANONICAL"],
        reviewer_roles=["RULE_SYSTEM"],
        expected_contract={"name": "TASK", "version": "0.1"},
    )
    return ValidationRequest.model_validate(payload)


@pytest.fixture
def target():
    payload = build_valid_payload(Task.model_json_schema())
    payload.update(task_id="task_test", phase="10")
    return ValidationTarget(
        task_id="task_test", target_ref="artifact_test", target_type="TASK", payload=payload
    )


@pytest.fixture
def store(tmp_path):
    return JsonLinesAuditStore(tmp_path / "validation.jsonl")


@pytest.fixture
def handler(store, now):
    return ValidationHandler(AuditWriter(store), clock=lambda: now)


@pytest.fixture
def governance():
    return GovernanceRequest(
        request_id="governance_request",
        task_id="task_test",
        requester="USER",
        operation="READ_DOCUMENT",
        target="artifact_test",
        scope=OperationScope(
            project="ROBERT_MASTER_SYSTEM", sections=("all",), phase=10, mode="MANUAL"
        ),
    )


@pytest.fixture
def grant(governance, now):
    return PermissionGrant(
        grant_id="grant_test",
        task_id=governance.task_id,
        requester="USER",
        issued_by="USER",
        operation=governance.operation,
        target=governance.target,
        scope=governance.scope,
        max_risk=3,
        issued_at=now - timedelta(hours=1),
        expires_at=now + timedelta(hours=1),
    )


def with_request(request, **updates):
    data = request.model_dump(mode="json")
    data.update(updates)
    return ValidationRequest.model_validate(data)


def rule(method="EXISTS", *, kind="RULE", required=True, path=("objective",), **extra):
    return dict(
        criterion_id="criterion_test",
        validation_type=kind,
        method=method,
        path=list(path),
        required=required,
        **extra,
    )
