"""Construction of canonical AuditEvent values without granting decision authority."""

from collections.abc import Callable
from datetime import UTC, datetime
from uuid import uuid4

from robert.contracts.audit import AuditEvent
from robert.contracts.base import Identifier, JsonObject, NonEmptyString


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _event_id() -> str:
    return f"audit_evt_{uuid4().hex}"


class AuditEventBuilder:
    """Build valid audit contracts; it does not authorize or execute actions."""

    def __init__(
        self,
        *,
        clock: Callable[[], datetime] = _utc_now,
        event_id_factory: Callable[[], str] = _event_id,
    ) -> None:
        self._clock = clock
        self._event_id_factory = event_id_factory

    def build(
        self,
        *,
        task_id: Identifier,
        event_type: NonEmptyString,
        actor: NonEmptyString,
        component: NonEmptyString,
        action: NonEmptyString,
        target: NonEmptyString,
        result: JsonObject,
        input_refs: list[Identifier] | None = None,
        output_refs: list[Identifier] | None = None,
        permission_state: JsonObject | None = None,
        scope_state: JsonObject | None = None,
        risk_state: JsonObject | None = None,
        approval_state: JsonObject | None = None,
        validation_state: JsonObject | None = None,
        error_ref: Identifier | None = None,
        metadata: JsonObject | None = None,
    ) -> AuditEvent:
        return AuditEvent(
            contract_version="0.1",
            event_id=self._event_id_factory(),
            task_id=task_id,
            timestamp=self._clock(),
            event_type=event_type,
            actor=actor,
            component=component,
            action=action,
            target=target,
            input_refs=input_refs or [],
            output_refs=output_refs or [],
            permission_state=permission_state or {},
            scope_state=scope_state or {},
            risk_state=risk_state or {},
            approval_state=approval_state or {},
            validation_state=validation_state or {},
            result=result,
            error_ref=error_ref,
            metadata=metadata or {},
        )
