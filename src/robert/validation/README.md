# Validation Core — Stage 4

| Module | Responsibility |
|---|---|
| `inputs.py` | Internal target adapter, closed contract expectation and declarative rule definitions |
| `findings.py` | Internal checks/issues mapped to the existing ValidationResult contract |
| `contract_validator.py` | Strict JSON validation through the existing 29-contract registry |
| `structure_validator.py` | Registered structure/types and required-field presence |
| `rule_validator.py` | Deterministic, non-executable data rules |
| `context_validator.py` | Existing Stage 3 permission/scope/security checks with trusted context |
| `handler.py` | Request handling, aggregation and mandatory AuditEvent persistence |

The public library method is `ValidationHandler.validate(ValidationRequest, ValidationTarget, ...)`.
It returns the existing canonical `ValidationResult`. No endpoint, new wire contract, automatic
reviewer routing, model call, tool call, memory write or execution is added.

## Supported request vocabulary

- `reviewer_roles`: exactly `["RULE_SYSTEM"]`.
- Initial types: RULE, CANONICAL, STRUCTURE, COMPLETENESS, CONSISTENCY, SECURITY, SCOPE, PERMISSION.
- `expected_contract`: `{"name": "TASK", "version": "0.1"}` (choose a registered ContractName).
  No inline schemas, remote references, dynamic classes or unknown options are accepted.
- `criteria`, `constraints`, `canonical_requirements`, `security_requirements`: objects with
  `criterion_id`, `validation_type`, `method`, `path` (array of data keys), optional `expected`,
  `other_path` and strict boolean `required` (default true).
- Methods: EXISTS, NON_EMPTY, EQUALS, NOT_EQUALS, ONE_OF, TYPE, FIELD_EQUALS.
  TYPE accepts string/integer/number/boolean/object/array/null. EQUALS uses JSON-value/type equality.
  Paths traverse dictionaries and nonnegative list indices, never attributes or executable code.
- `blocking_policy`: empty or `{"fail_closed": true}` only.
- Evidence/source requirements: supplied reference IDs as strings. Presence is checked;
  authenticity, freshness, truth and claim support are **not** independently verified.

Example criterion:

```json
{"criterion_id":"objective_present","validation_type":"RULE","method":"NON_EMPTY","path":["objective"],"required":true}
```

CANONICAL requires a registered expectation. STRUCTURE and COMPLETENESS use that expectation or
explicit criteria. RULE and CONSISTENCY require explicit criteria. Empty requirements do not cause
a vacuous PASS. Constraints and safety criteria cannot be made optional. Unknown vocabulary,
unsupported types/reviewers or missing required evidence produce blocking INCONCLUSIVE results.

## Trust and output boundary

Permission/scope checks require fresh `GovernanceRequest` and `PermissionGrant` inputs from a trusted
adapter, bound to the validation task, requester and target reference. Security requires a trusted
`SecurityContext`. Serialized `permission_context`, `scope_context` and `risk_context` claims in the
canonical request are not accepted as authority; nonempty values are currently unsupported and
produce INCONCLUSIVE. Caller data cannot authenticate a human or expand permission.

Required failures produce FAIL, required unavailable checks INCONCLUSIVE, optional failures
PASS_WITH_WARNINGS, otherwise PASS. FAIL and INCONCLUSIVE set `blocking=true`. Conceptual BLOCKED is
represented this way because the approved technical enum has no BLOCKED value. Confidence is null:
there is no calibrated confidence model. Checks, warnings and conflicts are carried in `checks` and
`issues`; no new top-level fields are invented.

PASS is not truth, approval, authority or execution. Validation does not decide which future operations
may skip checks. A future trusted caller must select the necessary types and criteria. All outcomes
must be audited before return; AuditWriteError propagates if persistence fails. Raw targets, rule
values and validation-library error inputs are not copied into audit logs.

Tests: `uv run pytest tests/validation -W error`.
