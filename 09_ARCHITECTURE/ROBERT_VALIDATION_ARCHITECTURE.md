# ROBERT_VALIDATION_ARCHITECTURE

**Versión:** 0.1
**Estado:** PROPUESTA — pendiente de revisión y aprobación
**Tipo:** Especificación arquitectónica de Validation
**Ubicación propuesta:** `09_ARCHITECTURE/ROBERT_VALIDATION_ARCHITECTURE.md`
**Fase relacionada:** Fase 10 — MVP técnico básico en preparación

**Dependencias principales:**

* `ROBERT_CANONICAL_MODEL v0.2`
* `ROBERT_ORCHESTRATOR_SPEC v0.1`
* `ROBERT_AGENT_ARCHITECTURE v0.1`
* `ROBERT_SKILL_ARCHITECTURE v0.1`
* `ROBERT_MODEL_INTERFACE_SPEC v0.1`
* `ROBERT_MEMORY_ARCHITECTURE v0.1`
* `ROBERT_SYSTEM_ARCHITECTURE`
* `ROBERT_CONTEXT_MASTER`
* `ROBERT_SECURITY_RULES`
* `ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC v0.2`
* `ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC v0.2`
* `ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC v0.3`
* `ROBERT_TECHNICAL_APPROVAL_AND_AUTHORIZATION_GATE_SPEC v0.3`

---

# 1. Propósito

`ROBERT_VALIDATION_ARCHITECTURE` define cómo Robert deberá evaluar si un output, claim, proposal, result, evidence package, memory candidate o artifact cumple los requisitos aplicables antes de ser utilizado para continuar una Task.

Validation busca responder:

```text
IS THIS OUTPUT ACCEPTABLE
FOR THIS PURPOSE
UNDER THESE REQUIREMENTS?
```

Validation no responde automáticamente:

```text
IS THIS TRUE?
IS THIS AUTHORIZED?
IS THIS APPROVED?
MAY THIS BE EXECUTED?
```

---

# 2. Definición de Validation

Validation es el proceso de comprobar un resultado contra criterios definidos.

Puede verificar:

```text
FORMAT
COMPLETENESS
CONSISTENCY
CANONICAL COMPLIANCE
SECURITY
EVIDENCE
SOURCES
CONSTRAINTS
TASK REQUIREMENTS
MEMORY RULES
```

según el caso.

---

# 3. Regla fundamental

Se formaliza:

```text
VALIDATION ≠ AUTHORIZATION

VALIDATION ≠ APPROVAL

VALIDATION ≠ EXECUTION AUTHORITY

VALIDATION ≠ TRUTH
```

Un output validado puede seguir necesitando:

```text
APPROVAL
PERMISSION
SCOPE
SECURITY CHECK
USER DECISION
```

---

# 4. Posición arquitectónica

Flujo conceptual:

```text
TASK
  ↓
ORCHESTRATOR
  ↓
AGENT / SKILL / MODEL / TOOL
  ↓
OUTPUT
  ↓
VALIDATION REQUIRED?
  ├── NO → CONTINUE
  └── YES
       ↓
     VALIDATION RESOLUTION
       ↓
     VALIDATION
       ↓
     VALIDATION RESULT
       ↓
     ORCHESTRATOR
```

Validation no reemplaza al Orchestrator.

---

# 5. Validation Responsibility

Se propone conceptualmente:

```text
VALIDATION RESOLVER
```

como responsabilidad especializada bajo el Orchestrator.

Su función será determinar:

```text
whether validation is required
what validation types are required
what criteria apply
what reviewer capability is needed
whether multiple validations are needed
what result is sufficient
```

---

# 6. Architectural Growth Check — Validation Resolver

```text
WHY NEEDED:
Centralizar la selección de Validation sin distribuir authority
entre Agents, Skills, Models y futuros Validators.

EXISTING COMPONENT IT EXTENDS:
ROBERT_ORCHESTRATOR.

NEW AUTHORITY CREATED?:
NO.

NEW TECHNICAL MODEL CREATED?:
NO.

PHASE 10 COMPATIBLE?:
YES — conceptual, documental, manual y supervisado.

APPROVAL REQUIRED?:
YES — como parte de ROBERT_VALIDATION_ARCHITECTURE v0.1.
```

Por tanto:

```text
VALIDATION RESOLVER ≠ ORCHESTRATOR

VALIDATION RESOLVER ≠ APPROVAL AUTHORITY
```

---

# 7. Validator

`Validator` se utiliza en esta arquitectura como:

```text
FUNCTIONAL VALIDATION ROLE
```

No se crea una nueva categoría canónica de primer nivel.

```text
VALIDATOR ≠ NEW CANONICAL ENTITY TYPE
```

La función de Validator puede ser cumplida, según el caso, por:

```text
RULE SYSTEM
AGENT
MODEL
SECURITY FUNCTION
USER
AUTHORIZED ROBERT COMPONENT
```

---

# 8. Validator ≠ Authority

```text
VALIDATOR ≠ DECISION MAKER

VALIDATOR ≠ ROUTING AUTHORITY

VALIDATOR ≠ APPROVAL AUTHORITY

VALIDATOR ≠ EXECUTION AUTHORITY
```

Validator evalúa.

No gobierna Robert.

---

# 9. Validation Request

Contrato conceptual:

```text
VALIDATION_REQUEST

validation_id
task_id
requester
target
target_type
purpose
validation_types
criteria
constraints
expected_output
evidence_requirements
source_requirements
canonical_requirements
security_requirements
risk_context
permission_context
scope_context
```

---

# 10. Validation Result

Contrato conceptual:

```text
VALIDATION_RESULT

validation_id
target_id
status
findings
passed_checks
failed_checks
warnings
conflicts
evidence
sources
confidence
limitations
required_corrections
escalation
recommended_next_step
```

---

# 11. Validation Status

Estados conceptuales:

```text
PASS
PASS_WITH_WARNINGS
FAIL
BLOCKED
INCONCLUSIVE
NOT_APPLICABLE
```

Estos valores no constituyen todavía una state machine técnica oficial.

---

# 12. PASS

`PASS` significa que el target cumple los criterios de Validation definidos para ese caso.

No significa:

```text
APPROVED
AUTHORIZED
TRUE
SAFE FOR EXECUTION
```

---

# 13. PASS WITH WARNINGS

`PASS_WITH_WARNINGS` indica que el target cumple los criterios mínimos pero existen observaciones no bloqueantes.

Ejemplos:

```text
minor incompleteness
low-impact ambiguity
optional improvement
non-critical uncertainty
```

---

# 14. FAIL

`FAIL` significa que uno o más criterios obligatorios no se cumplen.

Debe producir:

```text
failed_checks
reason
required_corrections
```

cuando sea posible.

---

# 15. BLOCKED

`BLOCKED` significa que Validation no puede continuar o que debe detener el flujo debido a:

```text
security issue
permission issue
scope issue
critical conflict
missing required evidence
missing required context
phase violation
```

---

# 16. INCONCLUSIVE

`INCONCLUSIVE` se utiliza cuando no existe evidencia suficiente para aprobar o rechazar el target.

```text
INCONCLUSIVE ≠ FAIL
INCONCLUSIVE ≠ PASS
```

---

# 17. Validation Dimensions

Validation utiliza dos dimensiones conceptuales separadas:

```text
VALIDATION_TYPE
```

y:

```text
REVIEWER_ROLE
```

Se formaliza:

```text
VALIDATION_TYPE ≠ REVIEWER_ROLE
```

`VALIDATION_TYPE` define **qué se verifica**.

`REVIEWER_ROLE` define **quién o qué realiza la verificación**.

Estas dimensiones pueden combinarse según la Task.

Ejemplo:

```text
VALIDATION_TYPE: SECURITY
REVIEWER_ROLE: AGENT
```

o:

```text
VALIDATION_TYPE: STRUCTURE
REVIEWER_ROLE: RULE_SYSTEM
```

---

## 17.1 Validation Type

Tipos conceptuales iniciales:

```text
RULE
CANONICAL
STRUCTURE
COMPLETENESS
CONSISTENCY
EVIDENCE
SOURCE
SECURITY
SCOPE
PERMISSION
MEMORY
MODEL_OUTPUT
```

Estos valores representan el objeto o criterio principal de Validation.

No identifican al reviewer.

---

## 17.2 Reviewer Role

Roles conceptuales iniciales:

```text
RULE_SYSTEM
AGENT
MODEL
USER
AUTHORIZED ROBERT FUNCTION
```

`REVIEWER_ROLE` no crea una nueva categoría canónica de entidad.

Describe la capacidad funcional utilizada para realizar Validation.

Por tanto:

```text
REVIEWER_ROLE ≠ NEW CANONICAL ENTITY TYPE
```

y:

```text
REVIEWER_ROLE ≠ ROUTING AUTHORITY
```

El Orchestrator continúa resolviendo qué capacidad concreta realizará la Validation.

---

## 17.3 Combination Rule

Una Validation puede combinar ambas dimensiones:

```text
VALIDATION REQUEST
│
├── VALIDATION_TYPE
└── REVIEWER_ROLE
```

Ejemplo:

```text
validation_type:
CANONICAL

reviewer_role:
AGENT
```

El Agent concreto será seleccionado mediante routing autorizado.

Otro ejemplo:

```text
validation_type:
STRUCTURE

reviewer_role:
RULE_SYSTEM
```

La arquitectura no debe inferir el reviewer únicamente a partir del Validation Type.

# 18. Rule Validation

`RULE_VALIDATION` verifica reglas deterministas o claramente definidas.

Ejemplos:

```text
required fields present
format correct
forbidden value absent
phase field valid
version present
```

---

# 19. Canonical Validation

Verifica alineación con:

```text
ROBERT_CANONICAL_MODEL
APPROVED ARCHITECTURE
APPROVED DECISIONS
SECURITY RULES
```

Regla:

```text
CANONICAL VALIDATION
DOES NOT MODIFY
CANONICAL SOURCE
```

---

# 20. Structure Validation

Verifica que un artifact tenga la estructura requerida.

Ejemplo:

```text
required sections
required metadata
required fields
expected organization
```

---

# 21. Completeness Validation

Comprueba si falta información necesaria.

Ejemplos:

```text
missing requirement
missing source
missing limitation
missing risk
missing decision reference
```

---

# 22. Consistency Validation

Comprueba coherencia interna y externa.

Debe apoyarse en:

```text
ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC
```

No crea un sistema paralelo de precedencia.

```text
VALIDATION CONSISTENCY CHECK
≠
GLOBAL CONFLICT AUTHORITY
```

---

# 23. Evidence Validation

Comprueba si la evidencia soporta suficientemente los claims relevantes.

Se mantienen:

```text
SOURCE ≠ CLAIM

CLAIM ≠ EVIDENCE

EVIDENCE ≠ INTERPRETATION
```

---

# 24. Source Validation

Puede evaluar:

```text
identity
provenance
authority
freshness
relevance
independence
reliability
```

cuando corresponda.

Pero:

```text
SOURCE VALIDATION ≠ SOURCE IS TRUE
```

---

# 25. Security Validation

Comprueba que el target no viole:

```text
SECURITY RULES
PHASE
SENSITIVE DATA RULES
EXTERNAL ACTION RESTRICTIONS
```

Security Validation puede bloquear.

Pero no puede conceder autorización.

---

# 26. Permission Validation

Comprueba si existe Permission suficiente.

Debe reutilizar:

```text
ROBERT_TECHNICAL_PERMISSIONS_AND_SCOPES_SPEC
```

```text
PERMISSION VALIDATION ≠ PERMISSION CREATION
```

---

# 27. Scope Validation

Comprueba si una operación permanece dentro del Scope autorizado.

```text
SCOPE VALIDATION ≠ SCOPE EXPANSION
```

---

# 28. Memory Validation

Puede evaluar:

```text
memory eligibility
memory type
retention
provenance
freshness
duplicates
conflicts
sensitivity
retrieval suitability
```

según `ROBERT_MEMORY_ARCHITECTURE`.

---

# 29. Memory Validation Boundary

```text
VALID MEMORY CANDIDATE ≠ MEMORY WRITE AUTHORIZATION
```

y:

```text
VALID RETRIEVAL RESULT ≠ UNIVERSAL TRUTH
```

---

# 30. Model Output Validation

Model output puede requerir comprobaciones de:

```text
format
task compliance
evidence
claims
limitations
canonical conflicts
scope
tool requests
```

---

# 31. Agent Review

Un Agent especializado puede revisar output de otro actor.

Ejemplo:

```text
ROBERT_ARCHITECT
  ↓
proposal
  ↓
ROBERT_CRITIC
  ↓
review
```

siempre mediado por Orchestrator.

---

# 32. Agent Review Boundary

```text
AGENT REVIEW ≠ APPROVAL

AGENT REVIEW ≠ ROUTING AUTHORITY

AGENT REVIEW ≠ FINAL TRUTH
```

---

# 33. Model Review

Un Model puede revisar output producido por:

```text
another Model
Agent
Skill
document
```

según routing autorizado.

---

# 34. Model Review Boundary

```text
MODEL REVIEW ≠ APPROVAL

MODEL REVIEW ≠ TRUTH

MODEL REVIEW ≠ AUTHORIZATION
```

---

# 35. Self Validation

Un Agent, Skill procedure o Model puede realizar una comprobación inicial de su propio output.

Pero:

```text
SELF VALIDATION ≠ INDEPENDENT VALIDATION
```

Cuando el impacto lo requiera, deberá existir un reviewer separado.

---

# 36. User Review

El usuario puede actuar como reviewer final.

Especialmente cuando:

```text
subjective preference
high-impact decision
architectural approval
tradeoff requires human judgment
```

---

# 37. User Review ≠ Automatic Decision

Incluso User Review debe distinguir:

```text
REVIEW
```

de:

```text
APPROVAL
```

La aprobación debe ser explícita cuando las reglas la exijan.

---

# 38. Validation Criteria

Cada Validation debe identificar criterios concretos.

Ejemplos:

```text
criterion_id
description
required
validation_method
expected_result
severity_if_failed
```

---

# 39. Required vs Optional Criteria

Se distingue:

```text
REQUIRED
OPTIONAL
```

Un criterio obligatorio fallido puede producir:

```text
FAIL
BLOCKED
```

Un criterio opcional fallido puede producir:

```text
PASS_WITH_WARNINGS
```

---

# 40. Severity

Hallazgos pueden clasificarse conceptualmente como:

```text
BLOCKING
IMPORTANT
OPTIONAL
FUTURE
```

Esto describe importancia de corrección.

No reemplaza Risk.

```text
VALIDATION SEVERITY ≠ SYSTEM RISK LEVEL
```

---

# 41. Validation Evidence

Validation debe conservar evidencia cuando sea útil.

Ejemplo:

```text
finding
criterion
evidence
source
reason
```

---

# 42. Evidence ≠ Validation Result

```text
EVIDENCE ≠ VALIDATION RESULT
```

Evidence soporta el resultado.

No es el resultado mismo.

---

# 43. Confidence

Validation puede reportar Confidence.

Ejemplo:

```text
confidence: 0.91
```

Pero:

```text
CONFIDENCE ≠ TRUTH

CONFIDENCE ≠ AUTHORITY

CONFIDENCE ≠ APPROVAL
```

---

# 44. Confidence Source

Metadata conceptual posible:

```text
RULE_DERIVED
MODEL_REPORTED
AGENT_DERIVED
USER_REPORTED
SYSTEM_DERIVED
UNKNOWN
```

---

# 45. Validation Depth

Puede existir profundidad conceptual:

```text
BASIC
STANDARD
DEEP
ADVERSARIAL
```

La taxonomía definitiva queda pendiente.

---

# 46. Basic Validation

Ejemplos:

```text
format
required fields
simple rules
```

---

# 47. Standard Validation

Puede combinar:

```text
structure
completeness
consistency
task requirements
```

---

# 48. Deep Validation

Puede incluir:

```text
canonical comparison
evidence review
source review
risk-sensitive analysis
cross-document consistency
```

---

# 49. Adversarial Validation

Busca activamente fallos.

Ejemplos:

```text
counterexamples
edge cases
authority leakage
routing bypass
scope expansion
hidden assumptions
```

---

# 50. Validation Depth ≠ Authority

```text
DEEP VALIDATION ≠ HIGHER AUTHORITY

ADVERSARIAL VALIDATION ≠ FINAL DECISION
```

---

# 51. Validation Routing

Flujo conceptual:

```text
OUTPUT
  ↓
VALIDATION REQUIREMENT
  ↓
ORCHESTRATOR
  ↓
VALIDATION RESOLVER
  ↓
VALIDATION CAPABILITY
  ↓
RESULT
```

---

# 52. Validation Capability Request

El Validation Resolver puede producir una necesidad de capacidad como:

```text
canonical compliance
security review
source validation
adversarial review
```

El Orchestrator resuelve quién o qué realiza esa capacidad.

---

# 53. Validation Request ≠ Direct Invocation

```text
VALIDATION REQUEST ≠ DIRECT MODEL INVOCATION

VALIDATION REQUEST ≠ DIRECT AGENT INVOCATION

VALIDATION REQUEST ≠ DIRECT TOOL INVOCATION
```

---

# 54. Multi-Validator Review

Una Task puede utilizar más de un reviewer.

Ejemplo:

```text
MODEL REVIEW
+
SECURITY REVIEW
+
RULE VALIDATION
```

---

# 55. Multi-Validator Consensus

Se mantiene:

```text
CONSENSUS ≠ TRUTH

CONSENSUS ≠ AUTHORIZATION

MAJORITY ≠ AUTOMATIC WINNER
```

---

# 56. Validator Conflict

Dos Validators pueden discrepar.

Ejemplo:

```text
VALIDATOR A → PASS
VALIDATOR B → FAIL
```

Resultado:

```text
VALIDATION CONFLICT
```

---

# 57. Validation Conflict Resolution

Flujo:

```text
VALIDATION CONFLICT
      ↓
ORCHESTRATOR
      ↓
CLASSIFY CONFLICT
      ↓
COMPARE CRITERIA
      ↓
COMPARE EVIDENCE
      ↓
COMPARE AUTHORITY / ROLE
      ↓
CAN RESOLVE?
   ├── YES → RESOLVE
   └── NO → ESCALATE
```

---

# 58. Validation Conflict ≠ Majority Vote

```text
MORE VALIDATORS
≠
CORRECT RESULT
```

Debe analizarse por criterios y evidencia.

---

# 59. Validation vs Approval

Flujo correcto:

```text
OUTPUT
  ↓
VALIDATION
  ↓
PASS
  ↓
APPROVAL REQUIRED?
  ├── NO → CONTINUE
  └── YES → APPROVAL GATE
```

No:

```text
VALIDATION PASS
  ↓
AUTOMATIC APPROVAL
```

---

# 60. Validation vs Authorization

```text
VALIDATION
checks acceptability
```

```text
AUTHORIZATION
checks whether action may proceed
```

Son responsabilidades diferentes.

---

# 61. Validation vs Decision

Una Validation puede recomendar:

```text
APPROVE
CORRECT
REJECT
ESCALATE
```

Pero:

```text
VALIDATION RECOMMENDATION ≠ DECISION
```

---

# 62. Validation vs Truth

Validation comprueba criterios.

No garantiza verdad universal.

```text
VALIDATED CLAIM ≠ ABSOLUTE TRUTH
```

---

# 63. Validation and Models

Models utilizados para Validation deben seguir:

```text
MODEL ROUTER
MODEL INTERFACE
MODEL ADAPTER
```

según arquitectura vigente.

---

# 64. Validation Model Independence

Preferencia:

```text
VALIDATION CAPABILITY
  ↓
MODEL ROUTER
  ↓
MODEL INTERFACE
  ↓
MODEL
```

No:

```text
VALIDATION
  ↓
CLAUDE-SPECIFIC REVIEW
```

salvo excepción documentada.

---

# 65. Validation and Tools

Validation puede requerir Tools.

Ejemplos:

```text
web
documents
filesystem read
test runner
```

Pero:

```text
VALIDATION TOOL REQUIREMENT ≠ TOOL AUTHORIZATION
```

---

# 66. Validation and Memory

Validation puede utilizar Memory recuperada.

Pero:

```text
MEMORY ≠ VALIDATION AUTHORITY
```

Memory debe entrar como Context autorizado.

---

# 67. Validation Memory Flow

```text
VALIDATION
  ↓
MEMORY NEEDED?
  ↓
ORCHESTRATOR
  ↓
MEMORY RESOLVER
  ↓
AUTHORIZED MEMORY CONTEXT
  ↓
VALIDATOR
```

---

# 68. Validation Output and Memory

Se mantiene:

```text
VALIDATION RESULT ≠ MEMORY WRITE
```

Validation puede producir:

```text
MEMORY CANDIDATE
```

si corresponde.

---

# 69. Validation and Security

Security puede requerir Validation especializada.

Ejemplos:

```text
permission analysis
scope analysis
data exposure
tool request review
external action review
```

---

# 70. Security Validation ≠ Security Override

```text
SECURITY VALIDATOR
CANNOT
LOWER SECURITY POLICY
```

sin gobernanza formal.

---

# 71. Validation and Risk

Validation puede detectar Risk.

Pero:

```text
VALIDATION RESULT ≠ RISK AUTHORITY

RISK ≠ VALIDATION STATUS
```

Un output puede:

```text
PASS VALIDATION
+
HIGH RISK
```

---

# 72. Validation and Permission

Un output puede validar correctamente y seguir sin Permission.

```text
PASS
+
PERMISSION MISSING
=
DO NOT EXECUTE
```

---

# 73. Validation and Scope

```text
PASS
+
SCOPE EXCEEDED
=
BLOCK / ESCALATE
```

---

# 74. Validation and Execution Authority

```text
VALIDATED ACTION
≠
EXECUTION AUTHORITY
```

Durante Fase 10:

```text
EXECUTION_AUTHORITY = NONE
```

---

# 75. Validation and Audit

Validation deberá reutilizar:

```text
ROBERT_TECHNICAL_AUDIT_TRAIL_SPEC
```

No crea un sistema paralelo llamado:

```text
ValidationAuditRecord
ValidationAuditTrail
```

---

# 76. Auditable Validation Information

Futuras Validation operations podrán registrar:

```text
validation_id
target
criteria
validator_type
models_used
agents_used
tools_used
evidence
sources
result
warnings
failures
confidence
escalation
```

---

# 77. Validation Audit Requirement ≠ New Audit System

```text
VALIDATION AUDIT REQUIREMENT
        ≠
NEW AUDIT SYSTEM
```

---

# 78. Validation Failure

Posibles fallos:

```text
MISSING_INPUT
MISSING_CONTEXT
MISSING_CRITERIA
MODEL_FAILURE
TOOL_FAILURE
SOURCE_FAILURE
EVIDENCE_INSUFFICIENT
PERMISSION_DENIED
SCOPE_VIOLATION
SECURITY_BLOCK
CONFLICT_UNRESOLVED
VALIDATOR_UNAVAILABLE
INVALID_VALIDATION_RESULT
```

---

# 79. Validation Failure Handling

```text
VALIDATION FAILURE
      ↓
CLASSIFY
      ↓
CAN RETRY?
  ├── YES → CONTROLLED RETRY
  └── NO
       ↓
FALLBACK / ESCALATE / BLOCK
```

---

# 80. Retry

Retry debe ser:

```text
BOUNDED
JUSTIFIED
TRACEABLE
```

```text
RETRY ≠ AUTONOMOUS UNBOUNDED LOOP
```

---

# 81. Fallback

Fallback puede utilizar:

```text
alternative Model
alternative Agent
Rule Validation
User Review
```

siempre mediante Orchestrator.

---

# 82. Validation Fallback ≠ Routing Authority

```text
FALLBACK RECOMMENDATION ≠ FALLBACK ROUTING AUTHORITY
```

---

# 83. Missing Evidence

Cuando un criterio requiera Evidence y no exista:

```text
EVIDENCE_INSUFFICIENT
```

No se debe inventar soporte.

---

# 84. Missing Source

```text
SOURCE MISSING ≠ SOURCE ASSUMED
```

---

# 85. Unknown

Validation debe poder devolver:

```text
UNKNOWN
INCONCLUSIVE
NOT ENOUGH EVIDENCE
```

cuando corresponda.

---

# 86. Validation of Proposals

Proposal puede validarse respecto a:

```text
consistency
completeness
security
architecture
evidence
scope
```

Pero:

```text
VALID PROPOSAL ≠ APPROVED DECISION
```

---

# 87. Validation of Decisions

Una Decision registrada puede validarse documentalmente respecto a:

```text
existence
format
references
change linkage
consistency
```

Validation no puede cambiar la Decision.

---

# 88. Validation of Changes

Un Change puede validarse respecto a:

```text
decision linkage
document effect
scope
consistency
auditability
```

---

# 89. Validation of Memory Candidates

Puede verificar:

```text
eligibility
duplicate
conflict
retention
type
scope
sensitivity
provenance
```

---

# 90. Validation of Model Requests

Puede verificar:

```text
required capabilities
context limits
scope
permissions
sensitive context
tool requirements
```

antes de Model invocation cuando corresponda.

---

# 91. Validation of Model Responses

Puede verificar:

```text
schema
task adherence
evidence
citations
limitations
tool requests
canonical conflicts
```

---

# 92. Validation of Agent Outputs

Puede verificar:

```text
task fit
Agent scope
skills used
unsupported authority claims
handoff requirements
risks
conflicts
```

---

# 93. Validation of Skill Outputs

Puede verificar:

```text
procedure compliance
preconditions
postconditions
evidence
limitations
output contract
```

---

# 94. Validation of Tool Results

Puede verificar:

```text
expected result
error status
source
scope
data integrity
```

cuando corresponda.

---

# 95. Validation Policy

Se propone conceptualmente:

```text
VALIDATION POLICY
```

como conjunto de reglas que determinan cuándo y cómo validar.

No constituye un nuevo actor.

---

# 96. Architectural Growth Check — Validation Policy

```text
WHY NEEDED:
Centralizar reglas declarativas para Validation.

EXISTING COMPONENT IT EXTENDS:
ROBERT_ORCHESTRATOR + Security + approved architecture.

NEW AUTHORITY CREATED?:
NO.

NEW TECHNICAL MODEL CREATED?:
NO.

PHASE 10 COMPATIBLE?:
YES.

APPROVAL REQUIRED?:
YES — como parte de esta arquitectura.
```

---

# 97. Validation Policy Factors

Puede considerar:

```text
task_type
target_type
impact
risk
canonical_effect
external_effect
memory_effect
evidence_requirements
security_requirements
```

---

# 98. Validation Required?

Ejemplos donde Validation puede ser obligatoria:

```text
canonical change proposal
security change
memory write candidate
external action proposal
high-impact technical artifact
multi-model disagreement
document approval candidate
```

---

# 99. Validation Optional?

Puede ser opcional para:

```text
simple informational outputs
low-impact transformations
formatting-only results
```

si no existe otra regla que lo exija.

---

# 100. Validation Matrix

La siguiente tabla es ilustrativa.

No constituye una `Validation Policy` vinculante ni establece requisitos técnicos definitivos.

```text
VALIDATION MATRIX EXAMPLE
        ≠
APPROVED VALIDATION POLICY
```

Los criterios obligatorios definitivos permanecen pendientes dentro de las decisiones previas a v1.0, incluyendo:

```text
Validation Policy final
criterios de obligatoriedad
human review thresholds
multi-validator policy
```


Ejemplo conceptual:

| Target                      | Validation mínima                     |
| --------------------------- | ------------------------------------- |
| Informational answer        | Optional / Basic                      |
| Architecture proposal       | Canonical + Consistency               |
| Security proposal           | Security + Canonical                  |
| Memory candidate            | Memory + Conflict                     |
| Model output with sources   | Evidence + Source                     |
| External action proposal    | Permission + Scope + Security         |
| Document approval candidate | Canonical + Consistency + User Review |

---

# 101. Validation Manifest

Formato conceptual:

```yaml
validation:
  id:
  purpose:
  target_type:
  status:

criteria:
  required:
  optional:

types:

context_requirements:

evidence_requirements:

source_requirements:

canonical_requirements:

security_requirements:

permission_requirements:

scope_requirements:

review:
  depth:
  capabilities:

result:
  allowed_statuses:

escalation:

audit:
```

Este manifest es conceptual.

No constituye un schema técnico definitivo.

```text
VALIDATION MANIFEST ≠ TECHNICAL VALIDATION SCHEMA
```

---

# 102. Validation Registry

Puede ser útil mantener conceptualmente un catálogo de Validation capabilities.

Ejemplos:

```text
canonical_compliance_check
consistency_check
evidence_validation
source_validation
security_review
completeness_check
```

---

# 103. Validation Registry Boundary

Durante Fase 10:

```text
VALIDATION REGISTRY = CONCEPTUAL / DOCUMENTAL
```

No se crea automáticamente un componente técnico nuevo.

---
# 103.1 Architectural Growth Check — Validation Registry

```text
WHY NEEDED:
Mantener un catálogo documental de capacidades de Validation
y evitar definiciones duplicadas.

EXISTING COMPONENT IT EXTENDS:
ROBERT_SKILL_REGISTRY / Validation Architecture documentation.

NEW AUTHORITY CREATED?:
NO.

NEW TECHNICAL MODEL CREATED?:
NO.

PHASE 10 COMPATIBLE?:
YES — conceptual and documental only.

APPROVAL REQUIRED?:
YES — as part of ROBERT_VALIDATION_ARCHITECTURE v0.1.
```

El Validation Registry no selecciona reviewers ni ejecuta Validation.

```text
VALIDATION REGISTRY ≠ VALIDATION RESOLVER

VALIDATION REGISTRY ≠ ROUTING AUTHORITY

VALIDATION REGISTRY ≠ EXECUTION ENGINE
```

Cuando una capacidad de Validation ya exista como Skill registrada, deberá reutilizarse en lugar de duplicarse.

Principio:

```text
REUSE EXISTING SKILL
BEFORE
CREATE NEW VALIDATION CAPABILITY
```


# 104. Existing Skill Reuse

Validation debe reutilizar Skills ya propuestas cuando sea posible.

Ejemplos:

```text
canonical_compliance_check
evidence_validation
consistency_check
completeness_check
security_review
source_validation
```

---

# 105. Validation ≠ Duplicate Skill System

```text
VALIDATION ARCHITECTURE
≠
SECOND SKILL ARCHITECTURE
```

Validation define cuándo y bajo qué criterios validar.

Skill Architecture define procedimientos reutilizables.

---

# 106. Existing Agent Reuse

Puede utilizar:

```text
ROBERT_CRITIC
ROBERT_SECURITY
ROBERT_TESTER
ROBERT_ARCHITECT
ROBERT_RESEARCHER
ROBERT_MEMORY
```

según la capacidad necesaria.

---

# 107. No New Validator Agent by Default

Esta v0.1 no crea automáticamente:

```text
ROBERT_VALIDATOR
```

como Agent nuevo.

Primero debe comprobarse si la función puede resolverse mediante:

```text
existing Agents
Validation Skills
Rule Validation
Model Review
User Review
```

---

# 108. Validation Independence

Preferencia:

```text
VALIDATION REQUIREMENT
  ↓
CAPABILITY
  ↓
AUTHORIZED RESOLUTION
```

No:

```text
VALIDATION
  ↓
SINGLE HARDCODED PROVIDER
```

---

# 109. Validation Consistency

Validation debe ser reproducible cuando sea razonablemente posible.

Mismos:

```text
target
criteria
context
rules
```

deberían producir resultados comparables.

---

# 110. Deterministic vs Judgment Validation

Se distingue entre:

```text
DETERMINISTIC VALIDATION
```

y:

```text
JUDGMENT-BASED VALIDATION
```

---

# 111. Deterministic Validation

Ejemplos:

```text
schema check
required field check
exact policy rule
format validation
```

---

# 112. Judgment-Based Validation

Ejemplos:

```text
architecture quality
source reliability
argument strength
tradeoff quality
```

Debe reportar limitaciones y Confidence cuando sea útil.

---

# 113. Human-in-the-Loop

Cuando Validation dependa de valores, preferencias o decisiones no resolubles técnicamente:

```text
USER REVIEW REQUIRED
```

---

# 114. High Impact Validation

Para outputs de alto impacto puede requerirse:

```text
MULTIPLE VALIDATION TYPES
+
USER REVIEW
```

---

# 115. Validation Escalation

Debe escalar cuando exista:

```text
conflict unresolved
evidence insufficient
security concern
permission missing
scope exceeded
canonical contradiction
high uncertainty
validator disagreement
user judgment required
```

---

# 116. Escalation Flow

```text
VALIDATION
  ↓
ESCALATE
  ↓
ORCHESTRATOR
  ↓
USER / SECURITY / AUTHORIZED REVIEW
```

---

# 117. Security Invariants

Validation nunca puede:

```text
CREATE PERMISSION
EXPAND SCOPE
CREATE AUTONOMY
CREATE EXECUTION AUTHORITY
SELF-APPROVE
BYPASS ORCHESTRATOR
ALTER PHASE
ALTER CANONICAL MODEL
EXECUTE TOOL DIRECTLY
WRITE MEMORY DIRECTLY
HIDE FAILED CHECKS
TURN CONSENSUS INTO AUTHORIZATION
```

---

# 118. Governance Invariants

```text
USER > VALIDATION RESULT

ROBERT > VALIDATOR

ORCHESTRATOR ROUTING > VALIDATOR REQUEST

SECURITY > VALIDATION CONVENIENCE

APPROVED DECISION > VALIDATION RECOMMENDATION

VALIDATION ≠ AUTHORIZATION

VALIDATION ≠ APPROVAL

VALIDATION ≠ EXECUTION AUTHORITY

VALIDATED OUTPUT ≠ AUTHORIZED ACTION

CONSENSUS ≠ TRUTH

CONFIDENCE ≠ TRUTH
```

---

# 119. Fase 10

Durante Fase 10:

```text
VALIDATION ARCHITECTURE = DOCUMENTAL
VALIDATION RESOLVER = CONCEPTUAL
VALIDATION POLICY = CONCEPTUAL
VALIDATION REGISTRY = CONCEPTUAL
AUTOMATED VALIDATION ENGINE = NOT IMPLEMENTED
```

Contexto operativo:

```text
AUTONOMY_LEVEL = 0
EXECUTION_AUTHORITY = NONE
```

---

# 120. Permitido en Fase 10

Se permite:

* diseñar Validation Architecture;
* ejecutar revisiones manuales;
* comparar outputs;
* realizar adversarial review;
* usar Claude y ChatGPT manualmente como reviewers;
* diseñar Validation Skills;
* diseñar Validation manifests;
* diseñar tests;
* simular conflictos entre Validators;
* diseñar reglas deterministas;
* validar manualmente arquitectura y documentación.

---

# 121. No permitido en Fase 10

No se autoriza:

* validation engine productivo autónomo;
* aprobación automática;
* autorización automática;
* Tool execution automática;
* Memory write automático;
* autonomous reviewer loops;
* autonomous Model-to-Model validation loops;
* self-approval;
* autonomous canonical changes;
* autonomous security changes;
* ejecución externa;
* avance automático a Fase 11.

---

# 122. Sandbox Tests futuros

```text
TEST 1
Valid output passes

TEST 2
Invalid output fails

TEST 3
Missing required criterion

TEST 4
Canonical conflict detected

TEST 5
Security violation blocked

TEST 6
Permission missing

TEST 7
Scope exceeded

TEST 8
Evidence insufficient

TEST 9
Source invalid

TEST 10
Validator disagreement

TEST 11
Consensus incorrectly treated as truth

TEST 12
PASS incorrectly treated as approval

TEST 13
PASS incorrectly treated as authorization

TEST 14
Validator attempts routing

TEST 15
Validator attempts Tool execution

TEST 16
Validator attempts Memory write

TEST 17
Model reviewer unavailable

TEST 18
Fallback reviewer used

TEST 19
Self-validation insufficient

TEST 20
User review required

TEST 21
Confidence high but evidence weak

TEST 22
Validated Memory Candidate attempts auto-write

TEST 23
Validation creates Permission

TEST 24
Validation expands Scope

TEST 25
Validation modifies Canonical Model

TEST 26
Validation retry loop becomes unbounded
```

---

# 123. Métricas futuras

```text
validation_pass_rate
validation_failure_rate
false_positive_rate
false_negative_rate
validator_disagreement_rate
user_override_rate
evidence_failure_rate
source_failure_rate
canonical_conflict_rate
security_block_rate
validation_latency
validation_cost
retry_rate
inconclusive_rate
```

---

# 124. Relación con Canonical Model

Validation debe preservar las distinciones canónicas existentes.

No crea una nueva entidad de primer nivel.

```text
VALIDATOR = FUNCTIONAL ROLE
```

---

# 125. Relación con Orchestrator

```text
ORCHESTRATOR
  ↓
VALIDATION RESOLVER
```

El Orchestrator conserva routing authority.

---

# 126. Relación con Agent Architecture

Agents pueden:

```text
produce outputs
review outputs
detect conflicts
recommend corrections
```

pero no adquieren approval authority.

---

# 127. Relación con Skill Architecture

Validation reutiliza Skills.

Ejemplos:

```text
output_validation
canonical_compliance_check
evidence_validation
consistency_check
completeness_check
```

---

# 128. Relación con Model Interface

Model reviewers deben utilizar:

```text
MODEL ROUTER
MODEL INTERFACE
MODEL ADAPTER
```

No comunicación autónoma directa Model-to-Model.

---

# 129. Relación con Memory Architecture

Validation puede:

```text
validate Memory Candidates
validate retrieval suitability
detect stale Memory
detect conflicts
```

pero:

```text
VALIDATION RESULT ≠ MEMORY WRITE
```

---

# 130. Relación con Data Consistency

Global source precedence y resolución documental de conflictos continúan perteneciendo a:

```text
ROBERT_TECHNICAL_DATA_CONSISTENCY_AND_CONFLICT_RESOLUTION_SPEC
```

Validation aporta detección y evidencia.

No reemplaza esa gobernanza.

---

# 131. Relación con Permissions and Scopes

Validation comprueba Permission y Scope.

No los crea.

```text
PERMISSION VALIDATION ≠ PERMISSION AUTHORITY

SCOPE VALIDATION ≠ SCOPE AUTHORITY
```

---

# 132. Relación con Approval Gate

Approval Gate decide si una acción requiere autorización o aprobación bajo sus reglas.

Validation puede proporcionar evidencia al Gate.

```text
VALIDATION RESULT
  ↓
APPROVAL GATE
```

pero:

```text
VALIDATION RESULT ≠ APPROVAL
```

---

# 133. Relación con Audit Trail

Validation relevante debe ser trazable utilizando la arquitectura de Audit existente.

No crea Audit paralelo.

---

# 134. Decisiones pendientes antes de v1.0

Deben resolverse:

1. Validation Request schema técnico;
2. Validation Result schema técnico;
3. Validation Policy final;
4. Validation Resolver exacto;
5. criterios de obligatoriedad;
6. Validation depth taxonomy final;
7. Validator capability routing;
8. Rule Validation engine;
9. Confidence normalization;
10. multi-validator policy;
11. disagreement resolution;
12. retry policy;
13. fallback policy;
14. source validation rules;
15. evidence validation rules;
16. Memory Validation rules;
17. Model Response Validation;
18. Agent Output Validation;
19. Tool Result Validation;
20. Validation Registry técnico o documental;
21. observability;
22. metrics implementation;
23. cost policy;
24. latency policy;
25. human review thresholds.

---

# 135. Estado actual

```text
DOCUMENT: ROBERT_VALIDATION_ARCHITECTURE
VERSION: 0.1
STATUS: PROPOSED
AUTHORITY: NON-CANONICAL

PHASE: 10
IMPLEMENTATION: NONE

VALIDATION_RESOLVER: CONCEPTUAL
VALIDATION_POLICY: CONCEPTUAL
VALIDATION_REGISTRY: CONCEPTUAL
AUTOMATED_VALIDATION_ENGINE: NOT_IMPLEMENTED

AUTONOMY_LEVEL: 0
EXECUTION_AUTHORITY: NONE
```

---

# 136. Criterios de aprobación

Esta propuesta podrá aprobarse cuando:

1. sea revisada contra Canonical Model;
2. sea revisada contra Orchestrator;
3. sea revisada contra Agent Architecture;
4. sea revisada contra Skill Architecture;
5. sea revisada contra Model Interface;
6. sea revisada contra Memory Architecture;
7. no cree routing authority paralela;
8. no convierta Validator en nueva categoría canónica;
9. no confunda Validation con Authorization;
10. no confunda Validation con Approval;
11. no confunda Confidence con Truth;
12. no trate Consensus como Truth;
13. el User la apruebe explícitamente;
14. se registre Decision;
15. se registre Change Control.

---

# 137. Próximo paso recomendado

Antes de aprobar:

```text
REVIEW ROBERT_VALIDATION_ARCHITECTURE v0.1
```

La revisión deberá buscar especialmente:

```text
VALIDATION AUTHORITY
VALIDATOR ROLE
APPROVAL BOUNDARY
AUTHORIZATION BOUNDARY
ROUTING
MULTI-VALIDATOR CONFLICT
CONFIDENCE
EVIDENCE
SOURCE VALIDATION
MEMORY VALIDATION
MODEL REVIEW
```

Después de aprobación, deberá evaluarse el siguiente bloque de arquitectura pendiente antes de entrar en planificación técnica de implementación.
