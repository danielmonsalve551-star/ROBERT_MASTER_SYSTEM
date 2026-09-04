# ROBERT_MODEL_INTERFACE_IMPLEMENTATION

**Versión:** 0.1
**Estado:** IMPLEMENTADO Y VERIFICADO — STAGE 6
**Fecha:** 04/09/2026
**Decisión:** DECISIÓN #048
**Cambio:** CAMBIO #074
**Fase:** 10 — cerrada
**Autonomy Level:** 0
**Execution Authority:** NONE

## 1. Alcance implementado

Stage 6 implementa la abstracción de Models antes de Agents:

```text
MODEL REQUEST
↓
MODEL ROUTER
↓
MODEL PROVIDER INTERFACE
↓
MODEL ADAPTER
↓
MODEL RESPONSE
↓
VALIDATION + AUDIT
```

El código vive en `src/robert/model/`; las pruebas en `tests/model/`. Los contratos canónicos
`ModelRequest`, `ModelResponse` y `ToolRequest` se reutilizan sin crear contratos wire paralelos.

## 2. Componentes

- `ModelRegistry`: separa perfiles relativamente estables de estados runtime suministrados.
- `ModelRouter`: filtra provider, capacidades obligatorias, Context, sensibilidad, soporte estructurado,
  Tool Calling, disponibilidad y rate limit; después ordena de forma determinista.
- `ModelProvider`: puerto mínimo inyectado, sin SDK ni conexión incluidos en el repositorio.
- `StructuredProviderAdapter`: traduce requests, descarta autoridad implícita y normaliza responses.
- `ModelInterface`: admite requesters explícitos, aplica límites, valida output, controla fallback y audita.
- `NormalizedModelError`: representa fallos sin copiar excepciones o payloads crudos del proveedor.

## 3. Límites preservados

No se implementan llamadas de red reales. El puerto se prueba con un proveedor determinista en
proceso. Tampoco se implementan Models productivos, credenciales, SDKs, Agents ni routing autónomo.

Un Model no puede conceder Permission, Scope, Approval, Autonomy ni Execution Authority. La identidad
del modelo y proveedor la fija el Adapter, no el payload recibido.

Las solicitudes de Tool se convierten a `ToolRequest` con requester `MODEL:<model_id>`, controles
separados requeridos y `side_effect_class=REQUEST_ONLY_NO_EXECUTION`. No existe ejecución directa.

Stage 6 rechaza `memory_write_allowed=true`. Ningún componente del paquete conoce una API de escritura
de Memory. Los outputs y consensos siguen siendo datos no verificados, no verdad ni decisiones.

## 4. Seguridad y fallos

- requester allowlist explícita, única y sin wildcard;
- Context y respuestas con patrones de secretos conocidos fallan cerrados;
- solicitudes de trazas privadas de razonamiento se rechazan;
- schemas de output estructurado usan un subconjunto cerrado y verificable;
- adapters ausentes o incompatibles no se invocan;
- retries/fallbacks están acotados a máximo tres intentos y solo usan modelos elegibles;
- timeouts, respuestas inválidas y fallos desconocidos regresan errores normalizados;
- una falla de Audit evita devolver ModelResponse o ToolRequest.

## 5. Evidencia de salida

La implementación parte de `5be3e5a07d75ddfd330be480bdda3160aea5bf05`, con 470 pruebas baseline.
La verificación final produjo:

```text
CANONICAL_CONTRACTS: 29 UNCHANGED
GENERATED_SCHEMAS: 29 UNCHANGED
STAGE_6_MODEL_TESTS: 37 PASSED
LOCAL_FULL_SUITE: 510 PASSED (WARNINGS AS ERRORS)
REAL_PROVIDER_CONNECTIONS: ABSENT
MODEL_CREDENTIALS: ABSENT
DIRECT_TOOL_EXECUTION: ABSENT
AUTOMATIC_MEMORY_WRITE: ABSENT
MODEL_OUTPUT_IS_AUTHORITY: FALSE
AUDIT_FAILURE: FAILS CLOSED
UV_LOCK_CHECK: PASS
RUFF_CHECK: PASS
RUFF_FORMAT_CHECK: PASS
SCHEMA_FULL_COMPARISON: PASS
GIT_DIFF_CHECK: PASS
```

## 6. Estado posterior

```text
TECHNICAL_IMPLEMENTATION: STAGES 0–6 COMPLETE
AUTHORIZED_BUILD_BOUNDARY: STAGE 6
STAGE_7: NOT AUTHORIZED
REAL_PROVIDER_CONNECTIONS: DISABLED
REAL_TOOL_EXECUTION: DISABLED
AUTOMATIC_MEMORY_WRITE: DISABLED
AUTONOMOUS_AGENTS: DISABLED
AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```
