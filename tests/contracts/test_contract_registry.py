import json
from pathlib import Path

from robert.contracts.base import ContractName
from robert.contracts.registry import CONTRACT_REGISTRY, CONTRACTS_BY_NAME

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_registry_contains_every_canonical_contract_once() -> None:
    names = [registration.name for registration in CONTRACT_REGISTRY]
    schema_paths = [registration.schema_path for registration in CONTRACT_REGISTRY]

    assert len(CONTRACT_REGISTRY) == 29
    assert len(names) == len(set(names))
    assert len(schema_paths) == len(set(schema_paths))
    assert set(names) == set(ContractName)
    assert set(CONTRACTS_BY_NAME) == set(ContractName)


def test_generated_schemas_match_registered_models() -> None:
    for registration in CONTRACT_REGISTRY:
        schema_path = PROJECT_ROOT / registration.schema_path
        committed_schema = json.loads(schema_path.read_text(encoding="utf-8"))
        generated_schema = registration.model.model_json_schema(mode="validation")

        assert committed_schema["x-robert-contract-name"] == registration.name.value
        assert committed_schema["x-robert-contract-owner"] == registration.owner
        assert committed_schema["$id"] == registration.schema_path
        assert committed_schema["properties"] == generated_schema["properties"]
        assert committed_schema["required"] == generated_schema["required"]
        generated_schema.update(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": registration.schema_path,
                "x-robert-contract-name": registration.name.value,
                "x-robert-contract-owner": registration.owner,
            }
        )
        assert committed_schema == generated_schema
