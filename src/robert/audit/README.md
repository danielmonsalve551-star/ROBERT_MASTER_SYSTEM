# Error and audit foundation

This package implements the Stage 2 traceability boundary without creating execution authority.

## Organization

| Module | Single responsibility |
|---|---|
| `catalog.py` | Approved 20-event error and blocking taxonomy |
| `outcome_builder.py` | Construction of canonical `Error` and `Block` outcomes |
| `event_builder.py` | Construction of canonical `AuditEvent` values |
| `redaction.py` | Recursive removal of secrets before persistence |
| `storage.py` | Append-only UTF-8 JSON Lines persistence |
| `writer.py` | Validation, sanitization and safe audit persistence |

## Runtime boundary

```text
AUDIT WRITER = RECORDING COMPONENT
AUDIT WRITER != AUTHORITY
AUDIT WRITER != ROUTER
AUDIT WRITER != EXECUTOR
```

Callers must provide an explicit `.jsonl` path. The recommended local path is
`var/audit/events.jsonl`; runtime logs are operational data and must not be committed.
