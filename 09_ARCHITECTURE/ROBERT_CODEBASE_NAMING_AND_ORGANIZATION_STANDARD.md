# ROBERT_CODEBASE_NAMING_AND_ORGANIZATION_STANDARD

**Versión:** 0.1
**Estado:** APPROVED / ACTIVE
**Fecha:** 01/09/2026
**Decisión:** #043
**Cambio:** #069

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
scripts/export_contract_schemas.py
```

---

# 4. Criterio de aceptación

Todo cambio futuro debe permitir que una persona identifique rápidamente:

```text
WHAT IT IS
WHERE IT LIVES
WHO OWNS THE CONTRACT
WHETHER IT IS SOURCE OR GENERATED OUTPUT
WHAT AUTHORIZATION BOUNDARY APPLIES
```
