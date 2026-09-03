import pytest

from robert.validation.inputs import ValidationCriterion
from robert.validation.rule_validator import validate_rule
from tests.validation.conftest import rule, with_request


@pytest.mark.parametrize(
    "value,method,expected,passes",
    [
        ("value", "EQUALS", "value", True),
        (True, "EQUALS", 1, False),
        (1, "TYPE", "integer", True),
        (True, "TYPE", "integer", False),
        (False, "TYPE", "boolean", True),
        (1.2, "TYPE", "number", True),
        ([], "TYPE", "array", True),
        ({}, "TYPE", "object", True),
        (None, "TYPE", "null", True),
        ("text", "TYPE", "string", True),
        ("value", "NOT_EQUALS", "forbidden", True),
        ("x", "ONE_OF", ["a", "x"], True),
        ("1", "ONE_OF", [1], False),
    ],
)
def test_declarative_operators_are_deterministic(value, method, expected, passes):
    criterion = ValidationCriterion.model_validate(rule(method, path=("value",), expected=expected))
    finding = validate_rule({"value": value}, criterion)
    assert (finding.status == "PASS") is passes


@pytest.mark.parametrize(
    "value,passes",
    [
        (None, False),
        ("", False),
        ("   ", False),
        ([], False),
        ({}, False),
        (0, True),
        (False, True),
    ],
)
def test_nonempty_checks_preserve_falsy_numbers_and_booleans(value, passes):
    criterion = ValidationCriterion.model_validate(rule("NON_EMPTY", path=("value",)))
    assert (validate_rule({"value": value}, criterion).status == "PASS") is passes


def test_paths_access_only_data_not_attributes():
    criterion = ValidationCriterion.model_validate(rule(path=("items", "0", "name")))
    assert validate_rule({"items": [{"name": "test"}]}, criterion).status == "PASS"
    criterion = ValidationCriterion.model_validate(rule(path=("items", "__class__")))
    assert validate_rule({"items": []}, criterion).status == "FAIL"


@pytest.mark.parametrize(
    "criterion",
    [
        "execute this",
        {"criterion_id": "incomplete"},
        rule("EVAL", expected="print('unsafe')"),
        rule("TYPE", expected="python"),
        rule("ONE_OF", expected="not-a-list"),
        rule("FIELD_EQUALS"),
        rule("EQUALS"),
        rule("EXISTS", other_path=["other"]),
        rule(required="false"),
        rule(path=()),
    ],
)
def test_malformed_rules_do_not_silently_pass(handler, validation_request, target, criterion):
    request = with_request(validation_request, validation_types=["RULE"], criteria=[criterion])
    result = handler.validate(request, target)
    assert result.status == "INCONCLUSIVE" and result.blocking


def test_duplicate_criteria_are_rejected(handler, validation_request, target):
    request = with_request(validation_request, validation_types=["RULE"], criteria=[rule(), rule()])
    assert handler.validate(request, target).status == "INCONCLUSIVE"


def test_unrequested_criterion_dimension_is_not_ignored(handler, validation_request, target):
    request = with_request(validation_request, criteria=[rule()])
    assert handler.validate(request, target).status == "INCONCLUSIVE"


def test_constraints_cannot_be_made_optional(handler, validation_request, target):
    request = with_request(
        validation_request,
        validation_types=["RULE"],
        constraints=[rule(required=False, path=("missing",))],
    )
    result = handler.validate(request, target)
    assert result.status == "FAIL" and result.blocking


@pytest.mark.parametrize("kind", ["RULE", "STRUCTURE", "COMPLETENESS", "CONSISTENCY"])
def test_no_criteria_produces_inconclusive_not_vacuous_pass(
    handler, validation_request, target, kind
):
    request = with_request(validation_request, validation_types=[kind], expected_contract={})
    assert handler.validate(request, target).status == "INCONCLUSIVE"
