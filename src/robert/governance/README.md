# Governance Core — Stage 3

| Module | Responsibility |
|---|---|
| `inputs.py` | Typed internal adapter inputs: request, human grant, scope, security observations |
| `policy.py` | Closed operation catalog, risk floors and execution restrictions |
| `checks.py` | Permission, scope, risk, security and approval checks |
| `engine.py` | Ordered evaluation, canonical Block construction and mandatory auditing |

`GovernanceOutcome` groups existing canonical contracts; it is not a new wire contract or an
execution capability. The canonical registry remains at 29 contracts.

## Trust boundary

This is an **internal library**, not a public authorization API. Grant, approval and security
objects must come from a trusted human-authorization adapter. A JSON field saying `USER` is not
authentication. No network adapter, identity provider, approval database, executor, permission
issuer or revocation service is implemented here.

The caller must supply current grant/revocation state on every evaluation. `consumed=True` rejects
one-shot grants already used; the engine does not mark grants consumed because it executes nothing.
No caller may reuse `ALLOWED` as authority to execute later. Approval windows are bounded, timestamps
are aware, resources match exactly and scoped sections use explicit subset comparison (no wildcards).

## Outcomes

Order: Permission → Scope → Risk → Security → Approval → Execution Authority.

The first failed check stops evaluation and yields a canonical Block plus persisted AuditEvent.
Missing security information fails closed. Approval conditions that cannot be evaluated are denied.
Risk inputs can raise, never lower, policy floors. Risk 4 is blocked. External actions, code execution,
connections, automation, agents and phase changes remain blocked with `EXECUTION_AUTHORITY=NONE`.

`ALLOWED` means the supplied documentary request passed this evaluation only. No action is performed,
including document changes. Failed mandatory audit persistence raises `AuditWriteError`; no allowed
result is returned. Tests: `uv run pytest tests/governance -W error`.
