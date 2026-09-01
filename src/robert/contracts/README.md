# Canonical contracts package

This package is the single technical source of truth for Stage 1 contracts.

## Organization

| Module | Responsibility |
|---|---|
| `base.py` | Contract version, strict model policy, IDs, UTC timestamps and canonical enums |
| `envelope.py` | Shared transport envelope |
| `task.py` | Task and Request Context |
| `orchestration.py` | Orchestrator Request, Route and Orchestrator Result |
| `agent.py` | Agent Request and Agent Result |
| `skill.py` | Skill Invocation and Skill Result |
| `model.py` | Model Request and Model Response |
| `tool.py` | Tool Request and Tool Result |
| `memory.py` | Memory Candidate, Record and Retrieval |
| `validation.py` | Validation Request and Validation Result |
| `governance.py` | Permission, Scope, Risk and Approval |
| `errors.py` | Error and Block |
| `audit.py` | Audit Event and Evidence Reference |
| `registry.py` | Complete canonical registry and schema locations |

## Rules

1. A canonical contract is defined once.
2. Every contract inherits `CanonicalContract`.
3. Unknown fields are rejected.
4. Every payload must include `contract_version="0.1"`.
5. Contract instances are immutable.
6. Timestamps are timezone-aware and normalized to UTC.
7. Generated schemas are outputs; edit the Pydantic source instead.
8. Stage 1 contracts contain no routing, approval or execution engine.
