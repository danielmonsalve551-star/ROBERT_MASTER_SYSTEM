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

The local store validates and sanitizes even direct append calls, rejects duplicate event IDs and
incomplete/corrupt history, and serializes same-process instances using a shared per-path lock.
Corrections must be additional events with new IDs. Failed writes require explicit recovery;
do not blindly retry an uncertain write. Multi-process writers, high volume, tamper-proof storage,
encryption and retention management are outside this initial store's guarantees.

Redaction covers known keys and token/private-key patterns, not arbitrary secrets. Callers must
still minimize payloads and use references. Frozen contract fields do not make nested collections
immutable; persistence and evaluation boundaries validate independent snapshots.
