"""Canonical Error and Block construction mapped to the approved event catalog."""

from collections.abc import Callable
from datetime import UTC, datetime
from uuid import uuid4

from robert.audit.catalog import ERROR_AND_BLOCKING_EVENT_CATALOG, ErrorAndBlockingEvent
from robert.contracts.base import Identifier, JsonObject, NonEmptyString
from robert.contracts.errors import Block, Error


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _identifier(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


class ErrorAndBlockBuilder:
    """Map approved taxonomy entries to canonical outcomes."""

    def __init__(
        self,
        *,
        clock: Callable[[], datetime] = _utc_now,
        identifier_factory: Callable[[str], str] = _identifier,
    ) -> None:
        self._clock = clock
        self._identifier_factory = identifier_factory

    def build_error(
        self,
        *,
        task_id: Identifier,
        event: ErrorAndBlockingEvent,
        source_component: NonEmptyString,
        message: NonEmptyString,
        recoverable: bool,
        retry_allowed: bool = False,
        fallback_allowed: bool = False,
        details: JsonObject | None = None,
        related_ref: Identifier | None = None,
    ) -> Error:
        definition = ERROR_AND_BLOCKING_EVENT_CATALOG[event]
        return Error(
            contract_version="0.1",
            error_id=self._identifier_factory("error"),
            task_id=task_id,
            source_component=source_component,
            error_type=event.name,
            code=definition.code,
            message=message,
            severity=definition.severity,
            recoverable=recoverable,
            retry_allowed=retry_allowed,
            fallback_allowed=fallback_allowed,
            details=details or {},
            related_ref=related_ref,
            timestamp=self._clock(),
        )

    def build_block(
        self,
        *,
        task_id: Identifier,
        event: ErrorAndBlockingEvent,
        source_component: NonEmptyString,
        reason: NonEmptyString,
        required_resolution: NonEmptyString,
        user_action_required: bool,
        approval_required: bool,
        related_refs: list[Identifier] | None = None,
    ) -> Block:
        definition = ERROR_AND_BLOCKING_EVENT_CATALOG[event]
        if not definition.blocks_action:
            raise ValueError(f"{event.name} does not define a blocking outcome")
        return Block(
            contract_version="0.1",
            block_id=self._identifier_factory("block"),
            task_id=task_id,
            block_type=event.name,
            source_component=source_component,
            reason=reason,
            severity=definition.severity,
            required_resolution=required_resolution,
            user_action_required=user_action_required,
            approval_required=approval_required,
            related_refs=related_refs or [],
            created_at=self._clock(),
            status="ACTIVE",
        )
