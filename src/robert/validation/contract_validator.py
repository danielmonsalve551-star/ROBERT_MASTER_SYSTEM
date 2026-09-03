"""Strict JSON validation against the existing closed canonical registry."""

import json
from types import MappingProxyType

from pydantic import ValidationError

from robert.contracts.base import JsonObject
from robert.contracts.registry import CONTRACT_REGISTRY, ContractType
from robert.validation.findings import CheckFinding
from robert.validation.inputs import ContractExpectation

_CONTRACTS = MappingProxyType({entry.name: entry.model for entry in CONTRACT_REGISTRY})


def contract_model(expected: ContractExpectation) -> ContractType:
    return _CONTRACTS[expected.name]


def validate_contract(payload: JsonObject, expected: ContractExpectation) -> CheckFinding:
    try:
        contract_model(expected).model_validate_json(
            json.dumps(payload, ensure_ascii=False, allow_nan=False), strict=True
        )
    except (ValidationError, ValueError, TypeError):
        # Never copy Pydantic's raw input/error context (which can contain secrets).
        return CheckFinding(
            "canonical:contract",
            "CANONICAL",
            "FAIL",
            "Payload does not satisfy the registered contract; inspect it locally",
        )
    return CheckFinding(
        "canonical:contract",
        "CANONICAL",
        "PASS",
        "Strict registered-contract JSON validation passed",
    )
