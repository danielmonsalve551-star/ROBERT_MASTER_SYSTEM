from pathlib import Path

from robert.audit.catalog import ErrorAndBlockingEvent
from robert.audit.event_builder import AuditEventBuilder
from robert.audit.outcome_builder import ErrorAndBlockBuilder
from robert.audit.storage import JsonLinesAuditStore
from robert.audit.writer import AuditWriter


def test_valid_request_produces_audit_event(
    tmp_path: Path, event_builder: AuditEventBuilder
) -> None:
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")
    event = event_builder.build(
        task_id="task_valid",
        event_type="VALID_REQUEST",
        actor="USER",
        component="API",
        action="VALIDATE_REQUEST",
        target="TASK",
        result={"status": "VALID"},
    )

    AuditWriter(store).write(event)

    assert store.read_events()[0].result == {"status": "VALID"}


def test_invalid_request_produces_error_and_audit_event(
    tmp_path: Path,
    event_builder: AuditEventBuilder,
    outcome_builder: ErrorAndBlockBuilder,
) -> None:
    error = outcome_builder.build_error(
        task_id="task_invalid",
        event=ErrorAndBlockingEvent.MISSING_INFORMATION,
        source_component="API",
        message="objective is required",
        recoverable=True,
    )
    event = event_builder.build(
        task_id=error.task_id,
        event_type="INVALID_REQUEST",
        actor="USER",
        component="API",
        action="VALIDATE_REQUEST",
        target="TASK",
        result={"status": "ERROR"},
        error_ref=error.error_id,
    )
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")

    AuditWriter(store).write(event)

    assert store.read_events()[0].error_ref == error.error_id


def test_blocked_request_produces_block_and_audit_event(
    tmp_path: Path,
    event_builder: AuditEventBuilder,
    outcome_builder: ErrorAndBlockBuilder,
) -> None:
    block = outcome_builder.build_block(
        task_id="task_blocked",
        event=ErrorAndBlockingEvent.UNAUTHORIZED_EXECUTION,
        source_component="APPROVAL_GATE",
        reason="Execution authority is NONE",
        required_resolution="Obtain separate authorization",
        user_action_required=True,
        approval_required=True,
    )
    event = event_builder.build(
        task_id=block.task_id,
        event_type="BLOCKED_REQUEST",
        actor="SYSTEM_RULE",
        component="APPROVAL_GATE",
        action="BLOCK_REQUEST",
        target="TASK",
        output_refs=[block.block_id],
        risk_state={"level": 4},
        result={"status": "BLOCKED"},
    )
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")

    AuditWriter(store).write(event)

    assert store.read_events()[0].output_refs == [block.block_id]
