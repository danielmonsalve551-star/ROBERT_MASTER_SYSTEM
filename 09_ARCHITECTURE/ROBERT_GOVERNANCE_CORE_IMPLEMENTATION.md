# ROBERT_GOVERNANCE_CORE_IMPLEMENTATION

**Versión:** 0.1
**Fecha:** 03/09/2026
**Estado:** IMPLEMENTED / VERIFIED
**Decisión:** #045
**Cambio:** #071
**Build Stage:** 3 — GOVERNANCE CORE

## Fuente y organización

Se implementa el orden definido en `ROBERT_BUILD_ORDER` secciones 22–26, junto con las reglas de
permisos, alcance, expiración y revocación. Los resultados utilizan `PermissionCheck`, `ScopeCheck`,
`RiskAssessment`, `ApprovalResult`, `Block` y `AuditEvent` existentes. No se crean contratos canónicos
paralelos. Las clases de entrada son estructuras internas de adaptación, no fuentes de autoridad.

Código: `src/robert/governance/`. Pruebas: `tests/governance/`.
La revisión previa y las correcciones están documentadas en
`ROBERT_STAGE_3_PREIMPLEMENTATION_AUDIT.md`.

## Política inicial explícita

| Operación | Riesgo mínimo | Aprobación | Ejecución habilitada |
|---|---:|---|---|
| READ_DOCUMENT | 0 | No, salvo riesgo declarado alto | No ejecuta acciones; solo evaluación |
| PREPARE_DRAFT | 2 | No, salvo riesgo declarado alto | No ejecuta acciones; solo evaluación |
| UPDATE_DOCUMENT | 3 | Humana explícita y vinculada | No ejecuta acciones; solo evaluación |
| DELETE_RESOURCE | 4 | No basta para levantar el bloqueo | No |
| EXTERNAL_ACTION, CONNECT_TOOL, RUN_CODE, ACTIVATE_AGENT, AUTOMATE, CHANGE_PHASE | 3 | No basta para otorgar Execution Authority | No |

Estos mínimos son decisiones conservadoras de implementación, no una evaluación semántica general
de todos los recursos. El adaptador de confianza debe elevar el riesgo cuando corresponda y clasificar
correctamente la operación. Datos sensibles o conflicto crítico bloquean en Security; riesgo 4 bloquea
en Risk. Se conserva la escala oficial 0–4 y autonomía 0.

## Orden y fallo seguro

1. Permission: autoridad humana declarada por adaptador confiable, vinculación a tarea/actor/operación/
   recurso, vigencia, revocación y consumo.
2. Scope: mismo proyecto, fase 10, modo y secciones explícitas autorizadas; sin comodines.
3. Risk: máximo entre mínimo fijo y riesgo declarado; no superar techo del permiso ni aceptar nivel 4.
4. Security: estado verificado, sin pausa, conflicto crítico ni datos sensibles sin protección.
5. Approval: estado aprobado, humano verificado por adaptador, vigencia y vinculación exacta a tarea,
   operación, recurso y alcance. Condiciones sin evaluador bloquean.
6. Execution Authority: NONE; ninguna variable de entorno puede elevarla.

Cada fallo produce Block y AuditEvent. Una escritura de auditoría fallida impide retornar ALLOWED.
ALLOWED no es una capacidad de ejecución ni permite usar la aprobación después de la evaluación.

## Verificación y límites

Las pruebas cubren el orden, todas las operaciones cerradas, rechazos, expiración, revocación,
riesgos, aprobaciones incompatibles, manipulación de inputs, auditoría y aislamiento de colecciones.
No hay endpoints nuevos, autenticación de usuarios, almacén productivo de permisos ni ejecución.

Verificación local final: 199 pruebas aprobadas con warnings tratados como errores; lockfile,
Ruff, formato, comparación completa de 29 schemas y `git diff --check` aprobados.

```text
TECHNICAL_IMPLEMENTATION: STAGES 0–3 COMPLETE
AUTHORIZED_BUILD_BOUNDARY: STAGE 3
STAGE_4: NOT AUTHORIZED
PHASE_10_CLOSED: YES
PHASE_11: NOT STARTED
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
REAL_TOOL_EXECUTION: DISABLED
```
