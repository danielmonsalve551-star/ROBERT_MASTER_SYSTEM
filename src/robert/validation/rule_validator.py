"""Closed declarative rule vocabulary; no eval, callbacks, imports or external access."""

import json
import math

from robert.contracts.base import JsonObject
from robert.validation.findings import CheckFinding
from robert.validation.inputs import RuleMethod, ValidationCriterion

_MISSING = object()


def _lookup(payload, path):
    value = payload
    for key in path:
        if isinstance(value, dict):
            value = value.get(key, _MISSING)
        elif isinstance(value, list) and key.isascii() and key.isdecimal() and len(key) <= 9:
            index = int(key)
            value = value[index] if index < len(value) else _MISSING
        else:
            return _MISSING
        if value is _MISSING:
            return value
    return value


def _equal(left, right):
    # JSON serialization distinguishes booleans, integers and strings, unlike Python ==.
    return json.dumps(left, sort_keys=True, allow_nan=False) == json.dumps(
        right, sort_keys=True, allow_nan=False
    )


def _has_type(value, expected):
    return {
        "string": isinstance(value, str),
        "integer": type(value) is int,
        "number": type(value) in (int, float)
        and (not isinstance(value, float) or math.isfinite(value)),
        "boolean": type(value) is bool,
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "null": value is None,
    }[expected]


def validate_rule(
    payload: JsonObject, criterion: ValidationCriterion, *, force_required=False
) -> CheckFinding:
    value = _lookup(payload, criterion.path)
    passed = False
    if value is not _MISSING:
        match criterion.method:
            case RuleMethod.EXISTS:
                passed = True
            case RuleMethod.NON_EMPTY:
                passed = value is not None and (
                    bool(value.strip())
                    if isinstance(value, str)
                    else (bool(value) if isinstance(value, (list, dict)) else True)
                )
            case RuleMethod.EQUALS:
                passed = _equal(value, criterion.expected)
            case RuleMethod.NOT_EQUALS:
                passed = not _equal(value, criterion.expected)
            case RuleMethod.ONE_OF:
                passed = any(_equal(value, item) for item in criterion.expected)
            case RuleMethod.TYPE:
                passed = _has_type(value, criterion.expected)
            case RuleMethod.FIELD_EQUALS:
                other = _lookup(payload, criterion.other_path)
                passed = other is not _MISSING and _equal(value, other)
    return CheckFinding(
        f"criterion:{criterion.criterion_id}",
        criterion.validation_type.value,
        "PASS" if passed else "FAIL",
        "Declared criterion satisfied" if passed else "Declared criterion not satisfied",
        required=force_required or criterion.required,
        conflict=criterion.method == RuleMethod.FIELD_EQUALS and not passed,
    )
