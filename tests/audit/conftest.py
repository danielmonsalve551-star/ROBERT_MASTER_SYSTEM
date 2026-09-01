from datetime import UTC, datetime

import pytest

from robert.audit.event_builder import AuditEventBuilder
from robert.audit.outcome_builder import ErrorAndBlockBuilder


@pytest.fixture
def fixed_time() -> datetime:
    return datetime(2026, 9, 1, 12, 0, tzinfo=UTC)


@pytest.fixture
def event_builder(fixed_time: datetime) -> AuditEventBuilder:
    return AuditEventBuilder(clock=lambda: fixed_time, event_id_factory=lambda: "audit_evt_test")


@pytest.fixture
def outcome_builder(fixed_time: datetime) -> ErrorAndBlockBuilder:
    return ErrorAndBlockBuilder(
        clock=lambda: fixed_time,
        identifier_factory=lambda prefix: f"{prefix}_test",
    )
