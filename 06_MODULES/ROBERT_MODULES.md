#ROBERT_MODULES — MAPA DE MÓDULOS DEL SISTEMA

Versión: 0.1  
Estado: Base inicial con Business Builder aprobado por el usuario
Última actualización: Junio 2026

---

# OBJETIVO

Definir los módulos principales de Robert.

Este documento existe para ordenar las capacidades funcionales del sistema.

Un módulo es un área funcional de Robert.

Un módulo no es lo mismo que:

- una capa interna;
    
- un comando;
    
- una herramienta externa;
    
- un agente;
    
- una automatización;
    
- una app conectada.
    

Los módulos representan **qué áreas puede trabajar Robert**.

Las capas explican **cómo funciona Robert por dentro**.

Los comandos explican **cómo el usuario activa funciones**.

Las herramientas explican **qué apps externas puede usar Robert**.

Los agentes explican **especialistas futuros dentro de módulos**.

---

# PRINCIPIO CENTRAL

Los módulos deben crecer por fases.

Robert no debe activar todos los módulos al mismo tiempo.

Primero se definen.

Después se prueban manualmente.

Después se conectan con comandos.

Después se integran al MVP.

Después pueden conectarse con herramientas.

Después pueden tener agentes especializados.

Regla:

Primero claridad. Después capacidad. Después automatización.

---

# RELACIÓN CON LA ARQUITECTURA

ROBERT_SYSTEM_ARCHITECTURE define 6 capas:

0. Identidad / Kernel
    
1. Memoria
    
2. Control
    
3. Capacidades
    
4. Gobierno
    
5. Presentación
    

Los módulos viven principalmente dentro de:

Capa 3 — Capacidades.

Los módulos deben respetar:

- Capa 2 — Control;
    
- Capa 4 — Gobierno;
    
- ROBERT_SECURITY_RULES;
    
- ROBERT_COMMANDS;
    
- ROBERT_CONTEXT_MASTER;
    
- ROBERT_PHASES.
    

Regla:

Ningún módulo puede ejecutar acciones fuera de autorización.

---

# DEFINICIÓN DE MÓDULO

Un módulo es una capacidad funcional de Robert.

Ejemplo:

- Ideas;
    
- Projects;
    
- Documents;
    
- Finance;
    
- Marketing;
    
- Security.
    

Un módulo sirve para organizar trabajo dentro de un área.

Cada módulo debe tener:

- nombre;
    
- propósito;
    
- función;
    
- estado;
    
- prioridad;
    
- comandos relacionados;
    
- documentos relacionados;
    
- nivel de riesgo;
    
- límites;
    
- posible evolución futura.
    

---

# DIFERENCIA ENTRE MODULES, LAYERS, TOOLS Y AGENTS

## MODULES

Son áreas funcionales de Robert.

Ejemplos:

- Ideas;
    
- Projects;
    
- Finance;
    
- Marketing;
    
- Documents;
    
- Security.
    

## LAYERS

Son capas internas de arquitectura.

Ejemplos:

- Identidad;
    
- Memoria;
    
- Control;
    
- Capacidades;
    
- Gobierno;
    
- Presentación.
    

## TOOLS

Son herramientas externas que Robert puede usar o conectar.

Ejemplos:

- Gmail;
    
- Google Calendar;
    
- Obsidian;
    
- Notion;
    
- Google Drive;
    
- Figma;
    
- Claude;
    
- ChatGPT.
    

## AGENTS

Son especialistas futuros que pueden operar dentro de un módulo.

Ejemplos:

- Agente financiero;
    
- Agente documental;
    
- Agente de marketing;
    
- Agente fiscal;
    
- Agente visual;
    
- Agente de investigación.
    

Regla:

No confundir módulos con agentes.

Un módulo es un área.

Un agente es un operador especializado futuro dentro de un área.

---

# MAPA GENERAL DE MÓDULOS

Los módulos principales de Robert son:

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

Base inicial pendiente de aprobación.

Los módulos todavía no están implementados.

Los módulos existen como mapa funcional inicial.

La prioridad actual no es programar módulos.

La prioridad actual es:

1. definir módulos;
    
2. conectarlos con documentos;
    
3. conectarlos con comandos;
    
4. priorizar módulos para MVP manual;
    
5. probarlos en sesiones reales;
    
6. después diseñar MVP técnico.
    

---

# MÓDULOS PRIORITARIOS PARA MVP MANUAL

Los módulos prioritarios para la etapa actual son:

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
    

Estos módulos permiten probar Robert sin programación.

---

# MÓDULOS PRIORITARIOS PARA MVP TÉCNICO

Los módulos prioritarios para una primera app técnica son:

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
    

Estos módulos deben aparecer primero en interfaz.

No se recomienda empezar con módulos complejos como Finance, Tax, Agents o Automation avanzada.

---

# MÓDULO 1 — ROBERT CORE

Propósito:

Representar el núcleo lógico de Robert.

Función:

Conectar contexto, memoria, comandos, documentos, decisiones, módulos, seguridad, autonomía y presentación visual.

Debe coordinar:

- intención del usuario;
    
- contexto;
    
- documento relacionado;
    
- comando detectado;
    
- módulo activo;
    
- riesgo;
    
- autorización;
    
- salida esperada.
    

Estado:

Base conceptual.

Prioridad:

Crítica.

Riesgo:

Alto si se define mal.

Límites:

Robert Core no debe convertirse en un módulo gigante donde todo se mezcle.

Debe coordinar, no reemplazar todos los módulos.

Documentos relacionados:

- ROBERT_CONTEXT_MASTER;
    
- ROBERT_SYSTEM_ARCHITECTURE;
    
- ROBERT_SECURITY_RULES;
    
- ROBERT_COMMANDS.
    

---

# MÓDULO 2 — COMMAND CENTER

Propósito:

Ser el centro de control operativo de Robert.

Función:

Mostrar y coordinar:

- comandos;
    
- estados;
    
- autorizaciones;
    
- modo activo;
    
- autonomía;
    
- riesgo;
    
- siguiente paso.
    

Debe permitir que el usuario controle Robert de forma clara.

Estado:

Base conceptual.

Prioridad:

Crítica.

Riesgo:

Medio.

Límites:

No debe ejecutar acciones sin pasar por Security Rules.

Documentos relacionados:

- ROBERT_COMMANDS;
    
- ROBERT_SECURITY_RULES;
    
- ROBERT_SYSTEM_ARCHITECTURE;
    
- ROBERT_VISUAL_REFERENCE.
    

---

# MÓDULO 3 — MEMORY

Propósito:

Conservar contexto útil.

Función:

Distinguir entre:

- contexto activo;
    
- contexto maestro;
    
- decisiones;
    
- información temporal;
    
- información permanente;
    
- ideas;
    
- tareas;
    
- referencias;
    
- reglas.
    

Estado:

Base inicial.

Prioridad:

Crítica.

Riesgo:

Medio.

Límites:

No debe guardar todo.

No debe guardar información sensible innecesaria.

Documentos relacionados:

- ROBERT_CONTEXT_MASTER;
    
- ROBERT_DECISIONS_LOG;
    
- ROBERT_SECURITY_RULES.
    

---

# MÓDULO 4 — IDEAS

Propósito:

Capturar, ordenar y desarrollar ideas.

Función:

Convertir ideas sueltas en:

- conceptos;
    
- proyectos;
    
- documentos;
    
- decisiones;
    
- planes;
    
- empresas;
    
- sistemas.
    

Estado:

Base inicial.

Prioridad:

Alta.

Riesgo:

Bajo.

Límites:

No toda idea es decisión.

No toda idea debe guardarse permanentemente.

Documentos relacionados:

- ROBERT_CONTEXT_MASTER;
    
- ROBERT_DECISIONS_LOG;
    
- ROBERT_MODULES.
    

---

# MÓDULO 5 — PROJECTS

Propósito:

Organizar proyectos.

Función:

Convertir ideas o trabajos en proyectos con:

- objetivo;
    
- estado;
    
- tareas;
    
- documentos;
    
- decisiones;
    
- fases;
    
- responsables;
    
- riesgos;
    
- próximos pasos.
    

Estado:

Base inicial.

Prioridad:

Alta.

Riesgo:

Bajo a medio.

Límites:

No debe cerrar fases ni proyectos sin autorización.

Documentos relacionados:

- ROBERT_PHASES;
    
- ROBERT_DECISIONS_LOG;
    
- ROBERT_CONTEXT_MASTER.
    

---

# # MÓDULO 6 — BUSINESS BUILDER

Propósito:

Ayudar al usuario a transformar ideas de negocio en estructuras empresariales completas, ordenadas y controladas.

Business Builder es el módulo de Robert encargado de apoyar la creación, desarrollo y organización de empresas desde una idea inicial hasta una estructura funcional por áreas.

---

# BUSINESS BUILDER — EMPRESAS COMPLETAS

## Estado

Aprobado por el usuario.

Fecha de aprobación: 22/06/2026

Decisión relacionada:

Business Builder — Empresas completas fue aprobado como capacidad de Robert para estructurar empresas completas por áreas funcionales.

---

## Función principal

Business Builder ayuda a convertir una idea de negocio en:

- modelo de negocio;
    
- estructura administrativa;
    
- plan financiero;
    
- estructura contable;
    
- análisis fiscal;
    
- estrategia de marketing;
    
- identidad de diseño;
    
- sistema de ventas;
    
- operación interna;
    
- documentos base;
    
- decisiones estratégicas;
    
- procesos organizados;
    
- plan de crecimiento;
    
- sistema empresarial estructurado.
    

---

## Definición

Business Builder no es una automatización empresarial completa todavía.

En la etapa actual, Business Builder funciona como una capacidad de planeación, estructura, documentación, simulación y análisis.

Robert puede ayudar a construir una empresa por áreas, pero no debe ejecutar acciones reales sin autorización, seguridad, revisión y fase correspondiente.

---

## Áreas que puede estructurar

Business Builder puede dividir una empresa en áreas funcionales como:

### 1. Administración

Organización general, estructura interna, roles, procesos, responsabilidades, políticas, tareas y operación administrativa.

### 2. Finanzas

Presupuestos, proyecciones, costos, ingresos, flujo de efectivo, rentabilidad, escenarios, análisis financiero y planeación de recursos.

### 3. Contabilidad

Catálogo conceptual de cuentas, registros, reportes, organización de información contable y estructura documental.

Robert no sustituye a un contador.

### 4. Fiscal

Identificación de temas fiscales, obligaciones posibles, riesgos, preguntas para revisar con especialista y organización de información.

Robert no sustituye a un asesor fiscal.

### 5. Marketing

Estrategia de mercado, cliente ideal, propuesta de valor, posicionamiento, campañas, contenido y comunicación.

### 6. Diseño

Identidad visual, estilo, marca, presentación, materiales, experiencia visual y coherencia gráfica.

### 7. Ventas

Proceso comercial, canales, guiones, seguimiento, embudo, CRM conceptual, precios, promociones y cierre.

### 8. Operaciones

Procesos internos, logística, entregas, proveedores, calidad, recursos, ejecución diaria y mejora continua.

### 9. Investigación

Análisis de mercado, competencia, tendencias, referencias, oportunidades, riesgos y validación de ideas.

### 10. Documentos

Creación de documentos base, planes, reportes, propuestas, presentaciones, manuales, checklists y estructuras internas.

### 11. Procesos

Diseño de procesos, flujos de trabajo, SOPs, responsabilidades, tareas repetitivas y mejora operativa.

### 12. Sistemas

Diseño conceptual de sistemas internos para operar, vender, organizar, medir y escalar una empresa.

---

## Qué puede hacer en el MVP manual

Durante el MVP manual, Business Builder puede:

- ordenar ideas de negocio;
    
- crear estructuras de empresa;
    
- preparar documentos base;
    
- proponer áreas funcionales;
    
- crear planes iniciales;
    
- simular escenarios;
    
- generar preguntas estratégicas;
    
- preparar prompts para Claude;
    
- crear borradores de procesos;
    
- detectar riesgos;
    
- separar decisiones importantes;
    
- preparar registros para Decisions Log;
    
- crear mapas de áreas;
    
- crear checklists;
    
- crear planes por etapas;
    
- preparar propuestas de estrategia;
    
- identificar qué información falta.
    

---

## Qué no puede hacer todavía

Durante el MVP manual, Business Builder no puede:

- crear empresas legalmente;
    
- hacer trámites reales;
    
- presentar declaraciones fiscales;
    
- tomar decisiones fiscales definitivas;
    
- tomar decisiones legales definitivas;
    
- tomar decisiones contables definitivas;
    
- tomar decisiones financieras definitivas;
    
- mover dinero;
    
- hacer pagos;
    
- contratar personas;
    
- enviar correos reales;
    
- publicar campañas reales;
    
- conectar herramientas externas;
    
- automatizar procesos reales;
    
- ejecutar acciones sin autorización;
    
- sustituir abogados, contadores, asesores fiscales o asesores financieros.
    

---

## Relación con otros módulos

Business Builder se conecta con:

- Administration;
    
- Finance;
    
- Accounting;
    
- Tax / Fiscal;
    
- Marketing;
    
- Design;
    
- Sales;
    
- Operations;
    
- Documents;
    
- Research;
    
- Analytics;
    
- Legal Reference;
    
- Decisions Log;
    
- Security;
    
- Automation futura;
    
- Apps Connector futuro;
    
- Visual Projection.
    

---

## Relación con ROBERT_SECURITY_RULES

Business Builder debe respetar siempre:

1. El usuario manda.
    
2. Robert no ejecuta acciones importantes sin autorización.
    
3. Robert no sustituye a profesionales legales, fiscales, contables o financieros.
    
4. Robert puede preparar, ordenar, simular y proponer.
    
5. Robert no debe ejecutar acciones externas sin alcance autorizado.
    
6. Robert debe separar sugerir, preparar y ejecutar.
    
7. Robert debe registrar decisiones importantes cuando afecten estructura, estrategia, módulos o fases.
    
8. Robert debe pedir confirmación reforzada cuando exista riesgo legal, fiscal, financiero, contable o de ejecución externa.
    

---

## Relación con ROBERT_PHASES

Business Builder existe como capacidad aprobada dentro de módulos, pero su desarrollo avanzado pertenece a una fase futura.

En la etapa actual:

- se puede definir;
    
- se puede probar manualmente;
    
- se puede usar para crear borradores;
    
- se puede conectar con prompts;
    
- se puede simular en sandbox;
    
- se puede usar como estructura estratégica.
    

No debe convertirse todavía en automatización, agente autónomo o app operativa completa.

---

## Relación con el MVP manual

En el MVP manual, Business Builder debe probarse con casos simples.

Ejemplo de prueba:

Idea de negocio  
↓  
Clasificación  
↓  
Áreas funcionales  
↓  
Documentos necesarios  
↓  
Riesgos  
↓  
Decisiones pendientes  
↓  
Siguiente paso

El objetivo no es ejecutar la empresa.

El objetivo es comprobar que Robert puede estructurar la empresa de forma clara, segura y útil.

---

## Riesgo

Nivel de riesgo:

Medio a alto.

Motivo:

Business Builder puede tocar áreas sensibles como finanzas, fiscal, contabilidad, legal, operaciones y decisiones empresariales importantes.

Regla:

Mientras Robert esté en MVP manual, Business Builder solo puede operar como apoyo estratégico, documental y de simulación.

---

## Prioridad

Alta a futuro.

Alta para la visión general de Robert.

Media para el MVP manual.

No debe adelantarse sobre seguridad, comandos, documentos maestros, sandbox ni MVP técnico.

---

## Límites

Business Builder no debe:

- automatizar empresas todavía;
    
- activar agentes empresariales autónomos;
    
- conectar herramientas reales sin autorización;
    
- ejecutar procesos reales;
    
- tomar decisiones críticas por el usuario;
    
- presentar información sensible como definitiva;
    
- sustituir revisión profesional;
    
- avanzar a fases futuras sin aprobación.
    

---

## Criterio de éxito

Business Builder funciona correctamente si Robert puede tomar una idea de negocio y convertirla en una estructura clara por áreas, documentos, decisiones, riesgos y siguientes pasos, sin ejecutar acciones reales ni quitarle control al usuario.

---

## Próximo paso recomendado

Probar Business Builder dentro del MVP manual con una idea de negocio real o simulada.

La prueba debe medir si Robert puede:

1. entender la idea;
    
2. dividirla por áreas;
    
3. identificar documentos necesarios;
    
4. detectar riesgos;
    
5. preparar decisiones;
    
6. proponer siguientes pasos;
    
7. mantenerse dentro de modo borrador o sandbox.


---

# MÓDULO 7 — ADMINISTRATION

Propósito:

Organizar tareas administrativas.

Función:

Ayudar con:

- procesos;
    
- documentos;
    
- organización;
    
- seguimiento;
    
- tareas;
    
- archivos;
    
- estructura operativa.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Medio.

Límites:

No debe modificar documentos reales sin autorización.

---

# MÓDULO 8 — FINANCE

Propósito:

Apoyar análisis financiero.

Función:

Puede ayudar con:

- presupuestos;
    
- escenarios;
    
- modelos;
    
- riesgos;
    
- reportes;
    
- análisis;
    
- preguntas para asesores;
    
- organización financiera.
    

Estado:

Futuro.

Prioridad:

Alta a futuro.

Riesgo:

Alto.

Límites:

No debe ejecutar compras, pagos, inversiones, apuestas u operaciones financieras.

No sustituye a asesor financiero.

Documentos relacionados:

- ROBERT_SECURITY_RULES;
    
- ROBERT_CONTEXT_MASTER.
    

---

# MÓDULO 9 — ACCOUNTING

Propósito:

Apoyar organización contable.

Función:

Puede ayudar con:

- clasificación de información;
    
- reportes;
    
- estructura de documentos;
    
- revisión conceptual;
    
- preparación de preguntas;
    
- borradores.
    

Estado:

Futuro.

Prioridad:

Media a alta.

Riesgo:

Alto.

Límites:

No debe emitir información contable definitiva sin revisión profesional.

---

# MÓDULO 10 — TAX / FISCAL

Propósito:

Apoyar organización fiscal.

Función:

Puede ayudar con:

- conceptos fiscales;
    
- checklists;
    
- organización de documentos;
    
- preguntas para asesores;
    
- escenarios;
    
- borradores.
    

Estado:

Futuro.

Prioridad:

Media a alta.

Riesgo:

Alto.

Límites:

No debe tomar decisiones fiscales definitivas.

No sustituye a contador o asesor fiscal.

---

# MÓDULO 11 — MARKETING

Propósito:

Crear y organizar estrategias de marketing.

Función:

Puede ayudar con:

- campañas;
    
- branding;
    
- contenido;
    
- audiencia;
    
- posicionamiento;
    
- mensajes;
    
- estrategia comercial;
    
- calendario de contenido.
    

Estado:

Futuro.

Prioridad:

Alta para Business Builder.

Riesgo:

Medio.

Límites:

No debe publicar contenido sin autorización.

---

# MÓDULO 12 — DESIGN

Propósito:

Desarrollar dirección visual, diseño y creatividad.

Función:

Puede ayudar con:

- identidad visual;
    
- interfaz;
    
- renders;
    
- presentaciones;
    
- materiales;
    
- conceptos;
    
- UX;
    
- referencias visuales.
    

Estado:

Activo conceptual.

Prioridad:

Alta.

Riesgo:

Bajo a medio.

Límites:

No debe cambiar ROBERT_VISUAL_REFERENCE oficial sin aprobación.

---

# MÓDULO 13 — SALES

Propósito:

Apoyar ventas y procesos comerciales.

Función:

Puede ayudar con:

- argumentos de venta;
    
- propuestas;
    
- scripts;
    
- CRM futuro;
    
- seguimiento;
    
- segmentación;
    
- estrategias.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Medio.

Límites:

No debe contactar clientes sin autorización.

---

# MÓDULO 14 — OPERATIONS

Propósito:

Organizar operaciones y procesos.

Función:

Puede ayudar con:

- procesos internos;
    
- flujos;
    
- SOPs;
    
- tareas repetitivas;
    
- organización;
    
- mejora operativa.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Medio.

Límites:

No debe automatizar operaciones reales sin validación.

---

# MÓDULO 15 — LEGAL REFERENCE

Propósito:

Ayudar a organizar información legal de referencia.

Función:

Puede ayudar con:

- conceptos;
    
- checklists;
    
- preguntas para abogados;
    
- organización de contratos;
    
- revisión de riesgos;
    
- borradores.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Alto.

Límites:

No sustituye a abogado.

No debe tomar decisiones legales definitivas.

---

# MÓDULO 16 — DOCUMENTS

Propósito:

Crear, ordenar y mantener documentos.

Función:

Puede ayudar con:

- documentos maestros;
    
- versiones;
    
- borradores;
    
- estructura;
    
- formato;
    
- actualizaciones;
    
- referencias;
    
- exportación.
    

Estado:

Activo conceptual.

Prioridad:

Crítica.

Riesgo:

Medio.

Límites:

No debe modificar documentos oficiales sin autorización.

Documentos relacionados:

- Todos los documentos maestros.
    

---

# MÓDULO 17 — RESEARCH

Propósito:

Investigar y organizar información.

Función:

Puede ayudar con:

- preguntas;
    
- fuentes;
    
- comparaciones;
    
- análisis;
    
- reportes;
    
- resúmenes;
    
- búsqueda de información.
    

Estado:

Futuro.

Prioridad:

Alta.

Riesgo:

Medio.

Límites:

Debe citar cuando use información externa.

Debe distinguir hechos, opiniones e inferencias.

---

# MÓDULO 18 — ANALYTICS

Propósito:

Analizar datos, patrones y métricas.

Función:

Puede ayudar con:

- tablas;
    
- métricas;
    
- reportes;
    
- dashboards;
    
- interpretaciones;
    
- escenarios;
    
- comparaciones.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Medio.

Límites:

No debe interpretar datos críticos sin contexto.

---

# MÓDULO 19 — AUTOMATION

Propósito:

Diseñar automatizaciones futuras.

Función:

Puede ayudar con:

- flujos;
    
- triggers;
    
- acciones;
    
- permisos;
    
- riesgos;
    
- herramientas;
    
- pruebas;
    
- logs.
    

Estado:

Futuro.

Prioridad:

Alta a futuro.

Riesgo:

Alto.

Límites:

No debe activar automatizaciones reales sin autorización y sandbox.

---

# MÓDULO 20 — APPS CONNECTOR

Propósito:

Gestionar conexión futura con herramientas externas.

Función:

Puede ayudar con:

- mapa de apps;
    
- permisos;
    
- estados de conexión;
    
- lectura;
    
- escritura;
    
- riesgos;
    
- desconexión;
    
- sandbox.
    

Estado:

Futuro.

Prioridad:

Alta a futuro.

Riesgo:

Alto.

Límites:

No debe conectar apps reales sin autorización.

---

# MÓDULO 21 — CALENDAR

Propósito:

Gestionar calendario futuro.

Función:

Puede ayudar con:

- eventos;
    
- agenda;
    
- recordatorios;
    
- planeación;
    
- disponibilidad;
    
- reuniones.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Alto si crea o modifica eventos.

Límites:

No debe crear, mover o cancelar eventos sin autorización.

---

# MÓDULO 22 — EMAIL

Propósito:

Gestionar correo futuro.

Función:

Puede ayudar con:

- borradores;
    
- resúmenes;
    
- clasificación;
    
- respuestas propuestas;
    
- seguimiento;
    
- búsqueda.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Alto.

Límites:

No debe enviar correos sin autorización.

---

# MÓDULO 23 — TASKS

Propósito:

Gestionar tareas.

Función:

Puede ayudar con:

- pendientes;
    
- prioridades;
    
- fechas;
    
- responsables;
    
- seguimiento;
    
- next steps;
    
- checklist.
    

Estado:

Base inicial.

Prioridad:

Alta para MVP manual.

Riesgo:

Bajo a medio.

Límites:

No debe crear tareas en apps externas sin autorización.

---

# MÓDULO 24 — VOICE

Propósito:

Permitir interacción por voz en el futuro.

Función:

Puede ayudar con:

- comandos por voz;
    
- dictado;
    
- respuesta hablada;
    
- confirmación de acciones;
    
- control manos libres.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Medio a alto.

Límites:

Los comandos de voz críticos deben confirmarse.

---

# MÓDULO 25 — CODE / DEVELOPMENT

Propósito:

Apoyar desarrollo técnico de Robert.

Función:

Puede ayudar con:

- arquitectura técnica;
    
- código;
    
- repositorios;
    
- debugging;
    
- prototipos;
    
- despliegue;
    
- documentación técnica.
    

Estado:

Futuro.

Prioridad:

Alta para MVP técnico.

Riesgo:

Alto.

Límites:

No debe ejecutar, borrar, sobrescribir o desplegar código sin autorización.

---

# MÓDULO 26 — KNOWLEDGE BASE

Propósito:

Organizar conocimiento.

Función:

Puede ayudar con:

- notas;
    
- referencias;
    
- aprendizaje;
    
- documentos;
    
- conceptos;
    
- resúmenes;
    
- relaciones.
    

Estado:

Base inicial.

Prioridad:

Alta.

Riesgo:

Bajo a medio.

Límites:

No debe guardar todo sin criterio.

---

# MÓDULO 27 — SECURITY

Propósito:

Proteger el sistema.

Función:

Debe revisar:

- riesgos;
    
- permisos;
    
- autorización;
    
- privacidad;
    
- credenciales;
    
- acciones críticas;
    
- fases;
    
- autonomía;
    
- herramientas.
    

Estado:

Base inicial.

Prioridad:

Crítica.

Riesgo:

Crítico si falla.

Límites:

Security tiene prioridad sobre velocidad, diseño, autonomía, automatización o conveniencia.

---

# MÓDULO 28 — DECISIONS LOG

Propósito:

Registrar decisiones.

Función:

Puede ayudar con:

- decisiones propuestas;
    
- decisiones pendientes;
    
- decisiones aprobadas;
    
- motivo;
    
- impacto;
    
- fecha;
    
- documentos relacionados;
    
- siguiente paso.
    

Estado:

Base inicial.

Prioridad:

Crítica.

Riesgo:

Medio.

Límites:

No debe registrar decisiones como aprobadas sin confirmación del usuario.

---

# MÓDULO 29 — LEARNING SYSTEM

Propósito:

Permitir que Robert mejore con el uso.

Función:

Puede ayudar con:

- patrones;
    
- preferencias;
    
- aprendizajes;
    
- mejoras;
    
- ajustes;
    
- retroalimentación;
    
- evolución del sistema.
    

Estado:

Futuro.

Prioridad:

Media.

Riesgo:

Medio.

Límites:

No debe guardar información sensible innecesaria.

---

# MÓDULO 30 — VISUAL PROJECTION

Propósito:

Mostrar información visualmente.

Función:

Puede ayudar con:

- mapas;
    
- dashboards;
    
- nodos;
    
- módulos;
    
- documentos;
    
- comandos;
    
- decisiones;
    
- apps;
    
- autonomía;
    
- seguridad;
    
- flujos.
    

Estado:

Base visual en revisión.

Prioridad:

Alta.

Riesgo:

Medio.

Límites:

No debe inventar capacidades que no existan en arquitectura.

---

# RELACIÓN ENTRE MÓDULOS Y COMANDOS

Los comandos activan funciones dentro de módulos.

Ejemplos:

RESUMEN:

- Memory;
    
- Knowledge Base;
    
- Documents.
    

CONCLUSION:

- Prompts;
    
- Knowledge Base;
    
- Documents.
    

DETENTE:

- Security;
    
- Command Center;
    
- Robert Core.
    

MODO_SANDBOX:

- Security;
    
- Automation;
    
- Apps Connector;
    
- Code / Development.
    

INFORME_ACCIONES:

- Decisions Log;
    
- Security;
    
- Memory.
    

CLASIFICAR:

- Knowledge Base;
    
- Documents;
    
- Memory.
    

ACTUALIZA:

- Documents;
    
- Security;
    
- Decisions Log.
    

---

# RELACIÓN ENTRE MÓDULOS Y AUTONOMÍA

La autonomía no es un módulo único.

La autonomía vive entre:

- Control;
    
- Capacidades;
    
- Gobierno.
    

Pero algunos módulos participan directamente:

Security:

- verifica riesgo y autorización.
    

Command Center:

- muestra modo activo y comandos.
    

Documents:

- permite autonomía documental.
    

Automation:

- diseña automatizaciones futuras.
    

Apps Connector:

- controla conexión con herramientas.
    

Decisions Log:

- registra acciones importantes.
    

Visual Projection:

- muestra estado de autonomía.
    

Regla:

La autonomía debe pasar por Security antes de cualquier acción importante.

---

# NIVELES DE RIESGO POR MÓDULO

Nivel bajo:

- Ideas;
    
- Knowledge Base;
    
- Visual Projection;
    
- Research básico;
    
- Design conceptual.
    

Nivel medio:

- Projects;
    
- Documents;
    
- Tasks;
    
- Decisions Log;
    
- Analytics;
    
- Marketing;
    
- Operations.
    

Nivel alto:

- Finance;
    
- Accounting;
    
- Tax / Fiscal;
    
- Legal Reference;
    
- Email;
    
- Calendar;
    
- Apps Connector;
    
- Automation;
    
- Code / Development.
    

Nivel crítico:

- Security si falla;
    
- cualquier módulo usando credenciales;
    
- cualquier módulo ejecutando acciones externas;
    
- cualquier módulo manejando dinero, datos sensibles o decisiones legales/fiscales.
    

---

# PRIORIDAD DE IMPLEMENTACIÓN

## Prioridad 1 — Base manual

- Robert Core
    
- Command Center
    
- Memory
    
- Documents
    
- Knowledge Base
    
- Security
    
- Decisions Log
    
- Ideas
    
- Projects
    
- Tasks
    

## Prioridad 2 — Visual y organización

- Visual Projection
    
- Design
    
- Research
    
- Analytics
    

## Prioridad 3 — Business Builder

- Business Builder
    
- Administration
    
- Marketing
    
- Sales
    
- Operations
    

## Prioridad 4 — Áreas sensibles

- Finance
    
- Accounting
    
- Tax / Fiscal
    
- Legal Reference
    

## Prioridad 5 — Integraciones y ejecución futura

- Apps Connector
    
- Email
    
- Calendar
    
- Automation
    
- Voice
    
- Code / Development
    

## Prioridad 6 — Aprendizaje y expansión

- Learning System
    
- agentes futuros dentro de módulos
    

---

# REGLAS MAESTRAS DE MÓDULOS

1. Ningún módulo puede saltarse Security Rules.
    
2. Ningún módulo puede ejecutar acciones externas sin autorización.
    
3. Ningún módulo puede modificar documentos oficiales sin aprobación.
    
4. Ningún módulo puede registrar decisiones aprobadas sin confirmación.
    
5. Ningún módulo puede conectarse a herramientas reales sin permiso.
    
6. Ningún módulo puede activar automatizaciones reales antes de sandbox.
    
7. Ningún módulo sensible puede operar sin revisión.
    
8. Los módulos deben crecer por fases.
    
9. Los módulos deben conectarse con comandos.
    
10. Los módulos deben respetar la arquitectura de 6 capas.
    
11. Los módulos deben distinguir preparación, simulación y ejecución.
    
12. Los módulos deben mostrar riesgo cuando aplique.
    
13. Los módulos deben registrar acciones importantes.
    
14. Los módulos no deben duplicarse innecesariamente.
    
15. Los módulos deben servir al usuario, no complicar el sistema.
    

---

# PENDIENTES

Pendientes principales:

1. Revisar si los 30 módulos son necesarios.
    
2. Definir módulos del MVP manual.
    
3. Definir módulos del MVP técnico.
    
4. Crear relación módulo → comando.
    
5. Crear relación módulo → documento.
    
6. Crear relación módulo → fase.
    
7. Definir qué módulos aparecen en el dashboard inicial.
    
8. Definir qué módulos pueden tener agentes futuros.
    
9. Definir qué módulos pueden usar herramientas externas.
    
10. Definir criterios de activación por módulo.
    

---

# CONTROL DE VERSIONES

Versión: 0.1  
Fecha: Junio 2026  
Cambio principal: Creación inicial del mapa de módulos de Robert con 30 módulos principales, prioridades, riesgos y relación con comandos, autonomía y arquitectura.  
Estado: Base inicial pendiente de aprobación.

---

# DECISIÓN PENDIENTE

Decisión pendiente:

Aprobar ROBERT_MODULES v0.1 como mapa inicial de módulos de Robert.

Motivo:

Robert necesita un mapa funcional claro para organizar capacidades, conectar comandos, definir MVP manual, preparar MVP técnico y evitar confundir módulos con capas, herramientas o agentes.

Estado:

Pendiente de aprobación.

Próximo paso sugerido:

Revisar si los módulos actuales son suficientes, eliminar duplicados, priorizar los módulos del MVP manual y confirmar si ROBERT_MODULES v0.1 queda aprobado como base inicial.

---

# RESUMEN EJECUTIVO

ROBERT_MODULES v0.1 define el mapa inicial de módulos funcionales de Robert.

Los módulos representan áreas de capacidad.

No son capas internas, comandos, herramientas externas ni agentes.

Robert tiene 30 módulos iniciales.

Los módulos prioritarios para MVP manual son:

- Robert Core;
    
- Command Center;
    
- Memory;
    
- Ideas;
    
- Projects;
    
- Documents;
    
- Knowledge Base;
    
- Security;
    
- Decisions Log;
    
- Tasks.
    

La regla central es:

Los módulos deben crecer por fases y siempre respetar Security Rules.

Ningún módulo puede ejecutar acciones importantes sin autorización.

La autonomía controlada no es un módulo aislado.

La autonomía vive entre Control, Capacidades y Gobierno, y se expresa a través de módulos como Security, Command Center, Documents, Automation, Apps Connector, Decisions Log y Visual Projection.
