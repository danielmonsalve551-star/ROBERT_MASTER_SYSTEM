"""Safe persistence boundary for immutable canonical AuditEvent values."""

from robert.audit.redaction import redact_sensitive_values
from robert.audit.storage import AuditStore
from robert.contracts.audit import AuditEvent


class AuditWriteError(RuntimeError):
    """Raised when required audit persistence cannot be confirmed."""


class AuditWriter:
    """Validate, sanitize and persist events without deciding or authorizing actions."""

    def __init__(self, store: AuditStore) -> None:
        self._store = store

    def write(self, event: AuditEvent) -> AuditEvent:
        payload = event.model_dump(mode="json")
        sanitized_payload = redact_sensitive_values(payload)
        sanitized_event = AuditEvent.model_validate(sanitized_payload)
        try:
            self._store.append(sanitized_event.model_dump(mode="json"))
        except (OSError, TypeError, ValueError) as exc:
            raise AuditWriteError(
                f"required audit event {event.event_id} could not be persisted"
            ) from exc
        return sanitized_event
