import json
from collections.abc import Mapping
from datetime import datetime
from pathlib import Path

import pytest

from robert.audit.event_builder import AuditEventBuilder
from robert.audit.storage import JsonLinesAuditStore
from robert.audit.writer import AuditWriteError, AuditWriter


def _build_event(builder: AuditEventBuilder, **overrides: object):
    values = {
        "task_id": "task_1",
        "event_type": "VALID_REQUEST",
        "actor": "USER",
        "component": "API",
        "action": "VALIDATE_REQUEST",
        "target": "TASK",
        "result": {"status": "VALID"},
    }
    values.update(overrides)
    return builder.build(**values)


def test_writer_persists_one_canonical_event_per_line(
    tmp_path: Path, event_builder: AuditEventBuilder
) -> None:
    store = JsonLinesAuditStore(tmp_path / "audit" / "events.jsonl")
    writer = AuditWriter(store)

    written = writer.write(_build_event(event_builder))

    assert store.read_events() == (written,)
    assert len(store.file_path.read_text(encoding="utf-8").splitlines()) == 1


def test_writer_appends_without_rewriting_history(tmp_path: Path, fixed_time: datetime) -> None:
    event_ids = iter(("audit_evt_1", "audit_evt_2"))
    builder = AuditEventBuilder(
        clock=lambda: fixed_time,
        event_id_factory=lambda: next(event_ids),
    )
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")
    writer = AuditWriter(store)

    writer.write(_build_event(builder))
    first_line = store.file_path.read_text(encoding="utf-8").splitlines()[0]
    writer.write(_build_event(builder, result={"status": "BLOCKED"}))

    lines = store.file_path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == first_line
    assert len(lines) == 2


def test_writer_redacts_nested_secrets_but_preserves_non_secret_counts(
    tmp_path: Path, event_builder: AuditEventBuilder
) -> None:
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")
    writer = AuditWriter(store)
    event = _build_event(
        event_builder,
        metadata={
            "api_key": "secret-value",
            "nested": {"access_token": "token-value"},
            "token_count": 42,
            "full_model_prompt": "unnecessarily duplicated prompt",
        },
    )

    writer.write(event)

    payload = json.loads(store.file_path.read_text(encoding="utf-8"))
    assert payload["metadata"]["api_key"] == "[REDACTED]"
    assert payload["metadata"]["nested"]["access_token"] == "[REDACTED]"
    assert payload["metadata"]["token_count"] == 42
    assert payload["metadata"]["full_model_prompt"] == "[OMITTED: USE REFERENCE]"


def test_store_requires_explicit_json_lines_extension(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match=".jsonl"):
        JsonLinesAuditStore(tmp_path / "events.json")


def test_audit_write_failure_is_not_silent(event_builder: AuditEventBuilder) -> None:
    class FailingStore:
        def append(self, payload: Mapping[str, object]) -> None:
            raise OSError("disk unavailable")

    writer = AuditWriter(FailingStore())

    with pytest.raises(AuditWriteError, match="could not be persisted"):
        writer.write(_build_event(event_builder))
