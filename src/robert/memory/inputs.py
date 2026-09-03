"""Closed Stage 5 adapter vocabulary, not additional canonical contracts."""

import json
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from robert.contracts.base import Identifier, NonEmptyString, UtcDateTime


def snapshot[Model: BaseModel](model: type[Model], value: Model) -> Model:
    """Detach nested data, reject non-finite JSON, and validate against the expected model."""
    return model.model_validate_json(
        json.dumps(value.model_dump(mode="json"), allow_nan=False), strict=True
    )


def checked_now(value: datetime) -> datetime:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("clock must be timezone-aware")
    return value


class MemoryInput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, allow_inf_nan=False)


class MemoryAuthority(MemoryInput):
    """Supplied only by the trusted, manually controlled repository adapter."""

    readers: tuple[NonEmptyString, ...] = Field(min_length=1)
    confidence: float | None = Field(default=None, ge=0, le=1, strict=True)
    confidence_source: Literal["USER_EXPLICIT", "VALIDATOR_DERIVED", "UNKNOWN"] = "UNKNOWN"
    expires_at: UtcDateTime | None = None
    task_id: Identifier | None = None

    @model_validator(mode="after")
    def check_confidence_source(self):
        if self.confidence is not None and self.confidence_source == "UNKNOWN":
            raise ValueError("confidence requires an explicit provenance")
        if any(not reader.strip() or reader == "*" for reader in self.readers):
            raise ValueError("readers must be explicit")
        return self


class RecordValidation(MemoryInput):
    status: Literal["PASS", "UNVERIFIED", "CONFLICTED"]
    verified_at: UtcDateTime | None = None
    conflict_refs: tuple[Identifier, ...] = ()


class FreshnessRequirement(MemoryInput):
    max_age_seconds: int | None = Field(default=None, ge=0, strict=True)
    verified_after: UtcDateTime | None = None
