"""Append-only JSON Lines storage for canonical AuditEvent records."""

import json
import os
import stat
from collections.abc import Mapping
from pathlib import Path
from threading import Lock, RLock
from typing import Protocol

from robert.audit.redaction import redact_sensitive_values
from robert.contracts.audit import AuditEvent

_LOCKS_GUARD = Lock()
_PATH_LOCKS: dict[Path, RLock] = {}


class AuditStore(Protocol):
    """Persistence boundary required by AuditWriter."""

    def append(self, payload: Mapping[str, object]) -> None: ...


class JsonLinesAuditStore:
    """Validated single-process store; instances share a per-path lock."""

    def __init__(self, file_path: Path) -> None:
        if file_path.suffix != ".jsonl":
            raise ValueError("audit store path must use the .jsonl extension")
        if file_path.is_symlink():
            raise ValueError("audit store must not be a symbolic link")
        self.file_path = file_path.absolute()
        with _LOCKS_GUARD:
            self._write_lock = _PATH_LOCKS.setdefault(file_path.resolve(), RLock())

    def append(self, payload: Mapping[str, object]) -> None:
        event = AuditEvent.model_validate(dict(payload))
        event = AuditEvent.model_validate(redact_sensitive_values(event.model_dump(mode="json")))
        encoded = (
            json.dumps(
                event.model_dump(mode="json"),
                ensure_ascii=False,
                allow_nan=False,
                separators=(",", ":"),
            ).encode("utf-8")
            + b"\n"
        )
        with self._write_lock:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            if self.file_path.is_symlink():
                raise ValueError("audit store must not be a symbolic link")
            flags = (
                os.O_RDWR
                | os.O_APPEND
                | os.O_CREAT
                | getattr(os, "O_NOFOLLOW", 0)
                | getattr(os, "O_NONBLOCK", 0)
            )
            descriptor = os.open(self.file_path, flags, 0o600)
            with os.fdopen(descriptor, "a+b") as stream:
                if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                    raise ValueError("audit store must be a regular file")
                stream.seek(0)
                existing = self._decode(stream.read())
                if any(item.event_id == event.event_id for item in existing):
                    raise ValueError("duplicate audit event_id")
                stream.write(encoded)
                stream.flush()
                os.fsync(stream.fileno())

    def read_events(self) -> tuple[AuditEvent, ...]:
        with self._write_lock:
            if self.file_path.is_symlink():
                raise ValueError("audit store must not be a symbolic link")
            if not self.file_path.exists():
                return ()
            return self._decode(self.file_path.read_bytes())

    @staticmethod
    def _decode(data: bytes) -> tuple[AuditEvent, ...]:
        if data and not data.endswith(b"\n"):
            raise ValueError("incomplete audit history; explicit recovery required")
        events = tuple(AuditEvent.model_validate_json(line) for line in data.splitlines())
        if len({event.event_id for event in events}) != len(events):
            raise ValueError("duplicate identities in audit history")
        return events
