# Controlled Memory Interfaces — Stage 5

| Module | Responsibility |
|---|---|
| `inputs.py` | Strict snapshots, trusted metadata and freshness vocabulary |
| `candidates.py` | Audited candidate creation and Stage 4 validation; no promotion |
| `repository.py` | Read-only port and manually seeded in-process adapter |
| `retrieval.py` | Permission gate, record eligibility, lexical ranking and audited result |

All wire data uses the existing MemoryCandidate, MemoryRecord, MemoryRetrievalRequest and
MemoryRetrievalResult contracts. No new canonical models, schemas, database or dependencies are added.

## Entry points

- `MemoryCandidateService.create(CandidateDraft, requester=...)` returns an unapproved proposal.
- `MemoryCandidateService.validate(candidate, requester=..., governance=..., grant=..., security=...)`
  returns ValidationResult. Governance uses PREPARE_DRAFT bound to the candidate ID. No supplied
  governance produces blocking INCONCLUSIVE; a supplied denied governance context raises PermissionError.
- `InMemoryMemoryRepository(repository_id, records)` takes an explicitly controlled startup seed.
  It exposes no write, update, delete or candidate-promotion method. Its internal `read(scope)` is
  not an authorization endpoint: application callers must use MemoryRetriever.
- `MemoryRetriever(repository, writer).retrieve(request, grant=..., security=...)` returns
  MemoryRetrievalResult. A trusted PermissionGrant must authorize READ_DOCUMENT on the exact
  repository ID, requester, task and operational scope. The adapter represents manually controlled
  MemoryRecord documents; this does not create a general-purpose memory-write operation.

## Closed retrieval vocabulary

These are Stage 5 adapter conventions inside existing JSON fields, not new global taxonomies.
Unrecognized record metadata is excluded, not interpreted permissively.

| Field | Accepted convention |
|---|---|
| Request/record `scope` | Stage 3 OperationScope: project, explicit sections, phase 10, mode |
| Request `memory_types`, `retention_classes` | Nonempty unique lists of canonical enum values |
| Request `sensitivity_constraints` | Nonempty list containing only PUBLIC and/or INTERNAL |
| Request `freshness_requirement` | Empty or max_age_seconds (nonnegative strict integer), verified_after (aware datetime) |
| Request `confidence_requirement` | Optional minimum; unknown record confidence cannot meet a minimum |
| Request `query` | Nonblank lexical terms, at most 2,000 characters; no wildcard load-all |
| Request `max_results` | 1–50; repository snapshots bounded to 10,000 records |
| Record `authority_metadata` | Explicit readers, optional confidence + confidence_source, expires_at, task_id |
| `confidence_source` | USER_EXPLICIT, VALIDATOR_DERIVED or UNKNOWN; a value requires known provenance |
| Record `validation_state` | status PASS/UNVERIFIED/CONFLICTED, verified_at, optional conflict_refs |
| Record `status` | ACTIVE is eligible; CONFLICTED is reported and excluded; other values excluded |

Metadata is trusted only because an authorized adapter controls the seed. A string such as USER,
PUBLIC, PASS or APPROVED in arbitrary user/model output proves no identity or authorization. There is
no public ingestion API. Future adapters must preserve these trust boundaries and enforce upstream
record access; they must raise MemoryRepositoryError on backend failure, not return fabricated data.

Record scope must fit the requested and granted operational scope. Readers are checked separately.
Known sensitive-data patterns are excluded even when a record is labeled PUBLIC/INTERNAL. Other
sensitivity classes require future safeguards. This is not a complete sensitive-data detector.

TEMPORARY requires a future expires_at; ACTIVE requires the current task_id. Any explicit task_id
must match. Expired records never return. All records require created_at <= updated_at <= verified_at
<= now; freshness uses verified_at, not merely a recent update. PERSISTENT is not exempt from freshness.

Ranking uses matched lexical term count, then update time, then ID. It is not truth or source
precedence. Exact duplicate content with the same provenance/classification is minimized; semantic
duplicates/contradictions are not detected. Declared conflicts are reported only after access filters,
without disclosing possibly unauthorized conflict_refs. No record is overwritten or deleted.

## Results, auditing and limits

SUCCESS contains eligible records; EMPTY means no eligible match, not proof that the store is empty.
DENIED means the access gate failed. INCONCLUSIVE means unsupported requirements or unreliable backend
data. Excluded records' IDs/counts are not disclosed. Known conflict IDs are exposed only when eligible
for the same reader/scope/sensitivity. Context assembly blocks on reported conflicts.

AuditWriter must succeed before a candidate, retrieval result or validation result returns. Audit logs
contain IDs and outcomes, not candidate content, query text or record payloads. Logs persist audit
events, **not memory records**. AuditWriteError propagates. Invalid canonical input or a naive clock
raises before processing; raw validation errors must not be exposed by a future public transport.

Inputs and results are detached snapshots. Grants are checked before repository access and again
after the read. Revocation/security observations are trusted per-call snapshots, not a continuously
updated identity system. Supply fresh observations on every request. No model invocation, vector
search, semantic truth check, automatic persistence, consolidation, deletion or provider disclosure.

Candidate validation checks structure, required values, declared conflict state, scope and security.
NONE_REPORTED means only that no conflict was reported. PASS does not establish semantic uniqueness,
source truth, long-term eligibility or permission to persist. Candidates remain PENDING proposals.

Tests: `uv run pytest tests/memory -W error`.
