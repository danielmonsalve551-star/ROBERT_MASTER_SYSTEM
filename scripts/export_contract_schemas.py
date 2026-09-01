"""Export canonical Pydantic contracts to organized JSON Schema files."""

import json
from pathlib import Path

from robert.contracts.registry import CONTRACT_REGISTRY

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def export_contract_schemas() -> int:
    """Write one deterministic schema per registered canonical contract."""

    for registration in CONTRACT_REGISTRY:
        output_path = PROJECT_ROOT / registration.schema_path
        output_path.parent.mkdir(parents=True, exist_ok=True)

        schema = registration.model.model_json_schema(mode="validation")
        schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
        schema["$id"] = registration.schema_path
        schema["x-robert-contract-name"] = registration.name.value
        schema["x-robert-contract-owner"] = registration.owner
        output_path.write_text(
            json.dumps(schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    return len(CONTRACT_REGISTRY)


if __name__ == "__main__":
    exported_count = export_contract_schemas()
    print(f"Exported {exported_count} canonical contract schemas.")
