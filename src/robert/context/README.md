# Context Assembly — Stage 5

`ContextAssembler.assemble()` combines an existing Task and explicitly selected ContextFragment inputs
into the canonical RequestContext. There is no new SessionRecord, ContextSnapshot, session store or
model/provider call.

- Require a current trusted READ_DOCUMENT PermissionGrant for the task ID, requester and Task's
  operational scope, plus verified SecurityContext. Block paused/security failures and blocked tasks.
- `task.authorized_scope` must use the Stage 3 OperationScope vocabulary. Task.phase must be "10".
- Every task.context_refs entry must have exactly one selected fragment; reject missing/duplicate
  references, unselected sources, wrong task/requester, broader scope or known sensitive payloads.
- Fragments are trusted adapter inputs, not arbitrary signed grants. The caller must verify source
  access before supplying them. Only PUBLIC/INTERNAL fragments are supported locally.
- With no memory_request, perform no memory retrieval. Nonempty task.memory_refs require fresh
  retrieval through an injected trusted MemoryRetrieval implementation and its separate memory_grant.
- Do not accept a previously serialized retrieval result as proof of access. Fetch again, bind task
  and request IDs, require an audit reference and usable status, and block conflicts/missing references.
- Keep conversation, documents, retrieved memory and system constraints separate. Text claiming
  "approved" or requesting a different phase remains data and cannot replace governance fields.
- Recheck the context grant before disclosure; require final audit persistence before return.

ContextAssemblyError means no partial context is returned. AuditWriteError propagates. Unsupported
canonical inputs/scope vocabulary fail validation before processing. A future transport must map
exceptions without exposing raw input. The retrieval port is a trusted code dependency, not an
untrusted plugin boundary: its implementation must enforce the memory interface contract.

The audit reference is preserved inside RequestContext.authorized_context, using the existing JSON
field. Memory retrieval retains its own audit_reference. Assembly never persists the Task, fragments,
RequestContext or MemoryRecord. No automatic memory writing or external disclosure is enabled.

Tests: `uv run pytest tests/context -W error`.
