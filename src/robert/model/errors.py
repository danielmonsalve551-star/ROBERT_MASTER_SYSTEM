"""Normalized Stage 6 provider errors without raw secret-bearing payloads."""

from enum import StrEnum

from pydantic import Field

from robert.contracts.base import JsonObject, NonEmptyString
from robert.model.inputs import ModelInput


class ModelErrorType(StrEnum):
    TIMEOUT = "TIMEOUT"
    RATE_LIMIT = "RATE_LIMIT"
    AUTH_FAILURE = "AUTH_FAILURE"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    INVALID_RESPONSE = "INVALID_RESPONSE"
    CONTEXT_LIMIT = "CONTEXT_LIMIT"
    CONTENT_REJECTION = "CONTENT_REJECTION"
    TOOL_FAILURE = "TOOL_FAILURE"
    UNKNOWN_PROVIDER_ERROR = "UNKNOWN_PROVIDER_ERROR"
    NO_ELIGIBLE_MODEL = "NO_ELIGIBLE_MODEL"
    REQUEST_REJECTED = "REQUEST_REJECTED"


class NormalizedModelError(ModelInput):
    error_type: ModelErrorType
    provider_error: NonEmptyString
    retryable: bool = Field(strict=True)
    fallback_allowed: bool = Field(strict=True)
    details: JsonObject = {}


class ModelProviderError(RuntimeError):
    """Safe adapter-to-interface failure; never carries a raw provider response."""

    def __init__(
        self,
        error_type: ModelErrorType,
        provider_error: str,
        *,
        retryable: bool = False,
        fallback_allowed: bool = False,
        details: JsonObject | None = None,
    ) -> None:
        super().__init__(provider_error)
        self.normalized = NormalizedModelError(
            error_type=error_type,
            provider_error=provider_error,
            retryable=retryable,
            fallback_allowed=fallback_allowed,
            details=details or {},
        )


class ModelRoutingError(RuntimeError):
    """No registered model satisfies all mandatory request constraints."""
