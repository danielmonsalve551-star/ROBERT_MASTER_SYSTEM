"""Error and blocking contracts subordinate to the approved taxonomy."""

from robert.contracts.base import (
    CanonicalContract,
    Identifier,
    JsonObject,
    NonEmptyString,
    UtcDateTime,
)


class Error(CanonicalContract):
    error_id: Identifier
    task_id: Identifier
    source_component: NonEmptyString
    error_type: NonEmptyString
    code: NonEmptyString
    message: NonEmptyString
    severity: NonEmptyString
    recoverable: bool
    retry_allowed: bool
    fallback_allowed: bool
    details: JsonObject
    related_ref: Identifier | None
    timestamp: UtcDateTime


class Block(CanonicalContract):
    block_id: Identifier
    task_id: Identifier
    block_type: NonEmptyString
    source_component: NonEmptyString
    reason: NonEmptyString
    severity: NonEmptyString
    required_resolution: NonEmptyString
    user_action_required: bool
    approval_required: bool
    related_refs: list[Identifier]
    created_at: UtcDateTime
    status: NonEmptyString
