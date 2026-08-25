# ROBERT_MODEL_INTERFACE_SPEC

**Versión:** 0.1
**Estado:** APROBADO — arquitectura documental vigente
**Tipo:** Especificación arquitectónica de interfaz de Models
**Ubicación:** `09_ARCHITECTURE/ROBERT_MODEL_INTERFACE_SPEC.md`
**Fase relacionada:** Fase 10 — MVP técnico básico en preparación
**Decisión de aprobación:** DECISIÓN #034
**Cambio de integración:** CAMBIO #059

**Dependencias principales:**

* `ROBERT_CANONICAL_MODEL v0.2`
* `ROBERT_ORCHESTRATOR_SPEC v0.1`
* `ROBERT_AGENT_ARCHITECTURE v0.1`
* `ROBERT_SKILL_ARCHITECTURE v0.1`
* `ROBERT_SYSTEM_ARCHITECTURE`
* `ROBERT_MODULES`
* `ROBERT_SECURITY_RULES`
* `ROBERT_CONTEXT_MASTER`
* `ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC`
* `ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC`
* `ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC`
* `ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC`

---

# 1. Propósito

`ROBERT_MODEL_INTERFACE_SPEC` define la interfaz uniforme mediante la cual Robert puede utilizar distintos Models sin acoplar Agents, Skills u otros componentes a un proveedor específico.

Objetivo principal:

```text
ROBERT
  ↓
ORCHESTRATOR
  ↓
MODEL ROUTER
  ↓
MODEL INTERFACE
  ↓
MODEL ADAPTER
  ↓
MODEL
```

en lugar de:

```text
AGENT
  ↓
CLAUDE-SPECIFIC LOGIC
```

o:

```text
SKILL
  ↓
CHATGPT-SPECIFIC LOGIC
```

---

# 2. Definición

Un Model es una entidad capaz de procesar información y producir resultados intelectuales, analíticos o generativos.

Ejemplos actuales:

```text
Claude
ChatGPT
```

Futuros Models pueden integrarse bajo el mismo contrato.

Por tanto:

```text
MODEL ≠ AGENT
MODEL ≠ SKILL
MODEL ≠ TOOL
MODEL ≠ MODULE
MODEL ≠ ORCHESTRATOR
MODEL ≠ ROBERT
```

---

# 3. Principio fundamental

Robert debe depender de capacidades y contratos, no de marcas o proveedores.

Preferencia:

```text
REQUIRED CAPABILITIES
        ↓
MODEL ROUTER
        ↓
MODEL INTERFACE
        ↓
MODEL ADAPTER
        ↓
COMPATIBLE MODEL
```

No:

```text
IF CLAUDE → PATH A
IF CHATGPT → PATH B
```

distribuido por todo Robert.

---

# 4. Posición arquitectónica general

El uso de un Model no requiere obligatoriamente una Skill.

Flujo general:

```text
AUTHORIZED REQUESTER
        ↓
CAPABILITY REQUEST
        ↓
ORCHESTRATOR
        ↓
CAPABILITY RESOLUTION
   ├── AGENT
   ├── SKILL
   ├── MODEL
   └── TOOL
        ↓
MODEL REQUIRED?
        ↓
MODEL ROUTER
        ↓
MODEL INTERFACE
        ↓
MODEL ADAPTER
        ↓
MODEL
```

Reglas:

```text
MODEL USE ≠ SKILL REQUIRED

SKILL MAY REQUIRE MODEL
```

---

# 5. Uso de Model mediante Skill

Cuando una Skill requiera inteligencia de un Model:

```text
AGENT
  ↓
CAPABILITY REQUEST
  ↓
ORCHESTRATOR
  ↓
SKILL RESOLVER
  ↓
SKILL
  ↓
MODEL REQUIREMENTS
  ↓
MODEL ROUTER
  ↓
MODEL INTERFACE
  ↓
MODEL
```

Por tanto, Skill y Model permanecen desacoplados.

---

# 6. Authorized Requester

Conceptualmente, un `AUTHORIZED REQUESTER` puede ser:

```text
AGENT
VALIDATOR
ORCHESTRATOR
AUTHORIZED ROBERT COMPONENT
```

cuando la arquitectura y el contexto operativo lo permitan.

Pero:

```text
AUTHORIZED REQUESTER ≠ ROUTING AUTHORITY
```

El Orchestrator conserva el routing.

---

# 7. Separación de responsabilidades

```text
ORCHESTRATOR
= routing authority

MODEL ROUTER
= model selection

MODEL INTERFACE
= common contract

MODEL ADAPTER
= provider translation

MODEL
= intelligence processing
```

Ninguno sustituye a los demás.

---

# 8. Responsabilidades de Model Interface

Model Interface normaliza conceptualmente:

* Request;
* Task;
* Context;
* Instructions;
* Constraints;
* expected output;
* Model requirements;
* Tool context;
* Evidence requirements;
* Source requirements;
* Responses;
* Errors;
* usage metadata;
* provider differences;
* structured outputs;
* limitations;
* validation metadata.

---

# 9. Lo que Model Interface NO hace

Model Interface no puede:

* tomar Decisions;
* sustituir al Orchestrator;
* crear Permissions;
* ampliar Scope;
* crear Autonomy;
* crear Execution Authority;
* seleccionar Tools unilateralmente;
* conceder Approval;
* alterar Phase;
* persistir Memory por sí sola;
* tratar output del Model como Truth;
* tratar consenso entre Models como Truth;
* convertirse en autoridad de seguridad.

---

# 10. Model Request

Contrato conceptual:

```text
MODEL_REQUEST

request_id
task_id
requester
purpose
task
context
instructions
constraints
expected_output
required_capabilities
preferred_capabilities
tool_context
evidence_requirements
source_requirements
risk_context
permission_context
scope_context
validation_requirements
model_policy
```

---

# 11. Model Response

Contrato conceptual:

```text
MODEL_RESPONSE

request_id
model_id
provider
model_version
result
rationale_summary
evidence
sources
risks
conflicts
confidence
confidence_source
limitations
assumptions
tool_requests
validation_notes
usage
errors
```

No todos los campos son obligatorios para todas las Tasks.

---

# 12. Rationale Summary

Robert puede solicitar una explicación breve y útil sobre la base del resultado:

```text
rationale_summary
```

Pero:

```text
RATIONALE SUMMARY ≠ PRIVATE REASONING TRACE
```

Y:

```text
MODEL INTERFACE MUST NOT REQUIRE PRIVATE CHAIN OF THOUGHT
```

Robert no debe depender de razonamiento interno privado de un Model para funcionar correctamente.

---

# 13. Structured Result

Cuando resulte apropiado, se prefiere:

```text
STRUCTURED OUTPUT
```

sobre texto completamente libre.

Ejemplo:

```yaml
result:
  summary:
  findings:
  recommendations:

evidence:

sources:

risks:

conflicts:

confidence:

limitations:
```

---

# 14. Provider Adapter

Cada proveedor se conecta mediante un Adapter.

```text
MODEL INTERFACE
   ├── CLAUDE ADAPTER
   ├── OPENAI ADAPTER
   └── FUTURE MODEL ADAPTER
```

El Adapter transforma el contrato común al formato técnico de cada proveedor.

---

# 15. Adapter Responsibilities

Un Model Adapter puede:

* transformar mensajes;
* mapear roles;
* mapear instrucciones;
* mapear structured outputs;
* traducir Tool schemas;
* configurar límites;
* normalizar responses;
* normalizar usage;
* detectar errores;
* traducir provider errors;
* interpretar Tool Requests.

---

# 16. Adapter Restrictions

Un Adapter no puede:

```text
CHANGE TASK INTENT
EXPAND SCOPE
CREATE PERMISSIONS
CREATE AUTONOMY
CREATE EXECUTION AUTHORITY
CREATE APPROVAL
ALTER SECURITY POLICY
ALTER PHASE
HIDE PROVIDER ERRORS
```

El Adapter traduce.

No gobierna.

---

# 17. Adapter Tool Boundary

Un Model Adapter puede:

* traducir Tool schemas;
* exponer Tool definitions al proveedor;
* interpretar Tool Requests;
* normalizar Tool Call arguments;
* recibir Tool Results;
* devolver Tool Results al Model.

No puede autorizar ni ejecutar independientemente una Tool.

```text
ADAPTER TOOL SUPPORT
        ≠
TOOL EXECUTION AUTHORITY
```

Flujo:

```text
MODEL
  ↓
PROVIDER TOOL REQUEST
  ↓
MODEL ADAPTER
  ↓
MODEL INTERFACE
  ↓
ORCHESTRATOR
  ↓
TOOL RESOLVER
  ↓
AUTHORIZATION CHECK
  ↓
TOOL
```

Aunque técnicamente un proveedor soporte native tool calling, la autoridad lógica permanece en Robert.

---

# 18. Model Registry

Se define conceptualmente:

```text
ROBERT_MODEL_REGISTRY
```

Cada Model registrado deberá poder declarar:

```text
model_id
provider
model_family
model_name
model_version
status
capabilities
limitations
context_window
modalities
tool_support
structured_output_support
reasoning_profile
adapter
```

Los detalles técnicos definitivos quedan pendientes.

---

# 19. Model Profile vs Runtime State

Se distingue conceptualmente entre información relativamente estable y estado dinámico.

```text
MODEL PROFILE
- identity
- provider
- family
- version
- capabilities
- limitations
- modalities
- adapter
```

y:

```text
MODEL RUNTIME STATE
- availability
- health
- latency
- cost information
- rate limitations
```

Esto evita mezclar identidad del Model con condiciones operativas cambiantes.

---

# 20. Model Identity

Debe distinguirse:

```text
PROVIDER
MODEL FAMILY
MODEL VERSION
MODEL INSTANCE
```

Por ejemplo:

```text
provider: OpenAI
family: GPT
version: specific-version
```

`ChatGPT` o `Claude` por sí solos no son identidad técnica suficiente para una implementación futura.

---

# 21. Model Capabilities

Ejemplos conceptuales:

```text
reasoning
long_context
coding
document_analysis
vision
structured_output
tool_calling
multilingual
summarization
critique
planning
```

El catálogo definitivo se normalizará posteriormente.

---

# 22. Required vs Preferred Capabilities

Una Task puede declarar:

```text
required_capabilities
```

y:

```text
preferred_capabilities
```

Ejemplo:

```yaml
required_capabilities:
  - coding

preferred_capabilities:
  - long_context
  - structured_output
```

Si un Model no cumple una Capability obligatoria:

```text
MODEL NOT ELIGIBLE
```

---

# 23. Model Router

Model Router selecciona un Model según:

```text
required_capabilities
preferred_capabilities
task_type
context_size
risk
evidence_requirements
tool_requirements
latency
cost
availability
health
fallback_policy
validation_requirements
```

---

# 24. Selection Authority

```text
MODEL PREFERENCE ≠ MODEL SELECTION AUTHORITY
```

Agents y Skills pueden declarar requisitos o preferencias.

Model Router realiza la selección bajo Orchestrator.

---

# 25. Model Ranking

Conceptualmente:

```text
REGISTERED MODELS
      ↓
FILTER REQUIRED CAPABILITIES
      ↓
FILTER SECURITY / POLICY
      ↓
FILTER AVAILABILITY
      ↓
FILTER CONTEXT COMPATIBILITY
      ↓
RANK
      ↓
SELECT
```

El ranking futuro puede considerar:

```text
quality
cost
latency
reliability
context_fit
task_fit
tool_fit
historical_performance
```

---

# 26. No Universal Best Model

Robert no debe asumir:

```text
ONE MODEL = BEST FOR EVERYTHING
```

Preferencia:

```text
BEST ELIGIBLE FIT FOR CURRENT TASK
```

---

# 27. Agent Model Requirements

Ejemplo:

```text
ROBERT_CODER

preferred_capabilities:
- coding
- debugging
- structured_output
```

El Agent no necesita estar permanentemente acoplado a un proveedor.

---

# 28. Skill Model Requirements

Ejemplo:

```text
architecture_review

required_capabilities:
- reasoning

preferred_capabilities:
- long_context
- structured_output
```

---

# 29. Context Packaging

Model Interface deberá utilizar:

```text
MINIMUM SUFFICIENT CONTEXT
```

El Context Package puede contener:

```text
task_context
canonical_context
decision_context
memory_context
source_context
security_context
```

---

# 30. Context Authority

El Context debe poder conservar información sobre autoridad.

Ejemplos:

```text
CANONICAL
APPROVED
REFERENCE
TEMPORARY
UNVERIFIED
```

El Model no debe tratar todo Context como igualmente autoritativo.

---

# 31. Context Priority

Conceptualmente:

```text
SECURITY / GOVERNANCE
        ↓
CANONICAL MODEL
        ↓
APPROVED DECISIONS
        ↓
CURRENT TASK
        ↓
AUTHORIZED CONTEXT
        ↓
REFERENCE MATERIAL
```

La implementación deberá permanecer compatible con las reglas canónicas vigentes.

---

# 32. Instruction Layers

Model Interface puede representar:

```text
SYSTEM CONSTRAINTS
ROBERT GOVERNANCE
TASK INSTRUCTIONS
SKILL PROCEDURE
CONTEXT
USER INPUT
OUTPUT FORMAT
```

Los proveedores pueden representarlas técnicamente de formas distintas.

El Adapter realiza la traducción.

---

# 33. Prompt Independence

Agents y Skills no deberían depender de prompts propietarios gigantes.

Preferencia:

```text
STRUCTURED INSTRUCTIONS
+
SKILL PROCEDURE
+
CONTEXT PACKAGE
+
OUTPUT CONTRACT
```

El Adapter traduce este contenido al mecanismo específico del proveedor.

---

# 34. Model Output ≠ Decision

```text
MODEL OUTPUT ≠ DECISION
```

Un Model puede producir:

```text
ANALYSIS
PROPOSAL
RECOMMENDATION
EVIDENCE
CODE
PLAN
```

sin convertir automáticamente esos resultados en Decisions autorizadas.

---

# 35. Model Output ≠ Truth

```text
MODEL OUTPUT ≠ TRUTH
```

Un Model puede:

* equivocarse;
* producir información no respaldada;
* interpretar mal Context;
* trabajar con información desactualizada;
* producir resultados estructuralmente inválidos.

Por eso puede requerirse Validation.

---

# 36. Consensus Rule

Cuando participen varios Models:

```text
MODEL A AGREES
+
MODEL B AGREES
≠
TRUTH
```

Y:

```text
CONSENSUS ≠ AUTHORIZATION
```

El consenso constituye evidencia adicional, no autoridad.

---

# 37. Multi-Model Mode

Robert puede utilizar varios Models.

Ejemplo:

```text
TASK
  ↓
ORCHESTRATOR
  ↓
MODEL ROUTER
  ├── MODEL A
  └── MODEL B
        ↓
AUTHORIZED RESULTS
        ↓
VALIDATION
```

---

# 38. Multi-Model Mediation

Los Models no deben comunicarse directamente de manera autónoma.

Flujo:

```text
MODEL A
  ↓
MODEL INTERFACE
  ↓
ORCHESTRATOR
  ↓
AUTHORIZED CONTEXT TRANSFER
  ↓
MODEL ROUTER
  ↓
MODEL B
  ↓
MODEL INTERFACE
  ↓
VALIDATION
```

Reglas:

```text
MODEL A ≠ AUTHORITY OVER MODEL B

MODEL-TO-MODEL TRANSFER
MUST BE MEDIATED BY ROBERT

PRIMARY MODEL ≠ ROUTING AUTHORITY
```

---

# 39. Multi-Model Patterns

Patrones conceptuales:

```text
PRIMARY + REVIEWER
PARALLEL ANALYSIS
ADVERSARIAL REVIEW
SPECIALIST MODELS
FALLBACK
CONSENSUS SUPPORT
```

Todos deben conservar mediación y trazabilidad mediante Robert.

---

# 40. Primary + Reviewer

Flujo correcto:

```text
MODEL A
  ↓
PRIMARY OUTPUT
  ↓
MODEL INTERFACE
  ↓
ORCHESTRATOR
  ↓
AUTHORIZED REVIEW CONTEXT
  ↓
MODEL ROUTER
  ↓
MODEL B
  ↓
REVIEW
```

No:

```text
MODEL A
  ↓
MODEL B
```

como comunicación autónoma.

---

# 41. Adversarial Model Review

```text
MODEL A
  ↓
PROPOSAL
  ↓
ROBERT
  ↓
MODEL B
  ↓
CHALLENGE
  ↓
VALIDATION
```

Model B no adquiere autoridad superior.

---

# 42. Model Fallback

Si el Model seleccionado falla:

```text
MODEL FAILURE
    ↓
CLASSIFY
    ↓
FALLBACK ALLOWED?
    ├── YES → MODEL ROUTER
    └── NO → ESCALATE
```

---

# 43. Fallback Rules

Fallback debe considerar:

```text
capability_equivalence
security
context_compatibility
tool_compatibility
structured_output_support
cost
availability
health
```

---

# 44. Fallback Restriction

```text
MODEL FAILURE ≠ USE ANY AVAILABLE MODEL
```

El fallback debe seguir cumpliendo requisitos mínimos.

---

# 45. Provider Failure

Taxonomía conceptual inicial:

```text
TIMEOUT
RATE_LIMIT
AUTH_FAILURE
SERVICE_UNAVAILABLE
INVALID_RESPONSE
CONTEXT_LIMIT
CONTENT_REJECTION
TOOL_FAILURE
UNKNOWN_PROVIDER_ERROR
```

---

# 46. Normalized Errors

Model Interface deberá poder representar:

```text
MODEL_ERROR

error_type
provider_error
retryable
fallback_allowed
details
```

---

# 47. Retry Policy

Una futura política podrá utilizar:

```text
retry_count
retry_delay
same_model_retry
fallback_model
```

pero:

```text
RETRY ≠ AUTONOMOUS UNBOUNDED LOOP
```

Toda política deberá tener límites.

---

# 48. Tool Requests from Models

Un Model puede solicitar una Tool.

Ejemplo:

```text
TOOL_REQUEST:
web_read
```

Pero:

```text
MODEL TOOL REQUEST ≠ TOOL AUTHORIZATION
```

---

# 49. Model Tool Boundary

Flujo:

```text
MODEL
  ↓
TOOL REQUEST
  ↓
MODEL ADAPTER
  ↓
MODEL INTERFACE
  ↓
ORCHESTRATOR
  ↓
TOOL RESOLVER
  ↓
PERMISSION / SCOPE / RISK / APPROVAL
  ↓
TOOL
```

---

# 50. Provider Tool Calling

Una API puede soportar function calling o mecanismos similares.

Aun así:

```text
PROVIDER TOOL CALL
≠
INDEPENDENT TOOL AUTHORITY
```

Robert conserva autorización lógica.

---

# 51. Model Capability ≠ Tool Permission

Un Model puede soportar Tool Calling.

Eso no implica:

```text
MODEL HAS TOOL PERMISSION
```

Regla:

```text
MODEL TOOL CAPABILITY
        ≠
ROBERT TOOL AUTHORIZATION
```

---

# 52. Memory Boundary

Un Model puede producir información potencialmente útil para Memory.

Pero:

```text
MODEL OUTPUT ≠ MEMORY WRITE
```

El output puede convertirse como máximo en candidato para evaluación por la futura Memory Architecture.

---

# 53. Evidence and Sources

Cuando una Task requiera evidencia, Model Interface debe poder preservar:

```text
CLAIM
SOURCE
EVIDENCE
INTERPRETATION
```

alineado con Skill Architecture.

---

# 54. Source Attribution

Si la procedencia no puede verificarse:

```text
SOURCE_STATUS: UNVERIFIED
```

Un Model no puede convertir una fuente inexistente o no verificada en una fuente autoritativa.

---

# 55. Confidence

Un Model puede ofrecer Confidence cuando tenga sentido.

Debe registrarse además:

```text
confidence_source
```

Ejemplos:

```text
MODEL_REPORTED
SYSTEM_DERIVED
VALIDATOR_DERIVED
UNKNOWN
```

Pero:

```text
CONFIDENCE ≠ TRUTH
CONFIDENCE ≠ AUTHORITY
CONFIDENCE ≠ APPROVAL
```

---

# 56. Limitations

Model Response debe poder expresar:

```text
limitations
```

Ejemplos:

```text
missing_context
uncertain_source
knowledge_staleness
model_capability_limit
tool_unavailable
context_limit
```

---

# 57. Assumptions

Los supuestos relevantes deben quedar visibles cuando sea razonable.

```text
assumptions
```

Esto mejora Validation y trazabilidad.

---

# 58. Validation

Model output puede requerir:

```text
RULE_VALIDATION
MODEL_REVIEW
AGENT_REVIEW
SECURITY_REVIEW
SOURCE_VALIDATION
USER_REVIEW
```

La futura `ROBERT_VALIDATION_ARCHITECTURE` formalizará estas políticas.

---

# 59. Model Validation ≠ Authorization

```text
VALID MODEL OUTPUT ≠ AUTHORIZED ACTION
```

Un output puede ser válido y aun así no tener autorización de ejecución.

---

# 60. Security Context

Model Request puede incluir restricciones:

```text
permissions
scope
risk
approval_state
external_effects_allowed
```

Estas restricciones guían al Model.

No convierten al Model en autoridad de seguridad.

---

# 61. Model Cannot Grant Authority

```text
MODEL CANNOT CREATE PERMISSION
MODEL CANNOT EXPAND SCOPE
MODEL CANNOT CREATE AUTONOMY
MODEL CANNOT CREATE EXECUTION AUTHORITY
MODEL CANNOT SELF-APPROVE
```

---

# 62. Minimum Necessary Disclosure

Un Model solo debe recibir Context necesario.

```text
MINIMUM NECESSARY DISCLOSURE
```

Especialmente para:

* Memory;
* datos internos;
* credentials;
* secrets;
* security context;
* personal data.

---

# 63. Sensitive Context

Una política futura deberá clasificar información:

```text
MAY BE SENT
MAY REQUIRE REDACTION
MUST NOT BE SENT
```

según:

```text
MODEL
PROVIDER
TASK
CONTEXT CLASS
PERMISSION
SCOPE
```

---

# 64. Model Registry Example

```yaml
model:
  id:
  provider:
  family:
  version:
  status:

adapter:

capabilities:
  reasoning:
  coding:
  long_context:
  vision:
  structured_output:
  tool_calling:

limits:
  context_window:
  output_limit:

security:
  allowed_context_classes:
```

---

# 65. Model Runtime State Example

```yaml
runtime:
  model_id:
  availability:
  health:
  latency:
  cost_information:
  rate_limit_state:
  last_checked:
```

Este estado es operativo y puede cambiar sin alterar la identidad del Model.

---

# 66. Adapter Manifest

```yaml
adapter:
  id:
  provider:
  version:

supports:
  system_instructions:
  structured_output:
  tool_calling:
  multimodal:

mapping:
  request:
  response:
  errors:
  usage:

tool_boundary:
  authorization: ROBERT
```

---

# 67. Model Request Example

```yaml
request:
  request_id: req_001
  task_id: task_100
  requester: ROBERT_ARCHITECT

purpose:
  architecture_review

task:
  review_memory_architecture

required_capabilities:
  - reasoning

preferred_capabilities:
  - long_context
  - structured_output

context:
  canonical_model:
  related_decisions:
  target_document:

constraints:
  phase: 10

expected_output:
  - findings
  - conflicts
  - recommendations
```

---

# 68. Model Response Example

```yaml
response:
  request_id: req_001

model:
  id:
  provider:
  version:

result:
  findings:
  conflicts:
  recommendations:

rationale_summary:

evidence:

sources:

confidence:

confidence_source:

limitations:

assumptions:

validation_notes:

errors:
```

---

# 69. Model Selection Example

Task:

```text
Review a very large architecture document
```

Requirements:

```text
reasoning
long_context
document_analysis
```

Model Router debe excluir Models incapaces de manejar el Context requerido.

---

# 70. Coding Example

Task:

```text
Review Python implementation
```

Required:

```text
coding
reasoning
```

Preferred:

```text
structured_output
long_context
```

---

# 71. Research Example

Task:

```text
Compare current vector databases
```

Model requirement:

```text
reasoning
```

Skill o Task pueden además requerir:

```text
web_read
```

Pero:

```text
MODEL CAPABILITY ≠ WEB ACCESS
```

---

# 72. Cost Policy

En fases futuras, Model Router podrá considerar Cost.

Ejemplo:

```text
LOW COMPLEXITY
→ lower-cost eligible Model

HIGH IMPACT
→ stronger eligible Model + stronger validation
```

Cost nunca debe ser el único criterio.

---

# 73. Latency Policy

Tasks sensibles a velocidad pueden priorizar Models con menor latencia.

Tasks de mayor impacto pueden priorizar calidad y Validation.

---

# 74. Quality Policy

Quality debe evaluarse por tipo de Task.

Métricas futuras:

```text
task_success
validation_pass_rate
unsupported_claim_rate
user_correction_rate
structured_output_compliance
```

---

# 75. Model Performance History

Una implementación futura podrá conservar:

```text
MODEL
+
TASK TYPE
+
HISTORICAL PERFORMANCE
```

para mejorar routing.

Esto no se convierte automáticamente en Memory semántica.

---

# 76. Model Health

Runtime State podrá usar estados candidatos:

```text
AVAILABLE
DEGRADED
UNAVAILABLE
DISABLED
```

Todavía no constituyen una state machine técnica final.

---

# 77. Model Status vs Authorization

```text
AVAILABLE ≠ AUTHORIZED
```

Un Model puede estar disponible técnicamente y aun así no estar permitido para determinado Context o Task.

---

# 78. Model Version Changes

Una actualización puede cambiar:

* behavior;
* capabilities;
* context window;
* Tool support;
* structured output;
* quality;
* safety characteristics.

Por tanto, debe preservarse `model_version` cuando sea posible.

---

# 79. Version Pinning

Para Tasks reproducibles puede preferirse una versión específica.

No todos los proveedores garantizan version pinning.

Esta limitación deberá poder representarse.

---

# 80. Reproducibility

```text
SAME INPUT
≠
GUARANTEED SAME OUTPUT
```

Incluso con el mismo Model y configuración.

---

# 81. Audit

Una futura interacción debería poder registrar:

```text
request_id
task_id
requester
model_id
model_version
provider
adapter_version
skill_id
context_reference
capabilities_required
selection_reason
response_status
validation_status
tool_requests
errors
usage
duration
```

---

# 82. Observability

Métricas futuras:

```text
model_selection_accuracy
task_success_rate
validation_pass_rate
fallback_rate
provider_error_rate
cost_per_task
latency
context_utilization
structured_output_failure_rate
user_correction_rate
```

---

# 83. Model Comparison

Robert podrá comparar Models mediante Tasks estandarizadas.

```text
STANDARD TEST SET
      ↓
ROBERT
   ├── MODEL A
   └── MODEL B
      ↓
VALIDATION
      ↓
METRICS
```

---

# 84. Benchmark ≠ Universal Truth

```text
BENCHMARK WINNER ≠ BEST MODEL FOR EVERY TASK
```

Los benchmarks deben interpretarse dentro del dominio correspondiente.

---

# 85. Model Specialization

Se permite especialización en:

```text
coding
reasoning
vision
research
speed
cost
long_context
```

Model Router puede aprovechar estas diferencias.

---

# 86. Model Independence Invariant

Agents y Skills deben sobrevivir al reemplazo de Model.

```text
ROBERT_ARCHITECT
      ↓
architecture_review
      ↓
MODEL INTERFACE
      ↓
MODEL A
```

puede pasar a:

```text
MODEL B
```

sin redefinir Agent o Skill.

---

# 87. Provider Independence Invariant

```text
PROVIDER CHANGE
    ≠
AGENT REWRITE
```

y:

```text
PROVIDER CHANGE
    ≠
SKILL REWRITE
```

salvo dependencia intencional explícita.

---

# 88. Model-Specific Features

Una capacidad específica de proveedor puede representarse como metadata:

```text
provider_specific_capability
```

Debe permanecer contenida dentro de Adapter / Model metadata.

No dispersarse por Robert.

---

# 89. Provider-Specific Optimization

Puede existir:

```text
COMMON CONTRACT
      ↓
PROVIDER ADAPTER
      ↓
PROVIDER-SPECIFIC OPTIMIZATION
```

sin romper el contrato común.

---

# 90. Fase 10

Durante Fase 10:

```text
MODEL INTERFACE = DOCUMENTAL
MODEL ROUTER = CONCEPTUAL
MODEL REGISTRY = CONCEPTUAL
MODEL RUNTIME STATE = CONCEPTUAL
MODEL ADAPTERS = DESIGN ONLY
```

Contexto operativo:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

---

# 91. Permitido en Fase 10

Se permite:

* definir contratos;
* diseñar Model Registry;
* diseñar Runtime State;
* diseñar Adapters;
* comparar Models manualmente;
* simular routing;
* crear tests;
* utilizar Claude y ChatGPT manualmente como apoyo;
* diseñar structured outputs;
* probar formatos en Sandbox;
* evaluar capabilities.

---

# 92. No permitido en Fase 10

Esta especificación no autoriza:

* routing autónomo productivo;
* llamadas API persistentes autónomas;
* loops multi-model autónomos;
* Tool execution automática;
* Memory writes automáticos;
* ejecución externa;
* creación autónoma de Permission;
* creación autónoma de Scope;
* creación autónoma de Autonomy;
* creación autónoma de Execution Authority;
* self-modification.

---

# 93. Sandbox Tests futuros

```text
TEST 1
Correct Model selected

TEST 2
Required capability missing

TEST 3
Preferred capability missing

TEST 4
Model unavailable

TEST 5
Fallback successful

TEST 6
Fallback incompatible

TEST 7
Context too large

TEST 8
Invalid structured output

TEST 9
Provider timeout

TEST 10
Rate limit

TEST 11
Model requests unauthorized Tool

TEST 12
Model output conflicts with Canonical Context

TEST 13
Multi-Model disagreement

TEST 14
Consensus produces wrong answer

TEST 15
Model attempts Scope expansion

TEST 16
Adapter changes Task meaning

TEST 17
Sensitive Context rejected

TEST 18
Unknown Model version

TEST 19
Model request without Skill

TEST 20
Adapter attempts direct Tool execution

TEST 21
Primary Model attempts direct Model-to-Model routing

TEST 22
Private reasoning trace required by caller

TEST 23
Available Model but unauthorized Context
```

---

# 94. Security Invariants

```text
MODEL CANNOT CREATE PERMISSIONS
MODEL CANNOT EXPAND SCOPE
MODEL CANNOT SELF-APPROVE
MODEL CANNOT ALTER PHASE
MODEL CANNOT ALTER CANONICAL MODEL
MODEL CANNOT CREATE AUTONOMY
MODEL CANNOT CREATE EXECUTION AUTHORITY

MODEL TOOL REQUEST ≠ TOOL AUTHORIZATION

MODEL OUTPUT ≠ DECISION
MODEL OUTPUT ≠ TRUTH

MODEL USE ≠ SKILL REQUIRED

ADAPTER TOOL SUPPORT ≠ TOOL EXECUTION AUTHORITY

MODEL-TO-MODEL TRANSFER MUST BE MEDIATED BY ROBERT
```

---

# 95. Governance Invariants

```text
USER > MODEL

ROBERT > MODEL

ORCHESTRATOR > MODEL ROUTING

SECURITY > MODEL REQUEST

APPROVED DECISION > MODEL PROPOSAL

VALIDATION > UNVERIFIED MODEL OUTPUT

CONSENSUS ≠ TRUTH

CONSENSUS ≠ AUTHORIZATION

PRIMARY MODEL ≠ ROUTING AUTHORITY

MODEL PREFERENCE ≠ MODEL SELECTION AUTHORITY
```

---

# 96. Dependencia con Memory Architecture

La futura:

```text
ROBERT_MEMORY_ARCHITECTURE
```

deberá definir:

* qué Memory puede entregarse a Models;
* qué información requiere redaction;
* qué outputs pueden convertirse en candidatos de Memory;
* provenance;
* retention;
* conflicts;
* retrieval.

---

# 97. Dependencia con Validation Architecture

La futura:

```text
ROBERT_VALIDATION_ARCHITECTURE
```

deberá definir:

* cuándo validar;
* quién valida;
* cómo comparar Model outputs;
* thresholds;
* evidence requirements;
* failure behavior;
* confidence handling.

---

# 98. Dependencia con Tool Architecture

La integración futura de Tool Calling deberá mantener:

```text
MODEL REQUESTS TOOL
        ↓
ROBERT AUTHORIZES TOOL
```

Nunca:

```text
MODEL SUPPORTS TOOL
        ↓
TOOL AUTOMATICALLY AUTHORIZED
```

---

# 99. Decisiones pendientes antes de v1.0

Quedan pendientes:

1. Model Registry técnico final;
2. Capability Taxonomy final;
3. Model Request schema técnico;
4. Model Response schema técnico;
5. Adapter interface;
6. Runtime State técnico;
7. error taxonomy final;
8. retry policy;
9. fallback policy;
10. ranking algorithm;
11. cost policy;
12. latency policy;
13. health policy;
14. context packaging;
15. sensitive Context rules;
16. multimodal interface;
17. Tool Calling interface;
18. provider-specific optimizations;
19. benchmarking methodology;
20. Model version policy;
21. observability implementation;
22. Confidence normalization.

---

# 100. Estado actual

```text
DOCUMENT: ROBERT_MODEL_INTERFACE_SPEC
VERSION: 0.1
STATUS: APPROVED
AUTHORITY: ARCHITECTURAL
DECISION: #034
CHANGE: #059
PHASE: 10
IMPLEMENTATION: NONE
OPERATIONAL_AUTONOMY: 0
OPERATIONAL_EXECUTION_AUTHORITY: NONE
```

---

# 101. Decisión arquitectónica

`ROBERT_MODEL_INTERFACE_SPEC v0.1` queda aprobado bajo los siguientes principios centrales:

```text
MODEL ≠ AGENT
MODEL ≠ SKILL
MODEL ≠ TOOL

MODEL USE ≠ SKILL REQUIRED

MODEL OUTPUT ≠ DECISION
MODEL OUTPUT ≠ TRUTH

MODEL TOOL CAPABILITY ≠ TOOL AUTHORIZATION

MODEL-TO-MODEL TRANSFER
MUST BE MEDIATED BY ROBERT

RATIONALE SUMMARY ≠ PRIVATE REASONING TRACE

PROVIDER CHANGE ≠ AGENT REWRITE
PROVIDER CHANGE ≠ SKILL REWRITE
```

---

# 102. Próximo paso

Después de registrar formalmente:

```text
DECISIÓN #034
CAMBIO #059
```

el siguiente bloque arquitectónico será:

```text
ROBERT_MEMORY_ARCHITECTURE v0.1
```

Su objetivo será definir cómo Robert:

```text
STORES
RETRIEVES
CLASSIFIES
VALIDATES
UPDATES
EXPIRES
CONFLICT-RESOLVES
GOVERNS
```

Memory, manteniendo separadas:

```text
CONTEXT
MEMORY
SOURCE
MODEL OUTPUT
PROPOSAL
DECISION
```
