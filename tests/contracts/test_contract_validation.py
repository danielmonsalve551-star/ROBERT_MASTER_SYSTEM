from copy import deepcopy
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from robert.contracts.audit import EvidenceRef
from robert.contracts.governance import RiskAssessment
from robert.contracts.model import ModelRequest
from robert.contracts.registry import CONTRACT_REGISTRY, ContractRegistration
from tests.contracts.schema_samples import build_valid_payload


@pytest.mark.parametrize(
    "registration",
    CONTRACT_REGISTRY,
    ids=lambda registration: registration.name.value,
)
def test_every_contract_parses_validates_and_serializes(
    registration: ContractRegistration,
) -> None:
    schema = registration.model.model_json_schema(mode="validation")
    payload = build_valid_payload(schema)

    contract = registration.model.model_validate(payload)
    serialized = contract.model_dump_json()
    restored = registration.model.model_validate_json(serialized)

    assert restored == contract


@pytest.mark.parametrize(
    "registration",
    CONTRACT_REGISTRY,
    ids=lambda registration: registration.name.value,
)
def test_every_contract_rejects_missing_version(registration: ContractRegistration) -> None:
    payload = build_valid_payload(registration.model.model_json_schema(mode="validation"))
    payload.pop("contract_version")

    with pytest.raises(ValidationError):
        registration.model.model_validate(payload)


@pytest.mark.parametrize(
    "registration",
    CONTRACT_REGISTRY,
    ids=lambda registration: registration.name.value,
)
def test_every_contract_rejects_unknown_fields(registration: ContractRegistration) -> None:
    payload = build_valid_payload(registration.model.model_json_schema(mode="validation"))
    payload["unknown_field"] = "not allowed"

    with pytest.raises(ValidationError):
        registration.model.model_validate(payload)


def test_contracts_reject_unsupported_version() -> None:
    payload = build_valid_payload(ModelRequest.model_json_schema(mode="validation"))
    payload["contract_version"] = "9.9"

    with pytest.raises(ValidationError):
        ModelRequest.model_validate(payload)


def test_contracts_are_immutable() -> None:
    payload = build_valid_payload(ModelRequest.model_json_schema(mode="validation"))
    contract = ModelRequest.model_validate(payload)

    with pytest.raises(ValidationError):
        contract.objective = "changed"


def test_timestamps_require_timezone_and_normalize_to_utc() -> None:
    payload = build_valid_payload(EvidenceRef.model_json_schema(mode="validation"))
    payload["created_at"] = "2026-09-01T02:00:00+02:00"
    contract = EvidenceRef.model_validate(payload)

    assert contract.created_at == datetime(2026, 9, 1, tzinfo=UTC)

    invalid_payload = deepcopy(payload)
    invalid_payload["created_at"] = "2026-09-01T00:00:00"
    with pytest.raises(ValidationError):
        EvidenceRef.model_validate(invalid_payload)


def test_risk_level_five_is_rejected() -> None:
    payload = build_valid_payload(RiskAssessment.model_json_schema(mode="validation"))
    payload["risk_level"] = 5

    with pytest.raises(ValidationError):
        RiskAssessment.model_validate(payload)
