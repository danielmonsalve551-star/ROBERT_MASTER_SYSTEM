# Skill Layer — Stage 7

`robert.skill` implementa Skills internas, reutilizables y sin efectos externos.

```text
EXPLICIT SKILL INVOCATION
→ MANIFEST CHECK
→ EXACT REGISTRY LOOKUP
→ INTERNAL PROCEDURE
→ VALIDATED SKILL RESULT
→ REQUIRED AUDIT
```

Componentes:

- `inputs.py`: Manifest, output contract y vocabulario runtime cerrado;
- `registry.py`: catálogo explícito sin selección ni routing;
- `procedure.py`: puerto de procedimiento y primera Skill determinista;
- `runner.py`: límites, ejecución interna, validación y auditoría;
- `catalog.py`: Manifest oficial de `contradiction_detection`.

`contradiction_detection` compara claims por subject normalizado y reporta valores diferentes. No
decide cuál claim es verdadero, no consulta Models, no recupera Memory y no invoca Tools.

## Límites

```text
SKILL RESULT ≠ DECISION
SKILL REQUIREMENT ≠ PERMISSION
SKILL REGISTRY ≠ ROUTING AUTHORITY
SKILL RUNNER ≠ EXECUTION AUTHORITY
TOOL REQUEST ≠ TOOL EXECUTION
```

La Invocation debe coincidir con el Manifest registrado. El caller no puede eliminar constraints,
cambiar requisitos ni sustituir el output contract. El Audit contiene referencias y estados, no el
input ni el output completo.

```bash
uv run pytest tests/skill -W error
uv run ruff check src/robert/skill tests/skill
uv run ruff format --check src/robert/skill tests/skill
```
