"""Minimum-necessary redaction before audit persistence."""

import re
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
    if isinstance(value, str):
        value = re.sub(
            r"-----BEGIN [^-]*PRIVATE KEY-----.*?-----END [^-]*PRIVATE KEY-----",
            REDACTED_VALUE,
            value,
            flags=re.DOTALL,
        )
        return re.sub(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]+", "Bearer [REDACTED]", value)
    return value


def _is_sensitive_key(key: str) -> bool:
    normalized = _normalize_key(key)
    sensitive_suffixes = ("_credential", "_key", "_password", "_secret", "_token")
    compact = normalized.replace("_", "")
    return (
        normalized in _SENSITIVE_KEYS
        or normalized.endswith(sensitive_suffixes)
        or compact in {"apikey", "privatekey", "accesstoken", "refreshtoken", "credentials"}
    )


def _protected_value(key: str, value: Any) -> Any:
    normalized = _normalize_key(key)
    if _is_sensitive_key(key):
        return REDACTED_VALUE
    if normalized in _FULL_PAYLOAD_KEYS:
        return OMITTED_VALUE
    return redact_sensitive_values(value)


def _normalize_key(key: str) -> str:
    return (
        re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", key).casefold().replace("-", "_").replace(" ", "_")
    )
