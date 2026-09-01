"""Append-only JSON Lines storage for canonical AuditEvent records."""

import json
import os
from collections.abc import Mapping
from pathlib import Path
from threading import Lock
from typing import Protocol

from robert.contracts.audit import AuditEvent


class AuditStore(Protocol):
    """Persistence boundary required by AuditWriter."""

    def append(self, payload: Mapping[str, object]) -> None: ...


class JsonLinesAuditStore:
    """Persist one sanitized canonical AuditEvent per UTF-8 JSON line."""

    def __init__(self, file_path: Path) -> None:
        if file_path.suffix != ".jsonl":
            raise ValueError("audit store path must use the .jsonl extension")
        self.file_path = file_path
        self._write_lock = Lock()

    def append(self, payload: Mapping[str, object]) -> None:
        encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self._write_lock, self.file_path.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(encoded)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())

    def read_events(self) -> tuple[AuditEvent, ...]:
        if not self.file_path.exists():
            return ()
        with self.file_path.open(encoding="utf-8") as stream:
            return tuple(AuditEvent.model_validate_json(line) for line in stream if line.strip())
