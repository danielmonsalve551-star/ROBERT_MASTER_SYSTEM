# ROBERT_MODULES — MAPA DE MÓDULOS DEL SISTEMA

**Versión:** 0.1
**Estado:** Base funcional con Business Builder aprobado; normalizada contra arquitectura canónica vigente
**Última actualización:** 31/08/2026

---

Tags: #robert/orbita-4 #capa/3 #tipo/maestro #robert/modulos #robert/capacidades

[[ROBERT_HOME]]
[[ROBERT_CONTEXT_MASTER]]
[[ROBERT_SYSTEM_ARCHITECTURE]]
[[ROBERT_CANONICAL_MODEL]]
[[ROBERT_AGENT_ARCHITECTURE]]
[[ROBERT_SKILL_ARCHITECTURE]]
[[ROBERT_MODEL_INTERFACE_SPEC]]
[[ROBERT_TOOL_ARCHITECTURE]]
[[ROBERT_TECHNICAL_COMPONENTS_SPEC]]
[[ROBERT_VISUAL_REFERENCE]]

# OBJETIVO

Definir los módulos principales de Robert.

Este documento existe para ordenar las capacidades funcionales del sistema.

Un módulo es un área funcional de Robert.

Un módulo no es lo mismo que:

* una capa interna;
* un comando;
* un Model;
* una Tool;
* un Agent;
* un Skill;
* una automatización;
* una app conectada.

Los Modules representan **qué áreas funcionales puede trabajar Robert**.

Las Layers explican **cómo funciona Robert por dentro**.

Los Commands explican **cómo el usuario activa funciones**.

Los Models aportan **capacidad de inteligencia**.

Los Agents representan **especialistas lógicos**.

Los Skills representan **procedimientos reutilizables**.

Las Tools representan **capacidades técnicas o externas**.

---

# CANONICAL ARCHITECTURE ALIGNMENT

`ROBERT_MODULES` conserva su función como mapa de dominios y capacidades funcionales.

La semántica de sus entidades queda subordinada a:

```text
ROBERT_CANONICAL_MODEL v0.2
DECISIÓN #030
CAMBIO #053
```

y a las arquitecturas especializadas posteriormente aprobadas:

```text
ROBERT_ORCHESTRATOR_SPEC v0.1
DECISIÓN #031
CAMBIO #054

ROBERT_AGENT_ARCHITECTURE v0.1
DECISIÓN #032
CAMBIO #055
CAMBIO #056

ROBERT_SKILL_ARCHITECTURE v0.1
DECISIÓN #033
CAMBIO #057
CAMBIO #058

ROBERT_MODEL_INTERFACE_SPEC v0.1
DECISIÓN #034
CAMBIO #059

ROBERT_MEMORY_ARCHITECTURE v0.1
DECISIÓN #035
CAMBIO #060

ROBERT_VALIDATION_ARCHITECTURE v0.1
DECISIÓN #036
CAMBIO #061

ROBERT_TOOL_ARCHITECTURE v0.1
DECISIÓN #037
CAMBIO #062
```

Se formaliza:

```text
MODULE ≠ AGENT

MODULE ≠ MODEL

MODULE ≠ SKILL

MODULE ≠ TOOL

MODULE ≠ LAYER
```

Un Module representa un dominio funcional.

Puede relacionarse con:

```text
AGENTS
SKILLS
MODELS
TOOLS
COMMANDS
DOCUMENTS
```

pero no se convierte en ninguno de ellos.

---

# PRINCIPIO CENTRAL

Los módulos deben crecer por fases.

Robert no debe activar todos los módulos al mismo tiempo.

Primero se definen.

Después se prueban manualmente.

Después se conectan con Commands y documentos.

Después se integran al MVP correspondiente.

Después pueden relacionarse con Skills, Agents, Models y Tool requirements.

Las conexiones o ejecuciones técnicas reales requieren la fase, Permission, Scope, Security, Approval y Execution Authority correspondientes.

Regla:

```text
PRIMERO CLARIDAD
DESPUÉS CAPACIDAD
DESPUÉS IMPLEMENTACIÓN CONTROLADA
DESPUÉS AUTOMATIZACIÓN AUTORIZADA
```

---

# RELACIÓN CON LA ARQUITECTURA

`ROBERT_SYSTEM_ARCHITECTURE` define 6 Layers:

0. Identidad / Kernel
1. Memory
2. Control
3. Capabilities
4. Governance
5. Presentation

Los Modules viven principalmente dentro de:

```text
CAPA 3 — CAPABILITIES
```

Los Modules deben respetar:

* Capa 2 — Control;
* Capa 4 — Governance;
* `ROBERT_CANONICAL_MODEL`;
* `ROBERT_ORCHESTRATOR_SPEC`;
* `ROBERT_AGENT_ARCHITECTURE`;
* `ROBERT_SKILL_ARCHITECTURE`;
* `ROBERT_MODEL_INTERFACE_SPEC`;
* `ROBERT_TOOL_ARCHITECTURE`;
* `ROBERT_SECURITY_RULES`;
* `ROBERT_COMMANDS`;
* `ROBERT_CONTEXT_MASTER`;
* `ROBERT_PHASES`.

Regla:

```text
NO MODULE
MAY BYPASS
ROBERT GOVERNANCE
```

Ningún Module puede ejecutar acciones fuera de autorización.

---

# DEFINICIÓN DE MÓDULO

Un Module es una capacidad o dominio funcional de Robert.

Ejemplos:

* Ideas;
* Projects;
* Documents;
* Finance;
* Marketing;
* Security.

Un Module sirve para organizar trabajo dentro de un área.

Cada Module debe poder declarar:

* nombre;
* propósito;
* función;
* estado;
* prioridad;
* Commands relacionados;
* documentos relacionados;
* Agents relacionados;
* Skills relacionados;
* Model requirements;
* Tool requirements;
* nivel de Risk;
* límites;
* posible evolución futura.

---

# DIFERENCIA ENTRE MODULES, LAYERS, MODELS, AGENTS, SKILLS Y TOOLS

## MODULES

Son áreas funcionales de Robert.

Ejemplos:

* Ideas;
* Projects;
* Finance;
* Marketing;
* Documents;
* Security.

```text
MODULE
=
WHERE FUNCTIONAL WORK BELONGS
```

---

## LAYERS

Son capas internas de arquitectura.

Ejemplos:

* Identidad;
* Memory;
* Control;
* Capabilities;
* Governance;
* Presentation.

```text
LAYER
≠
MODULE
```

---

## MODELS

Son proveedores de inteligencia que Robert puede utilizar para:

* razonamiento;
* análisis;
* generación;
* clasificación;
* revisión;
* evaluación.

Ejemplos actuales:

* Claude;
* ChatGPT.

Referencia:

```text
ROBERT_MODEL_INTERFACE_SPEC v0.1
DECISIÓN #034
CAMBIO #059
```

Reglas canónicas:

```text
MODEL ≠ TOOL

MODEL ≠ AGENT

MODEL ≠ SKILL

MODEL ≠ MODULE
```

Claude y ChatGPT son Models.

No son Tools.

Los Models pueden colaborar con Agents, Skills, Modules y Tool Requests, pero no adquieren Permission, Scope, Routing Authority o Execution Authority por existir.

---

## AGENTS

Agents ya forman parte de la arquitectura aprobada de Robert.

Referencia:

```text
ROBERT_AGENT_ARCHITECTURE v0.1
DECISIÓN #032
CAMBIO #055
CAMBIO #056
```

Un Agent es un especialista lógico que puede operar dentro de uno o más Modules para cumplir un objetivo definido.

Ejemplos del catálogo arquitectónico aprobado:

* ROBERT_ARCHITECT;
* ROBERT_RESEARCHER;
* ROBERT_CRITIC;
* ROBERT_SECURITY;
* ROBERT_MEMORY;
* ROBERT_CODER;
* ROBERT_TESTER;
* ROBERT_STRATEGIST.

Se formaliza:

```text
AGENT ≠ MODULE

AGENT ≠ MODEL

AGENT ≠ SKILL

AGENT ≠ TOOL

AGENT ≠ ORCHESTRATOR
```

Un Agent puede participar en uno o más Modules.

Los Agents no están implementados como actores autónomos en Fase 10.

Por tanto:

```text
AGENT_ARCHITECTURE = APPROVED

AUTONOMOUS_AGENTS = NOT ACTIVE

AUTONOMY_LEVEL = 0

EXECUTION_AUTHORITY = NONE
```

---

## SKILLS

Skills representan procedimientos reutilizables.

Referencia:

```text
ROBERT_SKILL_ARCHITECTURE v0.1
DECISIÓN #033
CAMBIO #057
CAMBIO #058
```

Se formaliza:

```text
SKILL ≠ AGENT

SKILL ≠ MODULE

SKILL ≠ TOOL

SKILL ≠ AUTONOMOUS ACTOR
```

Relación:

```text
MODULE
=
WHERE FUNCTIONAL WORK BELONGS

AGENT
=
WHO SPECIALIZES IN THE WORK

SKILL
=
HOW A REUSABLE PROCEDURE IS PERFORMED
```

---

## TOOLS

Tools son capacidades externas o técnicas mediante las cuales Robert puede interactuar con recursos, servicios o entornos.

Referencia:

```text
ROBERT_TOOL_ARCHITECTURE v0.1
DECISIÓN #037
CAMBIO #062
```

Ejemplos conceptuales:

* filesystem;
* GitHub;
* web;
* databases;
* terminal / code execution environment;
* Gmail;
* Calendar;
* Google Drive;
* APIs;
* otras integraciones.

Se formaliza:

```text
TOOL ≠ MODEL

TOOL ≠ AGENT

TOOL ≠ SKILL

TOOL ≠ MODULE

TOOL AVAILABLE
≠
TOOL ALLOWED

TOOL REQUEST
≠
TOOL AUTHORIZATION
```

Durante Fase 10:

```text
REAL_TOOL_EXECUTION = DISABLED

AUTONOMY_LEVEL = 0

EXECUTION_AUTHORITY = NONE
```

---

# CAPABILITY PROVIDERS

La clasificación vigente es:

```text
CAPABILITY PROVIDERS
│
├── MODELS
│   ├── Claude
│   ├── ChatGPT
│   └── future_model
│
└── TOOLS
    ├── filesystem
    ├── GitHub
    ├── web
    ├── database
    ├── code execution environment
    ├── Gmail
    ├── Calendar
    ├── Google Drive
    └── otras integraciones
```

Regla:

```text
MODELS ≠ TOOLS
```

Un Model puede producir un Tool Request mediante la arquitectura correspondiente.

Eso no convierte al Model en Tool.

---

# MODULE ROUTING

Modules no se seleccionan autónomamente.

La autoridad de routing pertenece al Orchestrator.

Referencia:

```text
ROBERT_ORCHESTRATOR_SPEC v0.1
DECISIÓN #031
CAMBIO #054
```

Flujo conceptual:

```text
TASK
  ↓
ORCHESTRATOR
  ↓
MODULE ROUTING
  ↓
AGENT / SKILL / MODEL / TOOL RESOLUTION
```

Se formaliza:

```text
MODULE ≠ ROUTER

AGENT ≠ MODULE ROUTER

MODEL ≠ MODULE ROUTER

ORCHESTRATOR
=
ROUTING AUTHORITY
```

---

# MAPA GENERAL DE MÓDULOS

Los Modules principales de Robert son:

1. Robert Core
2. Command Center
3. Memory
4. Ideas
5. Projects
6. Business Builder
7. Administration
8. Finance
9. Accounting
10. Tax / Fiscal
11. Marketing
12. Design
13. Sales
14. Operations
15. Legal Reference
16. Documents
17. Research
18. Analytics
19. Automation
20. Apps Connector
21. Calendar
22. Email
23. Tasks
24. Voice
25. Code / Development
26. Knowledge Base
27. Security
28. Decisions Log
29. Learning System
30. Visual Projection

---

# ESTADO GENERAL DE MÓDULOS

Estado actual:

```text
BASE FUNCTIONAL MAP
CANONICALLY NORMALIZED
```

Business Builder posee aprobación específica.

El mapa completo de 30 Modules no se marca automáticamente como formalmente aprobado mediante esta normalización.

Los Modules todavía no están implementados técnicamente.

La prioridad actual ya no es diseñar el MVP manual.

Robert se encuentra en Fase 10 / Implementation Readiness.

La prioridad vigente es:

1. mantener el mapa funcional alineado al Canonical Model;
2. definir relaciones Module → Command;
3. definir relaciones Module → Agent;
4. definir relaciones Module → Skill;
5. definir relaciones Module → Model requirement;
6. definir relaciones Module → Tool requirement;
7. utilizar el Build Order aprobado para futura implementación;
8. evitar activación o ejecución real sin autorización.

---

# MÓDULOS RELEVANTES PARA EL MVP MANUAL

El MVP manual utilizó principalmente:

1. Robert Core
2. Command Center
3. Memory
4. Ideas
5. Projects
6. Documents
7. Knowledge Base
8. Security
9. Decisions Log
10. Visual Projection
11. Tasks
12. Research

Estos Modules permitieron probar Robert sin programación productiva.

---

# MÓDULOS RELEVANTES PARA EL MVP TÉCNICO INICIAL

La priorización funcional puede considerar:

1. Robert Core
2. Command Center
3. Memory
4. Documents
5. Projects
6. Tasks
7. Decisions Log
8. Security
9. Visual Projection
10. Apps Connector básico

Sin embargo, la secuencia técnica de implementación no la gobierna este listado.

La secuencia oficial debe seguir:

```text
ROBERT_BUILD_ORDER v0.1
DECISIÓN #040
CAMBIO #065
```

Regla:

```text
MODULE PRIORITY
≠
BUILD ORDER
```

No se recomienda comenzar con áreas sensibles o ejecución externa antes de que existan sus dependencias de Governance, Contracts, Audit y Validation.

---

# MÓDULO 1 — ROBERT CORE

Propósito:

Representar el núcleo lógico funcional de Robert.

Función:

Relacionar conceptualmente:

* contexto;
* memoria;
* Commands;
* documentos;
* Decisions;
* Modules;
* Security;
* Governance;
* Presentation.

El routing técnico pertenece al Orchestrator.

Debe considerar:

* intención del usuario;
* Context autorizado;
* documento relacionado;
* Command detectado;
* Module requerido;
* Risk;
* Permission;
* Scope;
* Approval;
* salida esperada.

Estado:

Base conceptual.

Prioridad:

Crítica.

Risk:

Alto si se define mal.

Límites:

Robert Core no debe convertirse en un Module gigante donde todo se mezcle.

Debe representar núcleo funcional sin sustituir al Orchestrator ni a las Layers especializadas.

Documentos relacionados:

* ROBERT_CONTEXT_MASTER;
* ROBERT_CANONICAL_MODEL;
* ROBERT_SYSTEM_ARCHITECTURE;
* ROBERT_ORCHESTRATOR_SPEC;
* ROBERT_SECURITY_RULES;
* ROBERT_COMMANDS.

---

# MÓDULO 2 — COMMAND CENTER

Propósito:

Ser el centro de control operativo visible de Robert.

Función:

Mostrar y coordinar conceptualmente:

* Commands;
* estados;
* Approval;
* modo activo;
* Autonomy;
* Risk;
* bloqueos;
* siguiente paso.

Debe permitir que el usuario controle Robert de forma clara.

Estado:

Base conceptual.

Prioridad:

Crítica.

Risk:

Medio.

Límites:

Command Center no posee Execution Authority.

No debe ejecutar acciones saltándose Governance.

Documentos relacionados:

* ROBERT_COMMANDS;
* ROBERT_SECURITY_RULES;
* ROBERT_SYSTEM_ARCHITECTURE;
* ROBERT_ORCHESTRATOR_SPEC;
* ROBERT_VISUAL_REFERENCE.

---

# MÓDULO 3 — MEMORY

Propósito:

Organizar funcionalmente el uso de Memory.

La arquitectura formal de Memory pertenece a:

```text
ROBERT_MEMORY_ARCHITECTURE v0.1
DECISIÓN #035
CAMBIO #060
```

Función:

Trabajar con:

```text
MEMORY_TYPE:
CORE
SEMANTIC
EPISODIC
DECISIONAL
PROCEDURAL
```

y:

```text
RETENTION:
ACTIVE
TEMPORARY
PERSISTENT
```

Se mantiene:

```text
CONTEXT ≠ MEMORY

MEMORY_TYPE ≠ RETENTION

MEMORY CANDIDATE ≠ MEMORY
```

Estado:

Arquitectura aprobada / implementación no iniciada.

Prioridad:

Crítica.

Risk:

Medio.

Límites:

No debe guardar todo.

No debe guardar información sensible innecesaria.

No existe Automatic Memory Write autorizado.

Documentos relacionados:

* ROBERT_MEMORY_ARCHITECTURE;
* ROBERT_CONTEXT_MASTER;
* ROBERT_DECISIONS_LOG;
* ROBERT_SECURITY_RULES.

---

# MÓDULO 4 — IDEAS

Propósito:

Capturar, ordenar y desarrollar ideas.

Función:

Convertir ideas sueltas en:

* conceptos;
* Projects;
* documentos;
* propuestas;
* Decisions;
* planes;
* empresas;
* sistemas.

Estado:

Base inicial.

Prioridad:

Alta.

Risk:

Bajo.

Límites:

```text
IDEA ≠ DECISION
```

No toda idea debe convertirse en Memory persistente.

---

# MÓDULO 5 — PROJECTS

Propósito:

Organizar Projects.

Función:

Convertir ideas o trabajos en Projects con:

* objetivo;
* estado;
* Tasks;
* documentos;
* Decisions;
* fases;
* responsables;
* riesgos;
* próximos pasos.

Estado:

Base inicial.

Prioridad:

Alta.

Risk:

Bajo a medio.

Límites:

No debe cerrar fases ni Projects sin la gobernanza correspondiente.

Documentos relacionados:

* ROBERT_PHASES;
* ROBERT_DECISIONS_LOG;
* ROBERT_CONTEXT_MASTER.

---

# MÓDULO 6 — BUSINESS BUILDER

## Business Builder — Canonical Alignment

Business Builder conserva su estado como capacidad funcional aprobada mediante:

```text
DECISIÓN #001
```

Esta normalización no modifica su aprobación ni alcance.

Business Builder puede relacionarse con:

```text
AGENTS
SKILLS
MODELS
TOOLS
```

pero:

```text
BUSINESS BUILDER ≠ AGENT

BUSINESS BUILDER ≠ MODEL

BUSINESS BUILDER ≠ TOOL
```

Durante Fase 10 continúa limitado a:

```text
PLANNING
ANALYSIS
DOCUMENTATION
SIMULATION
DRAFTING
```

No autoriza:

```text
REAL BUSINESS EXECUTION
EXTERNAL TOOL EXECUTION
AUTONOMOUS AGENTS
LEGAL / FISCAL / FINANCIAL FINAL DECISIONS
```

---

## Propósito

Ayudar al usuario a transformar ideas de negocio en estructuras empresariales completas, ordenadas y controladas.

Business Builder es el Module de Robert encargado de apoyar la creación, desarrollo y organización conceptual de empresas desde una idea inicial hasta una estructura funcional por áreas.

---

# BUSINESS BUILDER — EMPRESAS COMPLETAS

## Estado

Aprobado por el usuario.

Fecha de aprobación: 22/06/2026

Decisión relacionada:

```text
DECISIÓN #001
```

Business Builder — Empresas completas fue aprobado como capacidad de Robert para estructurar empresas completas por áreas funcionales.

---

## Función principal

Business Builder ayuda a convertir una idea de negocio en:

* modelo de negocio;
* estructura administrativa;
* plan financiero;
* estructura contable;
* análisis fiscal;
* estrategia de marketing;
* identidad de diseño;
* sistema de ventas;
* operación interna;
* documentos base;
* decisiones estratégicas;
* procesos organizados;
* plan de crecimiento;
* sistema empresarial estructurado.

---

## Definición

Business Builder no es una automatización empresarial completa.

Actualmente funciona como capacidad de:

* Planning;
* análisis;
* estructura;
* documentación;
* simulación;
* Drafting.

Robert puede ayudar a construir conceptualmente una empresa por áreas, pero no debe ejecutar acciones reales sin la autorización, Governance y fase correspondientes.

---

## Áreas que puede estructurar

### 1. Administration

Organización general, estructura interna, roles, procesos, responsabilidades, políticas, Tasks y operación administrativa.

### 2. Finance

Presupuestos, proyecciones, costos, ingresos, flujo de efectivo, rentabilidad, escenarios, análisis financiero y planeación de recursos.

### 3. Accounting

Catálogo conceptual de cuentas, registros, reportes, organización de información contable y estructura documental.

Robert no sustituye a un contador.

### 4. Tax / Fiscal

Identificación de temas fiscales, obligaciones posibles, Risks, preguntas para revisar con especialista y organización de información.

Robert no sustituye a un asesor fiscal.

### 5. Marketing

Estrategia de mercado, cliente ideal, propuesta de valor, posicionamiento, campañas, contenido y comunicación.

### 6. Design

Identidad visual, estilo, marca, presentación, materiales, experiencia visual y coherencia gráfica.

### 7. Sales

Proceso comercial, canales, guiones, seguimiento, embudo, CRM conceptual, precios, promociones y cierre.

### 8. Operations

Procesos internos, logística, entregas, proveedores, calidad, recursos, ejecución diaria y mejora continua.

### 9. Research

Análisis de mercado, competencia, tendencias, referencias, oportunidades, Risks y validación de ideas.

### 10. Documents

Creación de documentos base, planes, reportes, propuestas, presentaciones, manuales, checklists y estructuras internas.

### 11. Processes

Diseño de procesos, workflows, SOPs, responsabilidades, Tasks repetitivas y mejora operativa.

### 12. Systems

Diseño conceptual de sistemas internos para operar, vender, organizar, medir y escalar una empresa.

---

## Qué puede hacer actualmente

Business Builder puede:

* ordenar ideas de negocio;
* crear estructuras de empresa;
* preparar documentos base;
* proponer áreas funcionales;
* crear planes iniciales;
* simular escenarios;
* generar preguntas estratégicas;
* preparar Model Requests;
* crear borradores de procesos;
* detectar Risks;
* separar Decisions importantes;
* preparar registros para Decisions Log;
* crear mapas de áreas;
* crear checklists;
* crear planes por etapas;
* preparar propuestas de estrategia;
* identificar qué información falta.

---

## Qué no puede hacer todavía

Business Builder no puede:

* crear empresas legalmente;
* hacer trámites reales;
* presentar declaraciones fiscales;
* tomar decisiones fiscales definitivas;
* tomar decisiones legales definitivas;
* tomar decisiones contables definitivas;
* tomar decisiones financieras definitivas;
* mover dinero;
* hacer pagos;
* contratar personas;
* enviar correos reales automáticamente;
* publicar campañas reales automáticamente;
* ejecutar Tools externas sin autorización;
* automatizar procesos reales;
* ejecutar acciones sin autorización;
* sustituir abogados, contadores, asesores fiscales o asesores financieros.

---

## Relación con otros Modules

Business Builder se relaciona con:

* Administration;
* Finance;
* Accounting;
* Tax / Fiscal;
* Marketing;
* Design;
* Sales;
* Operations;
* Documents;
* Research;
* Analytics;
* Legal Reference;
* Decisions Log;
* Security;
* Automation;
* Apps Connector;
* Visual Projection.

---

## Relación con ROBERT_SECURITY_RULES

Business Builder debe respetar siempre:

1. El usuario mantiene la autoridad humana superior.
2. Robert no ejecuta acciones importantes sin la autorización correspondiente.
3. Robert no sustituye a profesionales legales, fiscales, contables o financieros.
4. Robert puede preparar, ordenar, simular y proponer.
5. Robert no debe ejecutar acciones externas fuera del Scope autorizado.
6. Robert debe separar propuesta, preparación, Approval y ejecución.
7. Decisions importantes deben seguir la gobernanza documental vigente.
8. Risk no equivale a Permission ni Execution Authority.

---

## Relación con ROBERT_PHASES

Business Builder existe como capacidad aprobada dentro del mapa funcional.

En Fase 10:

* puede definirse;
* puede revisarse;
* puede probarse documentalmente;
* puede usarse para Drafting;
* puede simularse en Sandbox;
* puede utilizarse como estructura estratégica.

No debe convertirse todavía en:

```text
AUTONOMOUS BUSINESS AGENT SYSTEM
REAL EXTERNAL EXECUTION
AUTOMATIC TOOL WORKFLOW
```

---

## Relación con Sandbox

Business Builder puede probarse con casos reales o simulados dentro de límites seguros.

Ejemplo:

```text
BUSINESS IDEA
↓
CLASSIFICATION
↓
FUNCTIONAL AREAS
↓
REQUIRED DOCUMENTS
↓
RISKS
↓
PENDING DECISIONS
↓
NEXT STEP
```

El objetivo no es ejecutar la empresa.

El objetivo es comprobar que Robert puede estructurarla de forma clara, segura y útil.

---

## Risk

Nivel general:

Medio a alto según operación.

Business Builder puede tocar áreas sensibles como:

* Finance;
* Tax;
* Accounting;
* Legal;
* Operations;
* decisiones empresariales importantes.

Regla:

Las operaciones concretas deben utilizar la escala y gobernanza de Risk vigente.

---

## Prioridad

Alta para la visión general de Robert.

La prioridad técnica exacta debe subordinarse a:

```text
ROBERT_BUILD_ORDER v0.1
```

---

## Límites

Business Builder no debe:

* automatizar empresas sin autorización;
* activar Agents autónomos;
* ejecutar Tools reales sin autorización;
* ejecutar procesos reales por sí mismo;
* tomar Decisions críticas por el usuario;
* presentar información sensible como verdad definitiva;
* sustituir revisión profesional;
* avanzar de fase automáticamente.

---

## Criterio de éxito

Business Builder funciona correctamente si Robert puede tomar una idea de negocio y convertirla en una estructura clara por áreas, documentos, Decisions, Risks y siguientes pasos sin quitar control al usuario ni ejecutar acciones reales no autorizadas.

---

# MÓDULO 7 — ADMINISTRATION

Propósito:

Organizar Tasks administrativas.

Función:

Ayudar con:

* procesos;
* documentos;
* organización;
* seguimiento;
* Tasks;
* archivos;
* estructura operativa.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Media.

Risk:

Medio.

Límites:

No debe modificar recursos externos reales sin autorización.

---

# MÓDULO 8 — FINANCE

Propósito:

Apoyar análisis financiero.

Función:

Puede ayudar con:

* presupuestos;
* escenarios;
* modelos;
* Risks;
* reportes;
* análisis;
* preguntas para asesores;
* organización financiera.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Alta a futuro.

Risk:

Alto.

Límites:

No debe ejecutar compras, pagos, inversiones, apuestas u operaciones financieras.

No sustituye a asesor financiero.

---

# MÓDULO 9 — ACCOUNTING

Propósito:

Apoyar organización contable.

Función:

Puede ayudar con:

* clasificación de información;
* reportes;
* estructura de documentos;
* revisión conceptual;
* preparación de preguntas;
* Drafting.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Media a alta.

Risk:

Alto.

Límites:

No debe emitir información contable definitiva sin revisión profesional.

---

# MÓDULO 10 — TAX / FISCAL

Propósito:

Apoyar organización fiscal.

Función:

Puede ayudar con:

* conceptos fiscales;
* checklists;
* organización de documentos;
* preguntas para asesores;
* escenarios;
* Drafting.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Media a alta.

Risk:

Alto.

Límites:

No debe tomar Decisions fiscales definitivas.

No sustituye a contador o asesor fiscal.

---

# MÓDULO 11 — MARKETING

Propósito:

Crear y organizar estrategias de Marketing.

Función:

Puede ayudar con:

* campañas;
* branding;
* contenido;
* audiencia;
* posicionamiento;
* mensajes;
* estrategia comercial;
* calendario de contenido.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Alta para Business Builder.

Risk:

Medio.

Límites:

No debe publicar contenido externamente sin autorización.

---

# MÓDULO 12 — DESIGN

Propósito:

Desarrollar dirección visual, diseño y creatividad.

Función:

Puede ayudar con:

* identidad visual;
* interfaz;
* renders;
* presentaciones;
* materiales;
* conceptos;
* UX;
* referencias visuales.

Estado:

Activo conceptual.

Prioridad:

Alta.

Risk:

Bajo a medio.

Límites:

No debe cambiar una referencia visual canónica sin la gobernanza correspondiente.

---

# MÓDULO 13 — SALES

Propósito:

Apoyar ventas y procesos comerciales.

Función:

Puede ayudar con:

* argumentos de venta;
* propuestas;
* scripts;
* CRM conceptual;
* seguimiento;
* segmentación;
* estrategias.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Media.

Risk:

Medio.

Límites:

No debe contactar clientes automáticamente sin autorización.

---

# MÓDULO 14 — OPERATIONS

Propósito:

Organizar Operations y procesos.

Función:

Puede ayudar con:

* procesos internos;
* flows;
* SOPs;
* Tasks repetitivas;
* organización;
* mejora operativa.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Media.

Risk:

Medio.

Límites:

No debe automatizar Operations reales sin autorización.

---

# MÓDULO 15 — LEGAL REFERENCE

Propósito:

Ayudar a organizar información legal de referencia.

Función:

Puede ayudar con:

* conceptos;
* checklists;
* preguntas para abogados;
* organización de contratos;
* revisión de Risks;
* Drafting.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Media.

Risk:

Alto.

Límites:

No sustituye a abogado.

No debe tomar Decisions legales definitivas.

---

# MÓDULO 16 — DOCUMENTS

Propósito:

Crear, ordenar y mantener documentos.

Función:

Puede ayudar con:

* documentos maestros;
* versiones;
* Drafting;
* estructura;
* formato;
* actualizaciones;
* referencias;
* exportación.

Estado:

Activo conceptual.

Prioridad:

Crítica.

Risk:

Medio.

Límites:

No debe modificar documentos oficiales fuera de Change Control cuando corresponda.

---

# MÓDULO 17 — RESEARCH

Propósito:

Investigar y organizar información.

Función:

Puede ayudar con:

* preguntas;
* fuentes;
* comparaciones;
* análisis;
* reportes;
* resúmenes;
* búsqueda de información.

Estado:

Conceptual / futuro para implementación técnica.

Prioridad:

Alta.

Risk:

Medio.

Límites:

Debe mantener evidencia cuando corresponda.

Debe distinguir:

```text
FACT
OPINION
INFERENCE
MODEL OUTPUT
```

---

# MÓDULO 18 — ANALYTICS

Propósito:

Analizar datos, patrones y métricas.

Función:

Puede ayudar con:

* tablas;
* métricas;
* reportes;
* dashboards;
* interpretaciones;
* escenarios;
* comparaciones.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Media.

Risk:

Medio.

Límites:

No debe interpretar datos críticos sin Context suficiente.

---

# MÓDULO 19 — AUTOMATION

Propósito:

Diseñar Automation futura.

Función:

Puede ayudar con:

* workflows;
* triggers;
* acciones;
* Permissions;
* Risks;
* Tools;
* tests;
* logs.

Estado:

Conceptual / futuro.

Prioridad:

Alta a futuro.

Risk:

Alto.

Límites:

```text
AUTOMATION DESIGN
≠
AUTOMATION AUTHORIZATION
```

No debe activar Automation real sin Governance, Sandbox y autorización correspondiente.

---

# MÓDULO 20 — APPS CONNECTOR

Propósito:

Representar funcionalmente conexiones con Tools externas.

Función:

Puede ayudar con:

* mapa de providers;
* Permissions;
* estados de conexión;
* lectura;
* escritura;
* Risks;
* desconexión;
* Sandbox.

Estado:

Conceptual / futuro para implementación.

Prioridad:

Alta a futuro.

Risk:

Alto.

Límites:

```text
CONNECTED
≠
AUTHORIZED
```

No debe conectar o utilizar servicios externos fuera del Scope autorizado.

La arquitectura técnica de Tools pertenece a `ROBERT_TOOL_ARCHITECTURE`.

---

# MÓDULO 21 — CALENDAR

Propósito:

Representar capacidades relacionadas con Calendar.

Función:

Puede ayudar con:

* eventos;
* agenda;
* recordatorios;
* Planning;
* disponibilidad;
* reuniones.

Estado:

Conceptual / futuro para ejecución.

Prioridad:

Media.

Risk:

Alto cuando crea o modifica eventos.

Límites:

Las operaciones de escritura requieren Governance y autorización correspondiente.

---

# MÓDULO 22 — EMAIL

Propósito:

Representar capacidades relacionadas con Email.

Función:

Puede ayudar con:

* Drafts;
* resúmenes;
* clasificación;
* respuestas propuestas;
* seguimiento;
* búsqueda.

Estado:

Conceptual / futuro para ejecución.

Prioridad:

Media.

Risk:

Alto para acciones externas.

Límites:

Preparar un Email no equivale a enviarlo.

```text
DRAFT
≠
SEND
```

---

# MÓDULO 23 — TASKS

Propósito:

Gestionar Tasks.

Función:

Puede ayudar con:

* pendientes;
* prioridades;
* fechas;
* responsables;
* seguimiento;
* Next Steps;
* checklists.

Estado:

Base inicial.

Prioridad:

Alta.

Risk:

Bajo a medio.

Límites:

Una Task interna no autoriza automáticamente una acción externa.

---

# MÓDULO 24 — VOICE

Propósito:

Permitir interacción por Voice en el futuro.

Función:

Puede ayudar con:

* Commands por voz;
* dictado;
* respuesta hablada;
* confirmación de acciones;
* control manos libres.

Estado:

Futuro.

Prioridad:

Media.

Risk:

Medio a alto.

Límites:

Voice input no crea autoridad adicional.

Las acciones críticas deben seguir Governance normal.

---

# MÓDULO 25 — CODE / DEVELOPMENT

Propósito:

Apoyar desarrollo técnico de Robert.

Función:

Puede ayudar con:

* arquitectura técnica;
* Code;
* repositories;
* debugging;
* prototipos;
* Deployment;
* documentación técnica.

Estado:

Conceptual / implementación futura.

Prioridad:

Alta para implementación técnica.

Risk:

Alto.

Límites:

```text
CODE GENERATION
≠
CODE EXECUTION

CODE IMPLEMENTATION
≠
EXTERNAL EXECUTION AUTHORITY
```

Debe seguir `ROBERT_BUILD_ORDER` y la futura autorización explícita de implementación.

---

# MÓDULO 26 — KNOWLEDGE BASE

Propósito:

Organizar conocimiento.

Función:

Puede ayudar con:

* notas;
* referencias;
* aprendizaje;
* documentos;
* conceptos;
* resúmenes;
* relaciones.

Estado:

Base inicial.

Prioridad:

Alta.

Risk:

Bajo a medio.

Límites:

Knowledge Base no equivale automáticamente a Memory persistente ni a fuente canónica.

---

# MÓDULO 27 — SECURITY

Propósito:

Representar funcionalmente capacidades de Security.

Función:

Debe considerar:

* Risks;
* Permissions;
* Scope;
* Approval;
* privacidad;
* credenciales;
* acciones críticas;
* fases;
* Autonomy;
* Tools.

Estado:

Base conceptual crítica.

Prioridad:

Crítica.

Risk:

Crítico si falla.

Límites:

Security no debe confundirse con una nueva autoridad humana.

Opera dentro de la gobernanza aprobada.

Security tiene prioridad sobre velocidad, diseño, Automation o conveniencia cuando exista conflicto de seguridad.

---

# MÓDULO 28 — DECISIONS LOG

Propósito:

Registrar Decisions.

Función:

Puede ayudar con:

* propuestas;
* Decisions pendientes;
* Decisions aprobadas;
* motivo;
* impacto;
* fecha;
* documentos relacionados;
* Next Step.

Estado:

Base inicial.

Prioridad:

Crítica.

Risk:

Medio.

Límites:

```text
PROPOSAL
≠
DECISION
```

No debe registrar una Decision como aprobada sin autoridad humana válida.

---

# MÓDULO 29 — LEARNING SYSTEM

Propósito:

Permitir evolución futura basada en aprendizaje controlado.

Función:

Puede ayudar con:

* patrones;
* preferencias;
* aprendizajes;
* mejoras;
* ajustes;
* feedback;
* evolución del sistema.

Estado:

Futuro.

Prioridad:

Media.

Risk:

Medio.

Límites:

No debe crear Automatic Memory Write ni modificar comportamiento canónico sin Governance.

---

# MÓDULO 30 — VISUAL PROJECTION

Propósito:

Mostrar información visualmente.

Función:

Puede ayudar con:

* mapas;
* dashboards;
* nodos;
* Modules;
* documentos;
* Commands;
* Decisions;
* Apps;
* Autonomy;
* Security;
* flows.

Estado:

Base visual en revisión.

Prioridad:

Alta.

Risk:

Medio.

Límites:

```text
VISUAL REPRESENTATION
≠
ARCHITECTURAL AUTHORITY
```

No debe inventar capacidades que no existan en arquitectura.

---

# RELACIÓN ENTRE MÓDULOS Y COMANDOS

Los Commands pueden solicitar funciones relacionadas con Modules.

La resolución final pertenece al Orchestrator.

Ejemplos funcionales:

## RESUMEN

Puede involucrar:

* Memory;
* Knowledge Base;
* Documents.

## CONCLUSION

Puede involucrar:

* Knowledge Base;
* Documents;
* Model capabilities.

## DETENTE

Puede involucrar:

* Security;
* Command Center;
* Robert Core.

## MODO_SANDBOX

Puede involucrar:

* Security;
* Automation;
* Apps Connector;
* Code / Development.

## INFORME_ACCIONES

Puede involucrar:

* Decisions Log;
* Security;
* Audit;
* Memory.

## CLASIFICAR

Puede involucrar:

* Knowledge Base;
* Documents;
* Memory.

## ACTUALIZA

Puede involucrar:

* Documents;
* Security;
* Decisions Log.

Regla:

```text
COMMAND
≠
DIRECT MODULE EXECUTION

COMMAND
→
ORCHESTRATOR
→
ROUTING
```

---

# RELACIÓN ENTRE MÓDULOS Y AUTONOMÍA

Autonomy no es un Module.

Autonomy es una propiedad gobernada del sistema.

Puede afectar:

* Control;
* Capabilities;
* Governance.

Modules relacionados funcionalmente pueden incluir:

## Security

Evalúa condiciones de seguridad según arquitectura vigente.

## Command Center

Muestra estado, Commands y controles.

## Documents

Gestiona capacidades documentales.

## Automation

Representa Automation futura.

## Apps Connector

Representa conexiones con Tools.

## Decisions Log

Registra Decisions.

## Visual Projection

Muestra estados relevantes.

Se formaliza:

```text
MODULE
≠
AUTONOMY AUTHORITY
```

Durante Fase 10:

```text
AUTONOMY_LEVEL = 0

EXECUTION_AUTHORITY = NONE
```

---

# RISK POR MÓDULO

Los siguientes grupos son referencias funcionales iniciales.

No reemplazan la evaluación de Risk por operación.

## Generalmente bajo

* Ideas;
* Knowledge Base;
* Visual Projection;
* Research básico;
* Design conceptual.

## Generalmente medio

* Projects;
* Documents;
* Tasks;
* Decisions Log;
* Analytics;
* Marketing;
* Operations.

## Generalmente alto

* Finance;
* Accounting;
* Tax / Fiscal;
* Legal Reference;
* Email con acciones externas;
* Calendar con acciones externas;
* Apps Connector;
* Automation;
* Code / Development con ejecución.

## Puede llegar a crítico

* Security failure;
* credenciales;
* datos sensibles;
* operaciones financieras;
* decisiones legales/fiscales de alto impacto;
* ejecución externa no autorizada.

Regla:

```text
MODULE RISK PROFILE
≠
OPERATION RISK ASSESSMENT
```

La evaluación concreta usa la escala de Risk vigente de Robert.

---

# PRIORIDAD FUNCIONAL DE MÓDULOS

Esta prioridad describe importancia funcional.

No sustituye `ROBERT_BUILD_ORDER`.

## Prioridad funcional 1 — Core

* Robert Core
* Command Center
* Memory
* Documents
* Knowledge Base
* Security
* Decisions Log
* Ideas
* Projects
* Tasks

## Prioridad funcional 2 — Visual y organización

* Visual Projection
* Design
* Research
* Analytics

## Prioridad funcional 3 — Business Builder

* Business Builder
* Administration
* Marketing
* Sales
* Operations

## Prioridad funcional 4 — Áreas sensibles

* Finance
* Accounting
* Tax / Fiscal
* Legal Reference

## Prioridad funcional 5 — Integraciones futuras

* Apps Connector
* Email
* Calendar
* Automation
* Voice
* Code / Development

## Prioridad funcional 6 — Expansión

* Learning System
* evolución de Agents dentro de Modules según arquitectura vigente

Regla:

```text
FUNCTIONAL PRIORITY
≠
TECHNICAL BUILD STAGE
```

La secuencia técnica oficial pertenece a:

```text
ROBERT_BUILD_ORDER v0.1
DECISIÓN #040
CAMBIO #065
```

---

# REGLAS MAESTRAS DE MÓDULOS

1. Ningún Module puede saltarse Security Rules.
2. Ningún Module puede crear Permission por sí mismo.
3. Ningún Module puede ampliar Scope por inferencia.
4. Ningún Module puede obtener Execution Authority por existir.
5. Ningún Module puede ejecutar acciones externas sin autorización correspondiente.
6. Ningún Module puede modificar documentos canónicos fuera de Governance.
7. Ningún Module puede registrar Decisions aprobadas sin autoridad válida.
8. Ningún Module puede utilizar Tools reales solo porque estén disponibles.
9. Ningún Module puede activar Automation real antes de los gates correspondientes.
10. Los Modules deben crecer por fases.
11. Los Modules pueden relacionarse con Commands, Agents, Skills, Models y Tools.
12. Los Modules deben respetar la arquitectura de 6 Layers.
13. Los Modules deben distinguir propuesta, preparación, simulación y ejecución.
14. Los Modules deben utilizar Risk cuando aplique.
15. Los Modules deben producir trazabilidad cuando aplique.
16. Los Modules no deben duplicarse innecesariamente.
17. Los Modules deben servir al usuario sin complicar innecesariamente el sistema.
18. Module routing pertenece al Orchestrator.
19. Agent Architecture aprobada no significa Autonomous Agents activos.
20. Tool Architecture aprobada no significa Tool execution autorizada.

---

# INVARIANTES CANÓNICAS

```text
MODULE ≠ LAYER

MODULE ≠ AGENT

MODULE ≠ MODEL

MODULE ≠ SKILL

MODULE ≠ TOOL

MODEL ≠ TOOL

AGENT ≠ SKILL

SKILL ≠ TOOL

MODULE ≠ ROUTER

AGENT ≠ ORCHESTRATOR

TOOL AVAILABLE ≠ TOOL ALLOWED

TOOL REQUEST ≠ TOOL AUTHORIZATION

RISK ≠ PERMISSION

PERMISSION ≠ EXECUTION AUTHORITY

VALIDATION ≠ APPROVAL

IMPLEMENTED CAPABILITY ≠ AUTONOMY AUTHORIZATION
```

---

# PENDIENTES

Pendientes funcionales principales:

1. revisar si los 30 Modules siguen siendo necesarios;
2. detectar posibles duplicados funcionales;
3. completar matriz Module → Command;
4. completar matriz Module → Agent;
5. completar matriz Module → Skill;
6. completar matriz Module → Model requirement;
7. completar matriz Module → Tool requirement;
8. completar matriz Module → Phase;
9. definir qué Modules aparecerán en la primera UI;
10. definir criterios de activación por Module;
11. reconciliar futuras modificaciones con `ROBERT_BUILD_ORDER`;
12. revisar este mapa durante implementación sin alterar silenciosamente la arquitectura canónica.

Estos pendientes no constituyen un gap arquitectónico Core por sí mismos.

---

# CONTROL DE VERSIONES

**Versión:** 0.1
**Fecha original:** Junio 2026
**Última normalización:** 31/08/2026

Cambio original:

Creación inicial del mapa de Modules de Robert con 30 Modules principales, prioridades, Risks y relación con Commands, Autonomy y arquitectura.

Normalización actual:

* alineación con `ROBERT_CANONICAL_MODEL v0.2`;
* Claude y ChatGPT clasificados exclusivamente como Models;
* Agents reconocidos como arquitectura aprobada;
* Skills incorporados como categoría independiente;
* Tools reconciliadas con `ROBERT_TOOL_ARCHITECTURE`;
* Module Routing subordinado al Orchestrator;
* Business Builder preservado bajo `DECISIÓN #001`;
* eliminación del concepto vigente de “Agents futuros”;
* separación entre prioridad funcional y Build Order;
* preservación de `AUTONOMY_LEVEL = 0`;
* preservación de `EXECUTION_AUTHORITY = NONE`.

---

# ESTADO DE APROBACIÓN

`ROBERT_MODULES v0.1` conserva naturaleza de mapa funcional base.

No se declara mediante esta normalización que los 30 Modules hayan recibido aprobación formal individual o colectiva.

Aprobación formal confirmada dentro de este documento:

```text
BUSINESS BUILDER — EMPRESAS COMPLETAS
DECISIÓN #001
```

La normalización canónica actual:

```text
DOES NOT CREATE
A NEW APPROVAL
```

y:

```text
DOES NOT CHANGE
THE SCOPE OF DECISIÓN #001
```

---

# RESUMEN EJECUTIVO

`ROBERT_MODULES v0.1` define el mapa funcional de Modules de Robert.

Los Modules representan áreas de capacidad.

No son:

* Layers;
* Models;
* Agents;
* Skills;
* Tools;
* Commands.

Robert mantiene 30 Modules iniciales como mapa funcional.

La taxonomía vigente distingue:

```text
MODULE
=
FUNCTIONAL DOMAIN

AGENT
=
SPECIALIST

SKILL
=
REUSABLE PROCEDURE

MODEL
=
INTELLIGENCE PROVIDER

TOOL
=
TECHNICAL / EXTERNAL CAPABILITY

ORCHESTRATOR
=
ROUTING AUTHORITY
```

Claude y ChatGPT se clasifican exclusivamente como Models.

Agents ya están definidos arquitectónicamente y no deben describirse como una capacidad arquitectónica futura.

Lo que continúa siendo futuro es su implementación autónoma.

Business Builder conserva su aprobación mediante:

```text
DECISIÓN #001
```

Los Modules deben crecer por fases y respetar siempre:

```text
CANONICAL MODEL
ORCHESTRATOR
SECURITY
PERMISSIONS
SCOPE
RISK
APPROVAL
VALIDATION
EXECUTION AUTHORITY
```

Estado técnico:

```text
TECHNICAL_IMPLEMENTATION = NOT STARTED

AUTONOMOUS_AGENTS = DISABLED

REAL_TOOL_EXECUTION = DISABLED

AUTONOMY_LEVEL = 0

EXECUTION_AUTHORITY = NONE
```

---

# ESTADO ACTUAL

```text
DOCUMENT: ROBERT_MODULES

VERSION: v0.1

STATUS:
BASE FUNCTIONAL MAP / CANONICALLY NORMALIZED

BUSINESS_BUILDER:
APPROVED THROUGH DECISIÓN #001

CANONICAL_ALIGNMENT:
ROBERT_CANONICAL_MODEL v0.2
DECISIÓN #030
CAMBIO #053

ORCHESTRATOR:
APPROVED

AGENT_ARCHITECTURE:
APPROVED

SKILL_ARCHITECTURE:
APPROVED

MODEL_INTERFACE:
APPROVED

MEMORY_ARCHITECTURE:
APPROVED

VALIDATION_ARCHITECTURE:
APPROVED

TOOL_ARCHITECTURE:
APPROVED

TECHNICAL_IMPLEMENTATION:
NOT STARTED

AUTONOMOUS_AGENTS:
DISABLED

REAL_TOOL_EXECUTION:
DISABLED

AUTONOMY_LEVEL:
0

EXECUTION_AUTHORITY:
NONE
```
