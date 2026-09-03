# ROBERT_CODEBASE_NAMING_AND_ORGANIZATION_STANDARD

**Versión:** 0.5
**Estado:** APPROVED / ACTIVE
**Fecha:** 03/09/2026
**Decisiones:** #043 / #044 / #045 / #046 / #047
**Cambios:** #069 / #070 / #071 / #072 / #073

---

# 1. Objetivo

Mantener nombres claros, ubicación predecible y responsabilidades separadas en todo código nuevo de Robert.

---

# 2. Reglas obligatorias

1. Cada archivo debe tener una responsabilidad principal identificable.
2. Los nombres deben describir el dominio y la función; se prohíben nombres vagos como `utils2`, `misc`, `new`, `final` o `manager` sin dominio.
3. Los módulos Python utilizan `snake_case`.
4. Las clases y contratos utilizan `PascalCase` y conservan el nombre canónico aprobado.
5. Las constantes utilizan `UPPER_SNAKE_CASE`.
6. Los tests reflejan el comportamiento verificado mediante nombres `test_<resultado_esperado>`.
7. Los schemas generados utilizan `<contract_name>.schema.json` y se agrupan por dominio.
8. Una definición canónica debe tener una sola fuente técnica.
9. Los archivos generados se identifican y no se editan manualmente.
10. Ninguna reorganización puede crear Authority nueva ni ampliar el Stage autorizado.

---

# 3. Estructura técnica vigente

```text
src/robert/
├── app.py
├── config.py
├── context/
│   ├── inputs.py
│   └── assembly.py
├── memory/
│   ├── inputs.py
│   ├── candidates.py
│   ├── repository.py
│   └── retrieval.py
├── validation/
│   ├── inputs.py
│   ├── findings.py
│   ├── rule_validator.py
│   ├── contract_validator.py
│   ├── structure_validator.py
│   ├── context_validator.py
│   └── handler.py
├── governance/
│   ├── inputs.py
│   ├── policy.py
│   ├── checks.py
│   └── engine.py
├── audit/
│   ├── catalog.py
│   ├── outcome_builder.py
│   ├── event_builder.py
│   ├── redaction.py
│   ├── storage.py
│   └── writer.py
└── contracts/
    ├── base.py
    ├── envelope.py
    ├── task.py
    ├── orchestration.py
    ├── agent.py
    ├── skill.py
    ├── model.py
    ├── tool.py
    ├── memory.py
    ├── validation.py
    ├── governance.py
    ├── errors.py
    ├── audit.py
    └── registry.py

schemas/contracts/<owner>/<contract_name>.schema.json
tests/contracts/
tests/audit/
tests/governance/
tests/validation/
tests/memory/
tests/context/
tests/documentation/
scripts/export_contract_schemas.py
```

Stage 2 extiende este estándar mediante DECISIÓN #044 y CAMBIO #070 sin cambiar sus reglas.

Stage 3 añade Governance Core y pruebas de consistencia mediante DECISIÓN #045 / CAMBIO #071.
Las estructuras internas de adaptación no deben registrarse como contratos canónicos paralelos.

Stage 4 añade Validation Core mediante DECISIÓN #046 / CAMBIO #072, con módulos por responsabilidad
y una guía de vocabulario y límites en `src/robert/validation/README.md`.

---

# 4. Criterio de aceptación

Stage 5 incorpora Context / Memory Interfaces mediante DECISIÓN #047 / CAMBIO #073.
Cada paquete conserva su README de uso y límites. Los contratos siguen únicamente en `contracts/`.

Todo cambio futuro debe permitir que una persona identifique rápidamente:

```text
WHAT IT IS
WHERE IT LIVES
WHO OWNS THE CONTRACT
WHETHER IT IS SOURCE OR GENERATED OUTPUT
WHAT AUTHORIZATION BOUNDARY APPLIES
```
