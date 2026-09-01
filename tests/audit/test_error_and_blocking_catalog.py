import pytest

from robert.audit.catalog import ERROR_AND_BLOCKING_EVENT_CATALOG, ErrorAndBlockingEvent
from robert.audit.outcome_builder import ErrorAndBlockBuilder


def test_catalog_contains_all_twenty_approved_events() -> None:
    assert set(ERROR_AND_BLOCKING_EVENT_CATALOG) == set(ErrorAndBlockingEvent)
    assert len(ERROR_AND_BLOCKING_EVENT_CATALOG) == 20


def test_specific_automatic_blocks_reference_general_parent() -> None:
    for event_number in range(15, 21):
        event = ErrorAndBlockingEvent(event_number)
        assert (
            ERROR_AND_BLOCKING_EVENT_CATALOG[event].parent_event
            is ErrorAndBlockingEvent.AUTOMATIC_BLOCK
        )


def test_catalog_uses_stable_namespaced_codes() -> None:
    assert (
        ERROR_AND_BLOCKING_EVENT_CATALOG[ErrorAndBlockingEvent.UNAUTHORIZED_CONNECTION].code
        == "ROBERT-EVENT-16"
    )


def test_control_action_remains_outside_risk_scale() -> None:
    definition = ERROR_AND_BLOCKING_EVENT_CATALOG[ErrorAndBlockingEvent.MANDATORY_PAUSE]

    assert definition.default_risk is None
    assert definition.severity == "CONTROL_ACTION"


def test_error_builder_maps_approved_taxonomy(outcome_builder: ErrorAndBlockBuilder) -> None:
    error = outcome_builder.build_error(
        task_id="task_1",
        event=ErrorAndBlockingEvent.MISSING_INFORMATION,
        source_component="API",
        message="Required field is absent",
        recoverable=True,
    )

    assert error.error_type == "MISSING_INFORMATION"
    assert error.code == "ROBERT-EVENT-09"
    assert error.severity == "MEDIUM"


def test_block_builder_uses_specific_event(outcome_builder: ErrorAndBlockBuilder) -> None:
    block = outcome_builder.build_block(
        task_id="task_1",
        event=ErrorAndBlockingEvent.UNAUTHORIZED_CONNECTION,
        source_component="APPROVAL_GATE",
        reason="Connection has no authorization",
        required_resolution="Obtain explicit authorization",
        user_action_required=True,
        approval_required=True,
    )

    assert block.block_type == "UNAUTHORIZED_CONNECTION"
    assert block.severity == "CRITICAL"
    assert block.status == "ACTIVE"


def test_non_blocking_event_cannot_create_block(outcome_builder: ErrorAndBlockBuilder) -> None:
    with pytest.raises(ValueError, match="does not define a blocking outcome"):
        outcome_builder.build_block(
            task_id="task_1",
            event=ErrorAndBlockingEvent.WARNING,
            source_component="RISK_BADGE",
            reason="Review recommended",
            required_resolution="Review",
            user_action_required=False,
            approval_required=False,
        )
