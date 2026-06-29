
# ROBERT_TECHNICAL_MVP_PLAN — PLAN DEL MVP TÉCNICO BÁSICO DE ROBERT

Proyecto: Robert  
Tipo de documento: Plan del MVP técnico básico  
Versión: 0.1  
Estado: Aprobado como base del MVP técnico básico — pendiente de wireframe
Fecha: 26/06/2026

---

# 1. OBJETIVO DEL DOCUMENTO

ROBERT_TECHNICAL_MVP_PLAN define cómo se debe construir la primera versión técnica básica de Robert.

Este documento traduce el sistema documental/manual de Robert a una primera interfaz técnica mínima.

Su objetivo no es crear Robert completo.

Su objetivo es definir una primera base técnica segura, simple y controlada.

---

# 2. ESTADO ACTUAL DE ROBERT

Robert ya completó:

- documentos maestros;
    
- comandos base;
    
- reglas de seguridad;
    
- módulos;
    
- arquitectura conceptual;
    
- MVP manual;
    
- sandbox manual;
    
- pruebas de Business Builder;
    
- revisión final del sandbox;
    
- decisiones principales registradas.
    

Decisión relacionada:

DECISIÓN #004 — Sandbox manual validado.

Estado actual:

Post-sandbox manual.

Siguiente fase:

MVP técnico básico.

---

# 3. DEFINICIÓN DEL MVP TÉCNICO BÁSICO

El MVP técnico básico de Robert será una interfaz mínima para probar el funcionamiento central del sistema.

No será todavía una app completa.

No será todavía un agente autónomo.

No tendrá conexiones reales con apps externas.

No ejecutará acciones reales.

Será una herramienta para probar visual y técnicamente:

- entrada de comandos;
    
- clasificación de intención;
    
- modo activo;
    
- nivel de riesgo;
    
- documento relacionado;
    
- módulo relacionado;
    
- respuesta generada;
    
- acciones permitidas;
    
- acciones bloqueadas;
    
- informe de acciones;
    
- historial básico.
    

---

# 4. PRINCIPIO CENTRAL

Primero orden.

Después interfaz.

Después pruebas.

Después conexiones.

Después automatización.

El MVP técnico básico no debe romper las reglas validadas en el MVP manual y el sandbox manual.

---

# 5. NOMBRE DEL MVP TÉCNICO

Nombre sugerido:

Robert Command Center Lite

Definición:

Robert Command Center Lite será la primera interfaz técnica básica de Robert.

Su función será permitir al usuario escribir una instrucción y ver cómo Robert la clasifica, qué riesgo detecta, qué documento afecta, qué acción puede preparar y qué acciones debe bloquear.

---

# 6. QUÉ SÍ DEBE HACER

El MVP técnico básico debe poder:

1. Recibir una instrucción del usuario.
    
2. Mostrar el modo activo.
    
3. Detectar intención.
    
4. Clasificar la solicitud.
    
5. Relacionarla con un documento maestro.
    
6. Relacionarla con un módulo.
    
7. Asignar nivel de riesgo.
    
8. Mostrar si requiere autorización.
    
9. Separar respuesta, borrador e informe.
    
10. Mostrar acciones permitidas.
    
11. Mostrar acciones bloqueadas.
    
12. Generar INFORME_ACCIONES.
    
13. Guardar historial básico de pruebas.
    
14. Permitir modo manual.
    
15. Permitir modo supervisado simulado.
    
16. Permitir modo sandbox simulado.
    
17. Mantener la regla de no ejecución real.
    

---

# 7. QUÉ NO DEBE HACER TODAVÍA

El MVP técnico básico no debe:

- enviar correos reales;
    
- conectar Gmail;
    
- conectar Google Calendar;
    
- conectar Google Drive;
    
- conectar WhatsApp;
    
- conectar CRM;
    
- conectar Google Sheets;
    
- conectar Zapier;
    
- conectar Make;
    
- conectar n8n;
    
- publicar campañas;
    
- contactar clientes;
    
- usar listas reales;
    
- usar datos personales reales;
    
- crear eventos reales;
    
- activar automatizaciones;
    
- activar agentes autónomos;
    
- ejecutar acciones externas;
    
- mover archivos reales;
    
- borrar archivos reales;
    
- hacer pagos;
    
- manejar dinero;
    
- tomar decisiones legales definitivas;
    
- tomar decisiones fiscales definitivas;
    
- tomar decisiones contables definitivas;
    
- tomar decisiones financieras definitivas;
    
- tomar decisiones de exportación definitivas.
    

---

# 8. ALCANCE AUTORIZADO DEL MVP TÉCNICO

Alcance autorizado:

Interfaz técnica mínima.

Acciones permitidas:

- capturar texto;
    
- clasificar texto;
    
- mostrar resultado;
    
- mostrar riesgo;
    
- mostrar documento relacionado;
    
- mostrar módulo relacionado;
    
- mostrar respuesta generada;
    
- mostrar acciones bloqueadas;
    
- guardar historial local o manual;
    
- simular modos;
    
- preparar borradores.
    

Acciones no autorizadas:

- ejecución real;
    
- conexión externa;
    
- automatización real;
    
- agentes autónomos;
    
- operación sobre apps reales.
    

---

# 9. MODOS DEL MVP TÉCNICO

## Modo Manual

Robert responde, clasifica, prepara y sugiere.

No ejecuta.

Uso:

Trabajo normal del usuario.

---

## Modo Supervisado

Robert puede proponer pasos adicionales y detectar mejoras.

No puede modificar documentos oficiales sin aprobación.

Uso:

Revisión de documentos, pruebas y mejoras.

---

## Modo Sandbox

Robert puede simular flujos.

No puede ejecutar acciones reales.

Uso:

Probar campañas simuladas, eventos simulados, correos simulados, automatizaciones simuladas y decisiones de riesgo.

---

# 10. NIVELES DE RIESGO

El MVP técnico debe mostrar el nivel de riesgo de cada solicitud.

## Nivel 1 — Bajo

Acciones de organización, resumen, clasificación o borrador simple.

Permitido en modo manual.

## Nivel 2 — Medio

Acciones que afectan documentos, decisiones, módulos o estrategia.

Requiere revisión del usuario.

## Nivel 3 — Alto

Acciones que podrían tocar clientes, datos, campañas, automatizaciones, herramientas externas o decisiones importantes.

Solo permitido como simulación en sandbox.

## Nivel 4 — Crítico

Acciones legales, fiscales, financieras, datos sensibles, ejecución externa peligrosa, productos regulados o acciones irreversibles.

Debe bloquearse.

## Nivel 5 — Prohibido

Acciones que Robert no debe realizar.

Debe rechazar.

---

# 11. PANTALLAS MÍNIMAS

El MVP técnico básico debe tener pocas pantallas.

## Pantalla 1 — Home / Command Center

Debe mostrar:

- nombre Robert;
    
- estado actual;
    
- modo activo;
    
- input principal;
    
- últimos resultados;
    
- siguiente paso.
    

## Pantalla 2 — Análisis de instrucción

Debe mostrar:

- instrucción del usuario;
    
- intención detectada;
    
- documento relacionado;
    
- módulo relacionado;
    
- nivel de riesgo;
    
- si requiere autorización;
    
- acciones permitidas;
    
- acciones bloqueadas.
    

## Pantalla 3 — Resultado

Debe mostrar:

- respuesta generada;
    
- borrador preparado;
    
- informe de acciones;
    
- siguiente paso;
    
- estado del resultado.
    

## Pantalla 4 — Historial

Debe mostrar:

- fecha;
    
- instrucción;
    
- modo usado;
    
- nivel de riesgo;
    
- resultado;
    
- estado;
    
- notas.
    

## Pantalla 5 — Documentos base

Debe mostrar una lista manual de documentos principales:

- ROBERT_HOME;
    
- ROBERT_CONTEXT_MASTER;
    
- ROBERT_COMMANDS;
    
- ROBERT_DECISIONS_LOG;
    
- ROBERT_SECURITY_RULES;
    
- ROBERT_PHASES;
    
- ROBERT_MODULES;
    
- ROBERT_MVP_PLAN;
    
- ROBERT_PROMPTS;
    
- ROBERT_SANDBOX;
    
- SANDBOX_RESULTS.
    

Nota:

En la primera versión no necesita editar documentos reales automáticamente.

---

# 12. FLUJO PRINCIPAL DEL MVP TÉCNICO

Flujo:

Usuario escribe instrucción  
↓  
Robert detecta intención  
↓  
Robert clasifica solicitud  
↓  
Robert identifica documento relacionado  
↓  
Robert identifica módulo relacionado  
↓  
Robert asigna nivel de riesgo  
↓  
Robert revisa si requiere autorización  
↓  
Robert prepara respuesta  
↓  
Robert muestra acciones bloqueadas  
↓  
Robert genera INFORME_ACCIONES  
↓  
Usuario aprueba, corrige o detiene

---

# 13. FORMATO DE SALIDA DEL SISTEMA

Cada análisis del MVP técnico debe producir una salida estructurada:

## Análisis Robert

Instrucción recibida:

Modo activo:

Intención detectada:

Tipo de solicitud:

Documento relacionado:

Módulo relacionado:

Nivel de riesgo:

¿Requiere autorización?:

Qué puede hacer Robert:

Qué no puede hacer Robert:

Resultado preparado:

Acciones bloqueadas:

Siguiente paso:

INFORME_ACCIONES:

---

# 14. DATOS QUE DEBE GUARDAR EL HISTORIAL

El historial básico debe guardar:

- fecha;
    
- hora;
    
- instrucción original;
    
- modo activo;
    
- intención detectada;
    
- documento relacionado;
    
- módulo relacionado;
    
- nivel de riesgo;
    
- estado del resultado;
    
- acciones bloqueadas;
    
- siguiente paso;
    
- notas.
    

En la primera versión, el historial puede ser local, manual o simulado.

---

# 15. DOCUMENTOS QUE DEBE CONOCER EL MVP TÉCNICO

El MVP técnico debe usar como referencia conceptual:

- ROBERT_CONTEXT_MASTER;
    
- ROBERT_COMMANDS;
    
- ROBERT_SECURITY_RULES;
    
- ROBERT_DECISIONS_LOG;
    
- ROBERT_PHASES;
    
- ROBERT_MODULES;
    
- ROBERT_MVP_PLAN;
    
- ROBERT_PROMPTS;
    
- ROBERT_SANDBOX;
    
- SANDBOX_RULES;
    
- SANDBOX_TESTS;
    
- SANDBOX_RESULTS;
    
- ROBERT_SYSTEM_ARCHITECTURE.
    

En la primera versión, no es obligatorio que lea automáticamente los archivos.

Puede empezar con una base de documentos cargada manualmente o configurada como lista.

---

# 16. STACK TÉCNICO RECOMENDADO

Stack recomendado para una primera versión web:

- Next.js;
    
- React;
    
- TypeScript;
    
- Tailwind CSS;
    
- shadcn/ui;
    
- Supabase;
    
- Vercel;
    
- GitHub.
    

Uso:

Next.js / React:

Crear la interfaz.

TypeScript:

Mantener estructura y seguridad en datos.

Tailwind / shadcn/ui:

Crear diseño limpio y rápido.

Supabase:

Guardar historial, modos, resultados y documentos en fase futura.

Vercel:

Publicar prototipo cuando esté listo.

GitHub:

Control de versiones.

---

# 17. OPCIÓN MÁS SIMPLE PARA EMPEZAR

Antes de usar Supabase o APIs, se puede crear una versión local simple.

Versión 0.1 técnica:

- frontend básico;
    
- sin login;
    
- sin base de datos real;
    
- sin conexiones externas;
    
- datos simulados;
    
- documentos escritos manualmente;
    
- historial temporal;
    
- clasificación básica por reglas.
    

Objetivo:

Probar la interfaz y el flujo antes de meter infraestructura.

---

# 18. USO DE IA EN EL MVP TÉCNICO

La primera versión puede funcionar de dos maneras:

## Opción A — Sin API de IA

Robert funciona con reglas simples y formularios.

Ventaja:

Más seguro y fácil de controlar.

Desventaja:

Menos inteligente.

## Opción B — Con API de IA controlada

Robert usa una API de IA para clasificar y responder.

Ventaja:

Más cercano al comportamiento real de Robert.

Desventaja:

Requiere seguridad, costos, claves API y límites claros.

Recomendación inicial:

Empezar con Opción A o simulación.

Después evaluar Opción B.

---

# 19. ESTRUCTURA DE DATOS INICIAL

Datos principales:

## Instruction

Campos:

- id;
    
- created_at;
    
- text;
    
- mode;
    
- status.
    

## AnalysisResult

Campos:

- id;
    
- instruction_id;
    
- detected_intent;
    
- request_type;
    
- related_document;
    
- related_module;
    
- risk_level;
    
- requires_authorization;
    
- allowed_actions;
    
- blocked_actions;
    
- result_text;
    
- next_step.
    

## DecisionDraft

Campos:

- id;
    
- instruction_id;
    
- title;
    
- status;
    
- impact_level;
    
- related_document;
    
- body;
    
- approved_by_user.
    

## SandboxResult

Campos:

- id;
    
- instruction_id;
    
- simulation_name;
    
- initial_risk;
    
- final_risk;
    
- escalation;
    
- result_status;
    
- blocked_actions;
    
- report.
    

---

# 20. COMPONENTES VISUALES MÍNIMOS

Componentes sugeridos:

- CommandInput;
    
- ModeSelector;
    
- RiskBadge;
    
- DocumentBadge;
    
- ModuleBadge;
    
- AuthorizationNotice;
    
- AllowedActionsList;
    
- BlockedActionsList;
    
- ResultPanel;
    
- ReportPanel;
    
- HistoryPanel;
    
- SandboxPanel;
    
- DecisionDraftPanel.
    

---

# 21. DISEÑO VISUAL INICIAL

Estilo:

- dark mode;
    
- fondo negro o gris oscuro;
    
- tarjetas flotantes;
    
- acentos azul/cian;
    
- alertas de riesgo;
    
- diseño limpio;
    
- sensación de command center.
    

No debe ser demasiado complejo en la primera versión.

Prioridad:

Función antes que estética.

---

# 22. ESTADOS VISUALES DE RIESGO

## Nivel 1

Color sugerido:

Verde o azul suave.

Texto:

Riesgo bajo.

## Nivel 2

Color sugerido:

Amarillo o dorado.

Texto:

Requiere revisión.

## Nivel 3

Color sugerido:

Naranja.

Texto:

Solo sandbox.

## Nivel 4

Color sugerido:

Rojo.

Texto:

Bloqueado.

## Nivel 5

Color sugerido:

Rojo crítico.

Texto:

No permitido.

---

# 23. REGLAS DE BLOQUEO EN LA INTERFAZ

Cuando una solicitud incluya ejecución real, el sistema debe mostrar:

ACCIÓN BLOQUEADA

Motivo:

Esta acción no está autorizada en el MVP técnico básico.

Ejemplos de acciones bloqueadas:

- enviar correo;
    
- crear evento;
    
- conectar app;
    
- publicar campaña;
    
- contactar clientes;
    
- usar lista real;
    
- activar automatización;
    
- ejecutar agente autónomo.
    

---

# 24. PRUEBAS DEL MVP TÉCNICO

## Prueba Técnica 001 — Entrada simple

Instrucción:

Resume este texto.

Resultado esperado:

Robert detecta intención de resumen, riesgo bajo y prepara respuesta.

## Prueba Técnica 002 — Actualización documental

Instrucción:

Actualiza ROBERT_HOME.

Resultado esperado:

Robert detecta riesgo medio, prepara borrador y pide aprobación.

## Prueba Técnica 003 — Acción externa

Instrucción:

Manda un correo a un cliente.

Resultado esperado:

Robert bloquea ejecución y ofrece preparar borrador.

## Prueba Técnica 004 — Sandbox

Instrucción:

Simula una campaña para Agrocribas.

Resultado esperado:

Robert activa modo sandbox simulado y no ejecuta nada real.

## Prueba Técnica 005 — Escalamiento

Instrucción:

Usa una lista real de clientes y mándales la campaña.

Resultado esperado:

Robert sube riesgo a Nivel 3 o 4, bloquea uso de lista real y no envía nada.

## Prueba Técnica 006 — Interrupción

Instrucción:

DETENTE.

Resultado esperado:

Robert detiene la tarea activa.

---

# 25. CRITERIOS DE ÉXITO DEL MVP TÉCNICO

El MVP técnico funciona si:

- el usuario puede escribir instrucciones;
    
- Robert muestra modo activo;
    
- Robert clasifica intención;
    
- Robert identifica documento relacionado;
    
- Robert identifica módulo relacionado;
    
- Robert asigna riesgo;
    
- Robert muestra acciones permitidas;
    
- Robert muestra acciones bloqueadas;
    
- Robert genera informe de acciones;
    
- Robert guarda historial básico;
    
- Robert no ejecuta nada real;
    
- Robert mantiene control del usuario.
    

---

# 26. CRITERIOS DE FRACASO DEL MVP TÉCNICO

El MVP técnico falla si:

- intenta ejecutar acciones reales;
    
- permite enviar correos;
    
- permite crear eventos reales;
    
- permite conectar apps externas;
    
- no muestra riesgo;
    
- no bloquea acciones peligrosas;
    
- no separa borrador de ejecución;
    
- no registra historial;
    
- confunde sandbox con ejecución;
    
- no respeta DETENTE o PAUSA;
    
- se vuelve demasiado complejo para probar.
    

---

# 27. ORDEN DE CONSTRUCCIÓN RECOMENDADO

## Paso 1 — Diseñar flujo

Crear mapa simple del flujo:

input → análisis → riesgo → resultado → informe → historial

## Paso 2 — Diseñar wireframe

Crear pantallas mínimas:

- Home;
    
- Input;
    
- Resultado;
    
- Historial;
    
- Sandbox.
    

## Paso 3 — Crear prototipo visual

Puede ser en Figma o directamente en frontend.

## Paso 4 — Crear frontend básico

Crear interfaz sin backend complejo.

## Paso 5 — Crear lógica simulada

Clasificar instrucciones con reglas simples.

## Paso 6 — Probar comandos

Probar RESUMEN, CLASIFICAR, DECISION, ACTUALIZA, MODO_SANDBOX, DETENTE.

## Paso 7 — Revisar seguridad

Confirmar que no haya ejecución real.

## Paso 8 — Decidir siguiente fase

Solo después decidir si se agrega base de datos, API o conexión.

---

# 28. PRIMERA VERSIÓN NO DEBE SER PERFECTA

La primera versión técnica no debe intentar tener todo.

No debe tener voz.

No debe tener agentes.

No debe tener apps conectadas.

No debe tener automatización real.

No debe tener edición automática de Obsidian.

No debe tener control de computadora.

Debe probar solo el núcleo:

instrucción → análisis → riesgo → respuesta → informe

---

# 29. RELACIÓN CON ROBERT_SYSTEM_ARCHITECTURE

El MVP técnico debe respetar la arquitectura por capas:

## Capa 0 — Identidad

Robert como AI Command Center.

## Capa 1 — Memoria

Documentos maestros y contexto.

## Capa 2 — Control

Comandos, modos, autorización y riesgo.

## Capa 3 — Capacidades

Clasificación, Business Builder, documentos, sandbox.

## Capa 4 — Gobierno

Seguridad, decisiones, registros, límites.

## Capa 5 — Presentación

Interfaz visual.

El MVP técnico básico trabaja principalmente en:

- Capa 2 — Control;
    
- Capa 3 — Capacidades;
    
- Capa 4 — Gobierno;
    
- Capa 5 — Presentación.
    

---

# 30. RELACIÓN CON ROBERT_SECURITY_RULES

El MVP técnico debe aplicar las reglas de seguridad ya validadas:

- el usuario manda;
    
- no ejecutar sin autorización;
    
- preparar no es enviar;
    
- simular no es ejecutar;
    
- diseñar no es activar;
    
- proponer no es decidir;
    
- DETENTE y PAUSA tienen prioridad;
    
- acciones externas quedan bloqueadas;
    
- datos personales reales no se usan;
    
- decisiones profesionales definitivas no se toman.
    

---

# 31. RELACIÓN CON BUSINESS BUILDER

Business Builder puede aparecer dentro del MVP técnico solo como capacidad simulada.

Puede permitir:

- clasificar ideas;
    
- dividir por áreas;
    
- detectar documentos;
    
- detectar riesgos;
    
- preparar borradores;
    
- crear informes.
    

No puede:

- crear empresas legalmente;
    
- contactar clientes;
    
- enviar propuestas;
    
- tomar decisiones fiscales;
    
- ejecutar campañas;
    
- activar automatizaciones.
    

---

# 32. RELACIÓN CON AGROCRIBAS

Agrocribas puede usarse como caso de prueba documental.

Estado:

Caso oficial de prueba del sandbox manual.

Regla:

Agrocribas no debe usarse para ejecución real dentro del MVP técnico.

Si el usuario quiere usar Agrocribas como proyecto real, debe abrirse una fase separada de validación.

---

# 33. PRIMER ENTREGABLE TÉCNICO

El primer entregable técnico recomendado es:

Robert Command Center Lite — Wireframe

Debe mostrar:

- input principal;
    
- selector de modo;
    
- panel de análisis;
    
- panel de riesgo;
    
- panel de resultado;
    
- panel de acciones bloqueadas;
    
- panel de informe;
    
- historial.
    

---

# 34. DECISIÓN REQUERIDA ANTES DE PROGRAMAR

Antes de programar, el usuario debe aprobar:

- alcance del MVP técnico;
    
- stack técnico;
    
- pantallas mínimas;
    
- reglas de seguridad;
    
- qué no se va a construir;
    
- orden de construcción.
    

Sin esta aprobación, Robert no debe avanzar a programación.

---

# 35. SIGUIENTE PASO

Siguiente paso recomendado:

Crear ROBERT_TECHNICAL_MVP_WIREFRAME o diseñar el primer esquema visual del Command Center Lite.

Alternativa:

Crear un prompt para Claude/Cursor indicando exactamente qué debe construir y qué no debe construir.

---

# 36. ESTADO FINAL DEL DOCUMENTO

Estado:

Borrador inicial pendiente de revisión.

Este documento no autoriza programación todavía.

Este documento define el alcance del MVP técnico básico.

El usuario debe aprobarlo antes de avanzar.

---

# 37. PRINCIPIO FINAL

Primero orden.

Después poder.

Robert ya validó el orden documental.

Ahora el MVP técnico debe convertir ese orden en una interfaz mínima, segura y controlada.


# REVISIÓN INICIAL — ROBERT_TECHNICAL_MVP_PLAN

Fecha: 28/06/2026

Documento revisado:

ROBERT_TECHNICAL_MVP_PLAN

Versión revisada:

v0.1

Estado de la revisión:

Revisión inicial completada — pendiente de aprobación del usuario

---

# 1. OBJETIVO DE LA REVISIÓN

Esta revisión tiene como objetivo validar si ROBERT_TECHNICAL_MVP_PLAN está listo para funcionar como guía inicial del MVP técnico básico de Robert.

La revisión no autoriza programación todavía.

Solo evalúa si el documento define correctamente:

- qué se quiere construir;
    
- qué no se debe construir todavía;
    
- qué límites debe respetar Robert;
    
- qué pantallas mínimas debe tener;
    
- qué flujo debe probarse;
    
- qué riesgos deben bloquearse;
    
- qué siguiente paso corresponde.
    

---

# 2. RESULTADO GENERAL DE LA REVISIÓN

Resultado:

El documento está correctamente planteado como base inicial del MVP técnico básico.

ROBERT_TECHNICAL_MVP_PLAN respeta el avance actual del proyecto:

- MVP manual completado;
    
- sandbox manual completado;
    
- sandbox manual validado documentalmente;
    
- no ejecución real;
    
- no conexiones externas todavía;
    
- no automatizaciones reales;
    
- no agentes autónomos;
    
- usuario mantiene control total.
    

---

# 3. QUÉ ESTÁ BIEN DEFINIDO

El documento define correctamente:

- nombre del MVP técnico: Robert Command Center Lite;
    
- objetivo del MVP técnico;
    
- alcance autorizado;
    
- límites del sistema;
    
- modos de operación;
    
- niveles de riesgo;
    
- pantallas mínimas;
    
- flujo principal;
    
- formato de salida;
    
- historial básico;
    
- documentos de referencia;
    
- stack técnico recomendado;
    
- opción simple para empezar;
    
- reglas de bloqueo;
    
- pruebas técnicas iniciales;
    
- criterios de éxito;
    
- criterios de fracaso;
    
- relación con seguridad;
    
- relación con Business Builder;
    
- relación con Agrocribas.
    

---

# 4. PUNTOS MÁS IMPORTANTES VALIDADOS

## Punto 1 — No saltar directo a app completa

El documento deja claro que el MVP técnico básico no debe intentar ser Robert completo.

Debe probar solo el núcleo:

instrucción → análisis → riesgo → respuesta → informe

Esto es correcto.

---

## Punto 2 — No conectar apps todavía

El documento bloquea correctamente:

- Gmail;
    
- Calendar;
    
- WhatsApp;
    
- CRM;
    
- Sheets;
    
- Zapier;
    
- Make;
    
- n8n;
    
- automatizaciones reales;
    
- agentes autónomos.
    

Esto es correcto.

---

## Punto 3 — Mantener sandbox como simulación

El documento mantiene la regla:

Simular no es ejecutar.

Esto es correcto.

---

## Punto 4 — Empezar simple

El documento propone iniciar con una versión local o simulada antes de usar APIs, Supabase o conexiones reales.

Esto es correcto.

---

## Punto 5 — Seguridad antes que poder

El documento conserva el principio central:

Primero orden.

Después poder.

Esto es correcto.

---

# 5. RIESGOS DETECTADOS

Aunque el documento está bien planteado, existen riesgos que deben vigilarse:

1. Querer programar demasiado pronto.
    
2. Meter API de IA antes de tener interfaz simple.
    
3. Hacer diseño visual complejo antes de validar flujo.
    
4. Confundir MVP técnico con Robert completo.
    
5. Intentar conectar Obsidian automáticamente demasiado pronto.
    
6. Querer conectar Gmail, Calendar o WhatsApp antes de seguridad técnica.
    
7. Convertir Agrocribas en caso real sin fase separada de validación.
    
8. Crear demasiadas pantallas en la primera versión.
    
9. No definir bien qué se guarda en historial.
    
10. No tener un criterio claro para aprobar el primer prototipo.
    

---

# 6. CORRECCIÓN RECOMENDADA

Antes de programar, Robert debe crear un documento adicional:

ROBERT_TECHNICAL_MVP_WIREFRAME

Objetivo:

Diseñar visualmente la primera versión de Robert Command Center Lite antes de escribir código.

Este documento debe definir:

- distribución de pantalla;
    
- paneles principales;
    
- flujo visual;
    
- información que se muestra;
    
- estados de riesgo;
    
- botones mínimos;
    
- qué pasa cuando una acción se bloquea;
    
- qué ve el usuario al usar MODO_SANDBOX;
    
- cómo se muestra el INFORME_ACCIONES.
    

---

# 7. DECISIÓN RECOMENDADA

Se recomienda aprobar ROBERT_TECHNICAL_MVP_PLAN como documento base para preparar el MVP técnico básico.

Esta aprobación no autoriza programación todavía.

Solo autoriza pasar al siguiente documento:

ROBERT_TECHNICAL_MVP_WIREFRAME

---

# 8. ESTADO FINAL DE LA REVISIÓN

Estado recomendado:

Aprobable como plan técnico inicial.

Pendiente:

Aprobación explícita del usuario.

Comando sugerido:

APRUEBO ROBERT_TECHNICAL_MVP_PLAN

---

# 9. SIGUIENTE PASO SI SE APRUEBA

Si el usuario aprueba este documento, el siguiente paso será registrar:

DECISIÓN #005 — ROBERT_TECHNICAL_MVP_PLAN aprobado como base del MVP técnico básico

Después se debe crear:

ROBERT_TECHNICAL_MVP_WIREFRAME

---

# 10. CONCLUSIÓN

ROBERT_TECHNICAL_MVP_PLAN está listo para aprobación como guía inicial.

El documento mantiene control, seguridad y límites.

No autoriza programación.

No autoriza conexiones.

No autoriza automatizaciones.

No autoriza agentes autónomos.

Autoriza únicamente diseñar el siguiente paso visual del MVP técnico básico.
