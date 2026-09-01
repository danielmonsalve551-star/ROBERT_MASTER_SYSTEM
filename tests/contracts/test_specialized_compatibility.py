from robert.contracts.memory import MemoryRetrievalRequest
from robert.contracts.tool import ToolResult
from robert.contracts.validation import ValidationResult


def test_tool_result_preserves_specialized_confidence_field() -> None:
    assert "confidence_if_applicable" in ToolResult.model_fields


def test_memory_retrieval_request_preserves_specialized_fields() -> None:
    required_fields = {
        "requester",
        "scope",
        "freshness_requirement",
        "confidence_requirement",
        "sensitivity_constraints",
    }

    assert required_fields <= set(MemoryRetrievalRequest.model_fields)


def test_validation_result_preserves_reconciled_fields() -> None:
    required_fields = {
        "requester",
        "confidence",
        "limitations",
        "sources",
        "recommended_next_step",
    }

    assert required_fields <= set(ValidationResult.model_fields)
