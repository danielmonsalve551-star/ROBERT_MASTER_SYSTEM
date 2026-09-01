"""Minimum-necessary redaction before audit persistence."""

from collections.abc import Mapping, Sequence
from typing import Any

REDACTED_VALUE = "[REDACTED]"
OMITTED_VALUE = "[OMITTED: USE REFERENCE]"

_SENSITIVE_KEYS = frozenset(
    {
        "api_key",
        "authorization",
        "bearer",
        "credential",
        "password",
        "private_key",
        "secret",
        "session_token",
        "token",
    }
)

_FULL_PAYLOAD_KEYS = frozenset(
    {
        "full_document_content",
        "full_memory",
        "full_model_prompt",
        "full_tool_payload",
        "full_user_context",
    }
)


def redact_sensitive_values(value: Any) -> Any:
    """Return a recursively sanitized copy suitable for an audit record."""

    if isinstance(value, Mapping):
        return {str(key): _protected_value(str(key), item) for key, item in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [redact_sensitive_values(item) for item in value]
    return value


def _is_sensitive_key(key: str) -> bool:
    normalized = key.casefold().replace("-", "_").replace(" ", "_")
    sensitive_suffixes = ("_credential", "_key", "_password", "_secret", "_token")
    return normalized in _SENSITIVE_KEYS or normalized.endswith(sensitive_suffixes)


def _protected_value(key: str, value: Any) -> Any:
    normalized = key.casefold().replace("-", "_").replace(" ", "_")
    if _is_sensitive_key(key):
        return REDACTED_VALUE
    if normalized in _FULL_PAYLOAD_KEYS:
        return OMITTED_VALUE
    return redact_sensitive_values(value)
