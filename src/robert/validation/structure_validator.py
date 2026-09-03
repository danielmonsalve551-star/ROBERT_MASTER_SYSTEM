"""Declared root structure and required-field presence, separate from semantics."""

from robert.contracts.base import JsonObject
from robert.validation.contract_validator import contract_model, validate_contract
from robert.validation.findings import CheckFinding
from robert.validation.inputs import ContractExpectation


def validate_structure(payload: JsonObject, expected: ContractExpectation) -> CheckFinding:
    valid = validate_contract(payload, expected).status == "PASS"
    return CheckFinding(
        "structure:fields",
        "STRUCTURE",
        "PASS" if valid else "FAIL",
        "Registered field structure and types match"
        if valid
        else "Registered structure/types do not match",
    )


def validate_completeness(payload: JsonObject, expected: ContractExpectation) -> CheckFinding:
    required = {
        name for name, field in contract_model(expected).model_fields.items() if field.is_required()
    }
    missing = required - set(payload)
    return CheckFinding(
        "completeness:required",
        "COMPLETENESS",
        "FAIL" if missing else "PASS",
        "Required root fields are missing" if missing else "Required root fields are present",
    )
