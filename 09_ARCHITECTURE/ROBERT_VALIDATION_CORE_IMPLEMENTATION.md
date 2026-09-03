# ROBERT_VALIDATION_CORE_IMPLEMENTATION

**Versión:** 0.1
**Fecha:** 03/09/2026
**Estado:** IMPLEMENTED / VERIFIED
**Decisión:** #046
**Cambio:** #072
**Build Stage:** 4 — VALIDATION CORE

## Alcance y organización

Implementa `ROBERT_BUILD_ORDER` secciones 27–30 y las dimensiones iniciales previstas en
`ROBERT_VALIDATION_ARCHITECTURE`. Código en `src/robert/validation/`; pruebas en `tests/validation/`.
La interfaz consume ValidationRequest y produce ValidationResult canónicos. ValidationTarget,
ValidationCriterion y CheckFinding son adaptadores internos, no nuevas entidades ni contratos wire.
Los 29 contratos y sus 29 schemas siguen siendo la única fuente técnica canónica.

## Validaciones iniciales

| Dimensión | Comportamiento implementado |
|---|---|
| RULE | Vocabulario declarativo cerrado, sin eval, código ni llamadas externas |
| CANONICAL | Nombre/versión conocidos y validación JSON estricta del contrato registrado |
| STRUCTURE | Estructura/tipos del contrato o criterios explícitos |
| COMPLETENESS | Campos obligatorios presentes, criterios y referencias requeridas |
| CONSISTENCY | Comparación de campos declarados; conflictos reportados, nunca resueltos por mayoría |
| SECURITY | Contexto confiable verificado, pausas/conflictos/datos sensibles, fase y capacidades deshabilitadas |
| PERMISSION | Reutiliza comprobación Stage 3 con caducidad, revocación y vinculación |
| SCOPE | Reutiliza Stage 3: límites explícitos, fase, modo, secciones y techo de riesgo |

No se implementan revisión por Model/Agent/User ni validación semántica de evidencia, fuentes,
Memory o ModelOutput. Solicitar esas capacidades devuelve INCONCLUSIVE bloqueante, no una aprobación
simulada. La comparación canónica solo verifica contratos/criterios técnicos, no toda la arquitectura.

## Mapeo a ValidationResult sin cambiar el contrato

| Requisito conceptual | Campo canónico utilizado |
|---|---|
| passed_checks / failed_checks | `checks[]` con `status=PASS/FAIL/UNKNOWN` |
| warnings | `issues[]` con `kind=WARNING` |
| conflicts | `issues[]` con `kind=CONFLICT` y/o `conflict=true` |
| confidence | `confidence=null`, sin estimación calibrada inventada |
| limitations | `limitations[]`, siempre explica cobertura y límites |
| evidence / sources | `evidence[]` / `sources[]`, referencias suministradas |
| recommended_next_step | Campo canónico homónimo |
| BLOCKED conceptual | `status=FAIL/INCONCLUSIVE` más `blocking=true` |

Los requisitos obligatorios fallidos bloquean. Requisitos no disponibles dejan el resultado inconcluso
y bloqueante. Solo fallos opcionales permiten PASS_WITH_WARNINGS. Las restricciones y comprobaciones
de seguridad no admiten degradación a opcionales. Ningún resultado modifica aprobaciones o permisos.

## Auditoría y fronteras de confianza

Se reutiliza AuditWriter. Cada resultado conserva `audit_reference`, identidad de tarea/validación y
referencia al target. La auditoría almacena referencias, estado y contadores; no duplica el payload,
valores de criterios ni entradas crudas de excepciones. Si la escritura falla, no se devuelve PASS.
Se copian y revalidan entradas antes de evaluar para aislar colecciones mutables y rechazar NaN/Infinity.

Permisos/seguridad provienen de adaptadores de confianza: los strings de un payload no autentican a
nadie. Los contextos canónicos serializados no vacíos aún no tienen vocabulario autorizado y producen
INCONCLUSIVE. La presencia de una referencia no prueba su contenido ni su vigencia. El futuro caller
debe elegir todos los tipos necesarios; Stage 4 no es un Orchestrator ni un sistema completo de seguridad.

## Verificación y estado

La evidencia final se registra en CAMBIO #072: regresiones previas, 29 contratos, validaciones válidas,
fallidas e inconclusas, advertencias, conflictos, permisos, seguridad y errores de auditoría.

```text
TECHNICAL_IMPLEMENTATION: STAGES 0–4 COMPLETE
AUTHORIZED_BUILD_BOUNDARY: STAGE 4
STAGE_5: NOT AUTHORIZED
PHASE_10_CLOSED: YES
PHASE_11: NOT STARTED
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
REAL_TOOL_EXECUTION: DISABLED
```
