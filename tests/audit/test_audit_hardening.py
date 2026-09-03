from concurrent.futures import ThreadPoolExecutor

import pytest
from pydantic import ValidationError

from robert.audit import AuditWriter, JsonLinesAuditStore
from robert.audit.catalog import (
    ERROR_AND_BLOCKING_EVENT_CATALOG,
    ErrorAndBlockingEvent,
    select_specific_event,
)
from robert.audit.redaction import redact_sensitive_values


def build_event(builder):
    return builder.build(
        task_id="task_test",
        event_type="TEST",
        actor="USER",
        component="TEST",
        action="TEST",
        target="TEST",
        result={"status": "TEST"},
    )


@pytest.mark.parametrize(
    "key", ["apiKey", "APIKey", "privateKey", "accessToken", "credentials", "password"]
)
def test_secret_key_variants_are_redacted(key):
    assert redact_sensitive_values({key: "FAKE-SECRET"})[key] == "[REDACTED]"


def test_bearer_tokens_and_private_key_blocks_are_redacted_from_text():
    text = "message Bearer FAKE-TOKEN and -----BEGIN PRIVATE KEY-----FAKE-----END PRIVATE KEY-----"
    assert "FAKE" not in redact_sensitive_values(text)


def test_store_rejects_invalid_payload_before_creating_file(tmp_path):
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")
    with pytest.raises(ValidationError):
        store.append({"invalid": True})
    assert not store.file_path.exists()


def test_store_direct_write_also_redacts(tmp_path, event_builder):
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")
    payload = build_event(event_builder).model_dump(mode="json")
    payload["metadata"] = {"apiKey": "FAKE-SECRET"}
    store.append(payload)
    assert "FAKE-SECRET" not in store.file_path.read_text()


def test_duplicate_event_cannot_be_appended(tmp_path, event_builder):
    store = JsonLinesAuditStore(tmp_path / "events.jsonl")
    payload = build_event(event_builder).model_dump(mode="json")
    store.append(payload)
    before = store.file_path.read_bytes()
    with pytest.raises(ValueError, match="duplicate"):
        store.append(payload)
    assert store.file_path.read_bytes() == before


def test_incomplete_history_requires_explicit_recovery():
    # Inject corruption without altering existing repository or user data.
    with pytest.raises(ValueError, match="incomplete"):
        JsonLinesAuditStore._decode(b'{"incomplete":')


def test_append_to_corrupt_history_leaves_it_unchanged(tmp_path, event_builder):
    path = tmp_path / "events.jsonl"
    path.write_bytes(b'{"incomplete":')
    with pytest.raises(ValueError, match="incomplete"):
        JsonLinesAuditStore(path).append(build_event(event_builder).model_dump(mode="json"))
    assert path.read_bytes() == b'{"incomplete":'


def test_symlink_store_is_rejected(tmp_path):
    target = tmp_path / "original.jsonl"
    target.touch()
    link = tmp_path / "alias.jsonl"
    link.symlink_to(target)
    with pytest.raises(ValueError, match="symbolic"):
        JsonLinesAuditStore(link)


def test_invalid_utf8_history_is_rejected():
    with pytest.raises(ValueError):
        JsonLinesAuditStore._decode(b"\xff\n")


def test_multiple_store_instances_share_serialization(tmp_path, event_builder):
    path = tmp_path / "events.jsonl"
    template = build_event(event_builder)

    def append(index):
        event = template.model_copy(update={"event_id": f"event_{index}"})
        AuditWriter(JsonLinesAuditStore(path)).write(event)

    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(append, range(12)))
    assert len(JsonLinesAuditStore(path).read_events()) == 12


def test_catalog_is_not_mutable():
    with pytest.raises(TypeError):
        ERROR_AND_BLOCKING_EVENT_CATALOG[ErrorAndBlockingEvent.WARNING] = None


def test_specific_event_replaces_general_parent():
    assert (
        select_specific_event(
            {ErrorAndBlockingEvent.AUTOMATIC_BLOCK, ErrorAndBlockingEvent.UNAUTHORIZED_CONNECTION}
        )
        == ErrorAndBlockingEvent.UNAUTHORIZED_CONNECTION
    )


def test_multiple_specific_events_require_explicit_resolution():
    with pytest.raises(ValueError, match="unambiguous"):
        select_specific_event(
            {
                ErrorAndBlockingEvent.UNAUTHORIZED_AGENT,
                ErrorAndBlockingEvent.UNAUTHORIZED_CONNECTION,
            }
        )
