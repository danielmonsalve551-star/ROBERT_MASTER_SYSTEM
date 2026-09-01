"""Deterministic valid payload generation from Pydantic JSON Schemas."""

from typing import Any


def build_valid_payload(schema: dict[str, Any]) -> dict[str, Any]:
    """Build the smallest deterministic payload accepted by a contract schema."""

    value = _value_for_schema(schema, schema)
    if not isinstance(value, dict):
        raise TypeError("contract root schema must produce an object")
    return value


def _value_for_schema(node: dict[str, Any], root: dict[str, Any]) -> Any:
    if "$ref" in node:
        return _value_for_schema(_resolve_reference(node["$ref"], root), root)

    if "const" in node:
        return node["const"]

    if "enum" in node:
        return node["enum"][0]

    for union_key in ("anyOf", "oneOf"):
        if union_key in node:
            choices = node[union_key]
            non_null_choices = [choice for choice in choices if choice.get("type") != "null"]
            return _value_for_schema((non_null_choices or choices)[0], root)

    node_type = node.get("type")
    if isinstance(node_type, list):
        node_type = next(item for item in node_type if item != "null")

    if node.get("format") == "date-time":
        return "2026-09-01T00:00:00Z"
    if node_type == "string":
        return "sample"
    if node_type == "integer":
        return node.get("minimum", 0)
    if node_type == "number":
        return node.get("minimum", 0.0)
    if node_type == "boolean":
        return False
    if node_type == "array":
        return []
    if node_type == "object" or "properties" in node:
        properties = node.get("properties", {})
        return {
            field_name: _value_for_schema(properties[field_name], root)
            for field_name in node.get("required", [])
        }

    return None


def _resolve_reference(reference: str, root: dict[str, Any]) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ValueError(f"unsupported external schema reference: {reference}")

    resolved: Any = root
    for component in reference[2:].split("/"):
        key = component.replace("~1", "/").replace("~0", "~")
        resolved = resolved[key]

    if not isinstance(resolved, dict):
        raise TypeError(f"schema reference does not resolve to an object: {reference}")
    return resolved
