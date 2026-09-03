# ROBERT_CONTEXT_AND_MEMORY_INTERFACES_IMPLEMENTATION

**Versión:** 0.1
**Fecha:** 03/09/2026
**Estado:** IMPLEMENTED / LOCALLY VERIFIED
**Decisión:** #047
**Cambio:** #073
**Build Stage:** 5 — CONTEXT / MEMORY INTERFACES

## Alcance y organización

Implementa ROBERT_BUILD_ORDER secciones 31–35. Conserva los 29 contratos y 29 schemas canónicos.
Reutiliza Governance Core, Validation Core y AuditWriter. No modifica sus contratos ni políticas.

| Criterio de salida | Implementación |
|---|---|
| Context assembly | `src/robert/context/assembly.py`, RequestContext canónico |
| Create memory candidate | `MemoryCandidateService.create`, propuesta PENDING auditada |
| Validate memory candidate | Stage 4 más gate PREPARE_DRAFT; PASS no implica persistencia |
| Memory repository interface | Protocol de solo lectura y semilla manual en memoria del proceso |
| Read authorized memory | Gate READ_DOCUMENT del repositorio y filtros por registro |
| Return retrieval result | MemoryRetrievalResult canónico y auditoría obligatoria |

Los adaptadores internos no son nuevas entidades canónicas. Se documenta el vocabulario de scope,
authority_metadata, validation_state, freshness_requirement y sensibilidad en `src/robert/memory/README.md`.
Las clases de sensibilidad y metadata son convenciones locales conservadoras, no una nueva jerarquía
global. Los valores desconocidos no otorgan acceso.

## Fronteras preservadas

- Contexto, salida de modelo y candidato no se convierten automáticamente en MemoryRecord.
- La carga manual existe solo al construir el adaptador; no hay API de escritura ni almacén persistente.
- Los permisos pertenecen a adaptadores de confianza y se vinculan a tarea, requester, operación,
  recurso y alcance. Además se comprueban lectores explícitos en cada registro.
- Retention y MemoryType permanecen independientes. TEMPORARY expira; ACTIVE requiere tarea; PERSISTENT
  sigue sujeto a freshness. Confidence desconocida no satisface un mínimo solicitado.
- Se bloquea antes de consultar un repositorio no autorizado y se revalida caducidad tras la consulta.
- Datos sensibles conocidos se excluyen; no se habilitan PRIVATE/RESTRICTED/SECRET sin salvaguardas.
- Ranking léxico no resuelve precedencia ni verdad. Conflictos declarados se excluyen y escalan;
  ContextAssembler no devuelve contexto cuando hay conflictos o referencias requeridas ausentes.
- Los datos recuperados conservan provenance y referencias, pero no reemplazan reglas ni Decisions.
- La auditoría no duplica contenidos, queries ni payloads. Su fallo impide devolver el resultado.

## Límites explícitos

No hay autenticación pública, motor semántico, comprobación externa de fuentes, detección semántica de
contradicciones, evaluación completa de elegibilidad persistente ni resolución automática de conflictos.
La confianza declarada no es calibración estadística. La clasificación de sensibilidad y la semilla
requieren control de un adaptador confiable; los patrones detectados no certifican ausencia de secretos.

Los permisos/observaciones son snapshots por llamada, no un servicio continuo de revocación. No hay
escritura automática, consolidación, borrado, base vectorial, conexiones externas ni Model Interface.
Los eventos AuditEvent sí se escriben al almacén de auditoría existente; no contienen la memoria.

## Verificación

Base: Stage 4 en main `8fd54df77d9f58e946ea524bc95d321ad1b21515`, con árbol idéntico al local y
342 pruebas correctas. Los detalles de la verificación final se registran en CAMBIO #073.
La publicación en main y su CI son pasos separados; este documento no afirma haberlos ejecutado.

```text
TECHNICAL_IMPLEMENTATION: STAGES 0–5 COMPLETE
AUTHORIZED_BUILD_BOUNDARY: STAGE 5
STAGE_6: NOT AUTHORIZED
PHASE_11: NOT STARTED
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
AUTOMATIC_MEMORY_WRITE: DISABLED
REAL_TOOL_EXECUTION: DISABLED
```
