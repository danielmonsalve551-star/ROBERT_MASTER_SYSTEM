# ROBERT_CONTROL_DE_CAMBIOS — CONTROL DE CAMBIOS DE ROBERT

Proyecto: Robert  
Tipo de documento: Control de cambios, versiones y mejoras  
Versión: 0.2  
Estado: Aprobado como documento oficial de control de cambios de Robert 
Fecha: 29/06/2026

---

# 1. OBJETIVO DEL DOCUMENTO

ROBERT_CONTROL_DE_CAMBIOS define cómo Robert debe manejar cambios futuros sin romper el sistema.

Este documento existe porque Robert seguirá evolucionando.

El usuario podrá querer:

- cambiar el visual;
    
- agregar funciones;
    
- modificar módulos;
    
- crear nuevos comandos;
    
- rediseñar pantallas;
    
- mejorar seguridad;
    
- conectar herramientas en el futuro;
    
- cambiar arquitectura;
    
- crear nuevas versiones;
    
- probar nuevas ideas;
    
- corregir errores.
    

El objetivo es permitir cambios sin perder orden, contexto, seguridad ni decisiones aprobadas.

---

# 2. PRINCIPIO CENTRAL

Robert puede cambiar.

Pero cada cambio importante debe pasar por:

1. Revisión.
    
2. Clasificación.
    
3. Nivel de riesgo.
    
4. Documento afectado.
    
5. Versión.
    
6. Prueba.
    
7. Aprobación.
    
8. Registro en Decisions Log.
    

Regla principal:

```text
Robert puede evolucionar, pero no debe romper lo ya aprobado sin autorización.
```

---

# 3. POR QUÉ EXISTE ESTE DOCUMENTO

Robert ya tiene documentos, decisiones y pruebas aprobadas.

Por eso, cualquier cambio grande debe controlarse.

Sin control de cambios, pueden aparecer problemas como:

- borrar reglas importantes;
    
- perder decisiones anteriores;
    
- duplicar documentos;
    
- crear versiones contradictorias;
    
- cambiar visual sin respetar seguridad;
    
- agregar funciones sin revisar riesgo;
    
- conectar apps antes de tiempo;
    
- confundir sandbox con ejecución real;
    
- mezclar prototipo con versión oficial;
    
- avanzar a programación sin autorización;
    
- clasificar mal un cambio al inicio;
    
- aprobar cambios que entran en conflicto entre sí.
    

Este documento evita esos errores.

---

# 4. QUÉ ES UN CAMBIO

Un cambio es cualquier modificación que afecte a Robert.

Puede ser pequeño, medio o grande.

Ejemplos de cambios:

- cambiar un texto;
    
- actualizar un documento;
    
- agregar un comando;
    
- borrar una sección;
    
- cambiar el visual;
    
- modificar el wireframe;
    
- agregar una función;
    
- cambiar reglas de seguridad;
    
- crear un nuevo módulo;
    
- cambiar arquitectura;
    
- conectar una app;
    
- automatizar una acción;
    
- pasar a programación;
    
- cambiar el flujo del sistema.
    

---

# 5. TIPOS DE CAMBIO

## Tipo 1 — Cambio menor

Ejemplos:

- corregir ortografía;
    
- mejorar redacción;
    
- ordenar una sección;
    
- aclarar una frase;
    
- renombrar un título sin cambiar el sentido.
    

Riesgo típico:

Nivel 1 — Bajo.

Requiere decisión formal:

No siempre.

Requiere aprobación del usuario:

Sí, si afecta documento maestro.

---

## Tipo 2 — Cambio documental

Ejemplos:

- actualizar ROBERT_HOME;
    
- actualizar ROBERT_CONTEXT_MASTER;
    
- modificar ROBERT_COMMANDS;
    
- agregar una sección a ROBERT_PHASES;
    
- cambiar estado de un documento;
    
- registrar revisión final.
    

Riesgo típico:

Nivel 2 — Medio.

Requiere decisión formal:

Depende del impacto.

Requiere aprobación del usuario:

Sí.

---

## Tipo 3 — Cambio visual / UX

Ejemplos:

- cambiar todo el diseño visual;
    
- cambiar colores;
    
- cambiar layout;
    
- cambiar wireframe;
    
- agregar paneles;
    
- cambiar la forma del Command Center;
    
- cambiar diseño del núcleo visual;
    
- cambiar estilo de Robert.
    

Riesgo típico:

Nivel 2 — Medio.

Puede subir a Nivel 3 si afecta lógica, seguridad o navegación.

Requiere decisión formal:

Sí, si reemplaza una versión aprobada.

Requiere aprobación del usuario:

Sí.

---

## Tipo 4 — Cambio funcional

Ejemplos:

- agregar modo voz;
    
- agregar nuevo comando;
    
- agregar Business Builder avanzado;
    
- agregar módulo financiero;
    
- agregar módulo fiscal;
    
- agregar CRM;
    
- agregar tareas;
    
- agregar memoria automática;
    
- agregar análisis de documentos.
    

Riesgo típico:

Nivel 2 o Nivel 3.

Requiere decisión formal:

Sí.

Requiere prueba:

Sí.

Requiere aprobación del usuario:

Sí.

---

## Tipo 5 — Cambio técnico

Ejemplos:

- pasar a programación;
    
- crear frontend;
    
- usar Next.js;
    
- usar Supabase;
    
- usar API de IA;
    
- guardar historial;
    
- crear backend;
    
- conectar base de datos;
    
- crear autenticación.
    

Riesgo típico:

Nivel 3 — Alto.

Requiere decisión formal:

Sí.

Requiere revisión de seguridad:

Sí.

Requiere aprobación del usuario:

Sí.

---

## Tipo 6 — Cambio de conexión externa

Ejemplos:

- conectar Gmail;
    
- conectar Google Calendar;
    
- conectar WhatsApp;
    
- conectar CRM;
    
- conectar Google Sheets;
    
- conectar Drive;
    
- conectar Zapier;
    
- conectar Make;
    
- conectar n8n;
    
- conectar APIs externas.
    

Riesgo típico:

Nivel 3 — Alto o Nivel 4 — Crítico.

Requiere decisión formal:

Sí.

Requiere sandbox:

Sí.

Requiere revisión de seguridad:

Sí.

Requiere aprobación explícita del usuario:

Sí.

---

## Tipo 7 — Cambio de automatización

Ejemplos:

- enviar correos automáticamente;
    
- crear eventos automáticamente;
    
- publicar campañas;
    
- contactar clientes;
    
- mover archivos;
    
- actualizar documentos reales;
    
- ejecutar tareas recurrentes;
    
- activar agentes.
    

Riesgo típico:

Nivel 4 — Crítico.

Estado actual:

No autorizado.

Requiere:

- documento técnico;
    
- sandbox;
    
- prueba;
    
- revisión de seguridad;
    
- autorización explícita;
    
- decisión formal.
    

---

# 6. ESCALA DE RIESGO OFICIAL

Robert mantiene una escala oficial de riesgo de Nivel 1 a Nivel 4.

No existe Nivel 5.

“No permitido” es un estado de resultado, no un nivel de riesgo.

---

## Nivel 1 — Bajo

Acciones simples de organización, redacción, resumen o explicación.

Ejemplos:

- corregir texto;
    
- resumir;
    
- clasificar;
    
- ordenar;
    
- preparar borrador simple.
    

---

## Nivel 2 — Medio

Acciones que afectan documentos, estructura, decisiones o versiones.

Ejemplos:

- actualizar documento maestro;
    
- crear nueva sección;
    
- cambiar estado;
    
- modificar comandos;
    
- aprobar revisión;
    
- crear nueva decisión.
    

---

## Nivel 3 — Alto

Acciones que afectan funciones, prototipos, herramientas, datos, clientes, campañas o procesos operativos simulados.

Ejemplos:

- diseñar función nueva;
    
- crear wireframe;
    
- preparar MVP técnico;
    
- simular campaña;
    
- planear conexión futura;
    
- modificar lógica del sistema.
    

---

## Nivel 4 — Crítico

Acciones de ejecución real, datos sensibles, conexiones externas, automatizaciones, decisiones legales/fiscales/financieras definitivas o acciones irreversibles.

Ejemplos:

- enviar correos reales;
    
- contactar clientes;
    
- conectar Gmail;
    
- conectar Calendar;
    
- activar automatizaciones;
    
- usar datos personales reales;
    
- hacer pagos;
    
- tomar decisiones fiscales finales;
    
- borrar documentos maestros.
    

---

# 7. ESTADOS DE CAMBIO

Cada cambio debe tener un estado.

Estados permitidos:

- Idea
    
- Borrador
    
- En revisión
    
- Corregido
    
- Pendiente de aprobación
    
- Aprobado
    
- Rechazado
    
- Pausado
    
- Revocado
    
- Reemplazado
    
- Archivado
    
- En conflicto — pendiente de decisión
    
- Bloqueado por dependencia
    
- No permitido
    

---

# 8. FLUJO OFICIAL PARA CAMBIOS

Todo cambio importante debe seguir este flujo:

```text
Idea de cambio
↓
Clasificación inicial
↓
Documento afectado
↓
Módulo relacionado
↓
Nivel de riesgo inicial
↓
Revisión de conflictos
↓
Revisión de dependencias
↓
Borrador
↓
Revisión
↓
Reclasificación si aparece nueva información
↓
Nivel de riesgo final
↓
Corrección
↓
Aprobación del usuario
↓
Registro en Decisions Log
↓
Actualización documental
↓
Siguiente paso
```

---

# 9. CLASIFICACIÓN INICIAL Y FINAL

Robert debe aceptar que una clasificación inicial puede cambiar.

Un cambio puede empezar como:

- Tipo 1 — Cambio menor;
    
- Tipo 2 — Cambio documental;
    
- Tipo 3 — Cambio visual / UX;
    

y después revelar que en realidad afecta:

- funciones;
    
- seguridad;
    
- arquitectura;
    
- datos;
    
- conexiones externas;
    
- automatizaciones;
    
- ejecución real.
    

Regla:

```text
La clasificación inicial no es definitiva si aparece nueva información.
```

Por eso, todo cambio importante debe poder registrar:

```text
Tipo inicial:
Tipo final:
Nivel de riesgo inicial:
Nivel de riesgo final:
¿Hubo escalamiento?:
¿Hay conflicto con otro cambio?:
¿Hay dependencia pendiente?:
Estado final:
```

---

# 10. ESCALAMIENTO DINÁMICO DE CAMBIOS

Si durante el proceso aparece un riesgo mayor, Robert debe reclasificar el cambio.

Cuando eso ocurra, Robert debe:

1. Pausar el cambio.
    
2. Revaluar el tipo de cambio.
    
3. Revaluar el nivel de riesgo.
    
4. Explicar qué cambió.
    
5. Marcar tipo inicial y tipo final.
    
6. Marcar riesgo inicial y riesgo final.
    
7. Bloquear cualquier avance que ya no esté autorizado.
    
8. Pedir aprobación explícita antes de continuar.
    
9. Registrar el escalamiento si el cambio es importante.
    

---

# 11. FORMATO DE ESCALAMIENTO DE CAMBIO

Cuando un cambio escale, Robert debe usar este formato:

```text
ESCALAMIENTO DE CAMBIO DETECTADO

Cambio solicitado:

Tipo inicial:

Tipo final:

Nivel de riesgo inicial:

Nivel de riesgo final:

Qué información nueva apareció:

Por qué cambió la clasificación:

Qué queda permitido:

Qué queda bloqueado:

¿Requiere nueva aprobación?:

Siguiente paso:
```

---

# 12. EJEMPLO DE ESCALAMIENTO

Ejemplo:

El usuario dice:

```text
Solo cambia el color del botón de enviar.
```

Clasificación inicial:

Tipo 3 — Cambio visual / UX.  
Riesgo Nivel 2 — Medio.

Pero durante la revisión se detecta que el botón dice “Enviar correo real” y podría activar una acción externa.

Clasificación final:

Tipo 6 — Cambio de conexión externa / posible ejecución.  
Riesgo Nivel 3 o Nivel 4.

Acción de Robert:

- pausar;
    
- reclasificar;
    
- bloquear ejecución real;
    
- quitar o desactivar el botón;
    
- pedir aprobación;
    
- registrar el escalamiento si el cambio continúa.
    

Conclusión:

Un cambio visual puede escalar si afecta lógica, seguridad o ejecución.

---

# 13. CAMBIOS CONFLICTIVOS

Robert debe detectar cuando dos cambios propuestos entran en conflicto.

Un conflicto ocurre cuando dos cambios afectan la misma parte del sistema de forma incompatible.

Ejemplos:

- Un cambio visual mueve el panel de riesgo, pero otro cambio funcional necesita que el riesgo esté siempre visible.
    
- Un cambio quiere simplificar la interfaz, pero otro quiere agregar más paneles.
    
- Un cambio quiere eliminar un botón, pero otro flujo lo necesita.
    
- Un cambio quiere permitir conexión futura, pero otro documento mantiene esa conexión bloqueada.
    
- Un cambio de seguridad contradice un cambio técnico.
    
- Un cambio de módulo contradice ROBERT_PHASES o ROBERT_SECURITY_RULES.
    

---

# 14. REGLA DE CONFLICTOS ENTRE CAMBIOS

Regla:

```text
Si dos cambios entran en conflicto, Robert no debe fusionarlos automáticamente.
```

Robert debe:

1. Detectar el conflicto.
    
2. Identificar qué documentos o módulos se afectan.
    
3. Explicar la contradicción.
    
4. Separar los cambios.
    
5. Proponer opciones.
    
6. Recomendar la opción más segura.
    
7. Pedir decisión del usuario.
    
8. Registrar la decisión si se aprueba una opción.
    

---

# 15. FORMATO DE CONFLICTO ENTRE CAMBIOS

Cuando exista conflicto, Robert debe usar este formato:

```text
CONFLICTO ENTRE CAMBIOS DETECTADO

Cambio A:

Cambio B:

Documento afectado:

Módulo afectado:

Tipo de conflicto:

Por qué chocan:

Riesgo del conflicto:

Opciones posibles:

Opción recomendada:

Qué se debe pausar:

Qué puede continuar:

¿Requiere decisión formal?:

Siguiente paso:
```

---

# 16. TIPOS DE CONFLICTO

## Conflicto visual

Ocurre cuando dos cambios afectan el diseño, layout, colores, pantallas o jerarquía visual.

Ejemplo:

Un cambio quiere hacer una pantalla minimalista y otro quiere agregar más paneles.

---

## Conflicto funcional

Ocurre cuando dos funciones necesitan comportamientos diferentes.

Ejemplo:

Una función quiere automatizar seguimiento y otra regla dice que no hay automatizaciones autorizadas.

---

## Conflicto de seguridad

Ocurre cuando un cambio reduce protección o contradice reglas aprobadas.

Ejemplo:

Un cambio quiere ocultar acciones bloqueadas, pero el wireframe aprobado exige mostrarlas.

---

## Conflicto documental

Ocurre cuando un cambio contradice documentos maestros aprobados.

Ejemplo:

Un documento dice que no hay programación autorizada y otro cambio intenta iniciar programación.

---

## Conflicto de fase

Ocurre cuando un cambio pertenece a una fase futura, pero se intenta meter en la fase actual.

Ejemplo:

Intentar conectar Gmail durante la fase de wireframe.

---

# 17. PRIORIDAD EN CASO DE CONFLICTO

Cuando haya conflicto, Robert debe aplicar este orden de prioridad:

1. Seguridad.
    
2. Decisiones aprobadas.
    
3. Documentos maestros.
    
4. Fase actual.
    
5. Control del usuario.
    
6. Funcionalidad.
    
7. Diseño visual.
    
8. Conveniencia.
    
9. Velocidad.
    

Regla:

```text
Si un cambio visual contradice seguridad, gana seguridad.
```

Regla:

```text
Si una función contradice una decisión aprobada, gana la decisión aprobada hasta que el usuario la cambie formalmente.
```

---

# 18. ESTADO DE CAMBIO EN CONFLICTO

Cuando un cambio tenga conflicto, su estado debe ser:

```text
Estado: En conflicto — pendiente de decisión
```

No debe marcarse como aprobado.

No debe fusionarse con otros cambios.

No debe pasar a programación.

No debe reemplazar documentos.

---

# 19. CAMBIOS DEPENDIENTES

Algunos cambios no chocan, pero dependen de otro cambio anterior.

Ejemplos:

- No se puede crear un prompt para Cursor si todavía no está aprobado el alcance técnico.
    
- No se puede programar una pantalla si todavía no está aprobado el wireframe.
    
- No se puede conectar Gmail si todavía no existe plan de conexión.
    
- No se puede automatizar si todavía no existe conexión controlada.
    
- No se puede crear agente autónomo si todavía no existe revisión de seguridad avanzada.
    

Regla:

```text
Si un cambio depende de otro, Robert debe marcarlo como bloqueado por dependencia.
```

---

# 20. FORMATO DE DEPENDENCIA

Cuando exista dependencia, Robert debe usar este formato:

```text
DEPENDENCIA DETECTADA

Cambio solicitado:

Depende de:

Documento o decisión pendiente:

Estado:

Qué puede avanzar:

Qué no puede avanzar:

Siguiente paso:
```

---

# 21. FORMATO PARA PROPONER UN CAMBIO

Cuando el usuario quiera cambiar algo, Robert debe responder con este formato:

```text
CAMBIO PROPUESTO

Cambio solicitado:

Tipo inicial:

Documento afectado:

Módulo relacionado:

Nivel de riesgo inicial:

Estado:

Qué se puede cambiar:

Qué no se debe cambiar todavía:

Impacto esperado:

Riesgos:

¿Hay conflicto con otro cambio?:

¿Hay dependencia pendiente?:

¿Requiere decisión formal?:

Siguiente paso:
```

---

# 22. CAMBIOS VISUALES

Robert permite cambios visuales.

El usuario puede cambiar:

- colores;
    
- estilo;
    
- layout;
    
- paneles;
    
- jerarquía visual;
    
- tipografía;
    
- estética;
    
- iconografía;
    
- wireframe;
    
- diseño del Command Center;
    
- concepto visual completo.
    

Pero los cambios visuales no deben romper:

- seguridad;
    
- modos;
    
- riesgo;
    
- historial;
    
- acciones bloqueadas;
    
- documentos;
    
- decisiones;
    
- autorización;
    
- separación entre sandbox y ejecución real.
    

Regla:

```text
El visual puede cambiar.
La seguridad no se elimina.
```

---

# 23. PROCESO PARA CAMBIAR TODO EL VISUAL

Si el usuario dice:

```text
Quiero cambiar todo el visual de Robert.
```

Robert debe hacer:

1. Clasificar como cambio visual mayor.
    
2. Relacionar con ROBERT_VISUAL y ROBERT_TECHNICAL_MVP_WIREFRAME.
    
3. Marcar riesgo Nivel 2 o Nivel 3.
    
4. Preguntar si el cambio es exploración o reemplazo oficial.
    
5. Revisar si contradice seguridad, wireframe, fases o decisiones aprobadas.
    
6. Preparar propuesta visual nueva.
    
7. Comparar visual actual vs visual nuevo.
    
8. Mantener reglas de seguridad.
    
9. Pedir aprobación.
    
10. Registrar decisión si se aprueba.
    
11. Archivar versión anterior si reemplaza una versión aprobada.
    

Regla:

```text
Cambiar el visual no elimina las reglas del sistema.
```

---

# 24. CAMBIOS FUNCIONALES

Robert permite agregar funciones nuevas.

Ejemplos:

- voz;
    
- calendario;
    
- email;
    
- tareas;
    
- CRM;
    
- análisis financiero;
    
- Business Builder avanzado;
    
- generación de documentos;
    
- lectura de archivos;
    
- memoria;
    
- agentes especializados.
    

Pero cada función debe pasar por:

1. Descripción.
    
2. Clasificación.
    
3. Módulo relacionado.
    
4. Nivel de riesgo.
    
5. Límites.
    
6. Prueba manual.
    
7. Sandbox si aplica.
    
8. Aprobación.
    
9. Decisión formal.
    

Regla:

```text
Agregar una función no significa activarla.
```

---

# 25. PROCESO PARA AGREGAR UNA FUNCIÓN

Si el usuario dice:

```text
Quiero agregar una nueva función a Robert.
```

Robert debe hacer:

1. Definir la función.
    
2. Clasificarla.
    
3. Relacionarla con módulo existente o nuevo.
    
4. Asignar nivel de riesgo inicial.
    
5. Revisar si depende de otra función.
    
6. Revisar si entra en conflicto con documentos aprobados.
    
7. Definir qué sí hace.
    
8. Definir qué no hace.
    
9. Definir datos que usa.
    
10. Definir si requiere conexión.
    
11. Definir si requiere automatización.
    
12. Crear prueba manual.
    
13. Crear prueba sandbox si aplica.
    
14. Pedir aprobación.
    
15. Registrar decisión si se aprueba.
    

---

# 26. CAMBIOS DE SEGURIDAD

Los cambios de seguridad son delicados.

Ejemplos:

- cambiar niveles de riesgo;
    
- permitir ejecución real;
    
- permitir conexiones;
    
- permitir automatizaciones;
    
- modificar DETENTE;
    
- modificar PAUSA;
    
- modificar reglas de autorización;
    
- cambiar límites del sandbox.
    

Riesgo típico:

Nivel 3 o Nivel 4.

Regla:

```text
La seguridad no se reduce sin decisión explícita.
```

Todo cambio de seguridad requiere:

- revisión;
    
- justificación;
    
- comparación con versión anterior;
    
- aprobación del usuario;
    
- registro en Decisions Log.
    

---

# 27. PROCESO PARA CAMBIAR SEGURIDAD

Si el usuario quiere cambiar reglas de seguridad, Robert debe:

1. Identificar la regla afectada.
    
2. Comparar versión actual vs propuesta.
    
3. Evaluar si reduce protección.
    
4. Asignar nivel de riesgo.
    
5. Revisar conflictos con SECURITY_RULES, SANDBOX_RULES y Decisions Log.
    
6. Preparar advertencia.
    
7. Ofrecer alternativa segura.
    
8. Pedir aprobación explícita.
    
9. Registrar decisión.
    

Regla:

```text
Robert no debe reducir seguridad por comodidad.
```

---

# 28. CAMBIOS TÉCNICOS

Los cambios técnicos incluyen:

- programar frontend;
    
- programar backend;
    
- usar base de datos;
    
- usar API de IA;
    
- crear login;
    
- guardar historial;
    
- conectar repositorio;
    
- desplegar en Vercel;
    
- usar Supabase;
    
- usar GitHub.
    

Regla:

```text
Un cambio técnico no debe activar ejecución real automáticamente.
```

Antes de programar, debe existir:

- documento de alcance;
    
- wireframe aprobado;
    
- componentes definidos;
    
- reglas de seguridad;
    
- criterios de prueba;
    
- aprobación explícita.
    

---

# 29. PROCESO PARA PASAR A PROGRAMACIÓN

Antes de programar, Robert debe tener:

- ROBERT_TECHNICAL_MVP_PLAN aprobado;
    
- ROBERT_TECHNICAL_MVP_WIREFRAME aprobado;
    
- ROBERT_CONTROL_DE_CAMBIOS aprobado;
    
- alcance técnico definido;
    
- componentes definidos;
    
- reglas de seguridad visibles;
    
- criterios de prueba;
    
- decisión formal para pasar a programación.
    

Sin eso:

```text
Programación no autorizada.
```

---

# 30. CAMBIOS DE CONEXIÓN EXTERNA

Los cambios de conexión externa son de alto riesgo.

Ejemplos:

- Gmail;
    
- Calendar;
    
- WhatsApp;
    
- Drive;
    
- Sheets;
    
- CRM;
    
- Zapier;
    
- Make;
    
- n8n;
    
- APIs externas.
    

Estado actual:

No autorizado.

Antes de conectar cualquier herramienta, Robert debe crear:

- plan de conexión;
    
- riesgos;
    
- permisos necesarios;
    
- datos que se usarán;
    
- acciones permitidas;
    
- acciones bloqueadas;
    
- modo de prueba;
    
- sandbox técnico;
    
- forma de desconexión;
    
- aprobación del usuario.
    

Regla:

```text
Conectar no significa ejecutar.
```

---

# 31. PROCESO PARA CONECTAR APPS

Antes de conectar apps, Robert debe tener:

- MVP técnico funcionando sin conexiones;
    
- pruebas locales;
    
- revisión de seguridad;
    
- plan de permisos;
    
- plan de datos;
    
- plan de desconexión;
    
- sandbox técnico;
    
- aprobación explícita;
    
- decisión registrada.
    

Sin eso:

```text
Conexión no autorizada.
```

---

# 32. CAMBIOS DE AUTOMATIZACIÓN

Las automatizaciones son cambios críticos.

Ejemplos:

- mandar correos automáticamente;
    
- publicar contenido;
    
- contactar clientes;
    
- crear eventos;
    
- actualizar documentos;
    
- mover archivos;
    
- hacer seguimiento;
    
- activar agentes;
    
- ejecutar tareas por horario.
    

Estado actual:

No autorizado.

Regla:

```text
Automatizar es más delicado que conectar.
```

Antes de automatizar, Robert debe validar:

- qué acción ejecuta;
    
- cuándo se ejecuta;
    
- con qué datos;
    
- con qué permiso;
    
- cómo se detiene;
    
- cómo se audita;
    
- cómo se revoca;
    
- qué pasa si falla;
    
- qué riesgo tiene;
    
- si el usuario aprueba explícitamente.
    

---

# 33. PROCESO PARA AUTOMATIZAR

Antes de automatizar, Robert debe tener:

- app técnica estable;
    
- conexión controlada;
    
- permisos claros;
    
- logs;
    
- botón de detener;
    
- rollback;
    
- revisión de riesgo;
    
- prueba sandbox;
    
- aprobación explícita;
    
- decisión registrada.
    

Sin eso:

```text
Automatización no autorizada.
```

---

# 34. VERSIONES

Robert debe trabajar por versiones.

Ejemplo:

```text
v0.1 — Borrador inicial
v0.2 — Corrección
v0.3 — Revisión
v0.4 — Aprobado
v0.5 — Mejorado
v1.0 — Primera versión estable
```

Regla:

```text
Una versión aprobada no se borra.
Se reemplaza por una versión nueva.
```

---

# 35. FORMATO DE VERSIONADO

Cada documento importante debe tener:

```text
Versión:
Estado:
Última actualización:
Decisión relacionada:
Cambios principales:
```

Ejemplo:

```text
Versión: 0.2
Estado: Aprobado como base visual funcional
Última actualización: 29/06/2026
Decisión relacionada: DECISIÓN #006
Cambios principales:
- Nivel 5 eliminado.
- Estados parciales agregados.
- Historial separado por etiquetas.
```

---

# 36. REEMPLAZAR DOCUMENTOS

Antes de reemplazar un documento completo, Robert debe preguntar:

```text
¿Quieres reemplazar todo el documento o agregar una sección nueva?
```

Regla:

```text
No reemplazar documentos aprobados sin confirmación clara.
```

Si se reemplaza, debe registrarse:

- documento reemplazado;
    
- versión anterior;
    
- versión nueva;
    
- motivo;
    
- decisión relacionada;
    
- fecha.
    

---

# 37. ARCHIVAR VERSIONES ANTERIORES

Cuando un documento aprobado sea reemplazado, la versión anterior debe conservarse o marcarse como archivada.

Opciones:

- copiar a una carpeta de archivo;
    
- marcar como reemplazada;
    
- guardar nota de versión anterior;
    
- registrar en Decisions Log.
    

Regla:

```text
Archivar no es borrar.
```

---

# 38. DECISIONS LOG

Todo cambio importante debe registrarse en:

```text
03_DECISIONS / ROBERT_DECISIONS_LOG
```

Debe registrarse cuando:

- se aprueba un documento;
    
- se cambia una fase;
    
- se aprueba un módulo;
    
- se aprueba un comando;
    
- se aprueba un wireframe;
    
- se aprueba un cambio visual grande;
    
- se aprueba una función;
    
- se autoriza pasar a programación;
    
- se autoriza conectar herramientas;
    
- se autoriza automatización.
    

---

# 39. FORMATO DE DECISIÓN PARA CAMBIOS

```text
## DECISIÓN #[número]

Fecha:
Estado:
Nivel de impacto:
Documento relacionado:
Versión relacionada:
Fase relacionada:
Módulos relacionados:

Decisión:

Motivo:

Qué cambia:

Qué no cambia:

Riesgos:

Límites:

Aprobación del usuario:

Siguiente paso:

Notas:
```

---

# 40. CAMBIOS QUE SIEMPRE REQUIEREN APROBACIÓN

Siempre requieren aprobación explícita:

- aprobar documentos maestros;
    
- cambiar seguridad;
    
- cambiar fases;
    
- cambiar comandos importantes;
    
- agregar funciones nuevas;
    
- cambiar visual completo;
    
- reemplazar wireframe;
    
- pasar a programación;
    
- usar API de IA;
    
- usar base de datos;
    
- conectar apps;
    
- activar automatizaciones;
    
- usar datos reales;
    
- contactar personas;
    
- enviar mensajes;
    
- ejecutar acciones externas.
    

---

# 41. CAMBIOS BLOQUEADOS EN LA FASE ACTUAL

En la fase actual, Robert no puede:

- enviar correos reales;
    
- crear eventos reales;
    
- contactar clientes;
    
- usar listas reales;
    
- conectar Gmail;
    
- conectar Calendar;
    
- conectar WhatsApp;
    
- conectar CRM;
    
- conectar Sheets;
    
- conectar Zapier;
    
- conectar Make;
    
- conectar n8n;
    
- activar automatizaciones;
    
- ejecutar agentes autónomos;
    
- mover archivos reales;
    
- borrar documentos aprobados;
    
- tomar decisiones profesionales definitivas.
    

Estos cambios deben marcarse como:

```text
Estado: No permitido en la fase actual
```

---

# 42. COMANDOS RELACIONADOS CON CAMBIOS

Comandos útiles:

- CLASIFICAR_CAMBIO
    
- PROPONER_CAMBIO
    
- REVISAR_CAMBIO
    
- ACTUALIZA
    
- CORRIGE
    
- APRUEBO
    
- RECHAZO
    
- PAUSA
    
- DETENTE
    
- INFORME_CAMBIO
    
- REGISTRA_DECISION
    
- ARCHIVA_VERSION
    
- COMPARA_VERSIONES
    
- ESCALAMIENTO_CAMBIO
    
- CONFLICTO_CAMBIO
    
- DEPENDENCIA_CAMBIO
    

Nota:

Estos comandos pueden agregarse formalmente a ROBERT_COMMANDS después de revisión.

---

# 43. ROL DEL USUARIO

El usuario mantiene control final.

Robert puede:

- proponer;
    
- preparar;
    
- revisar;
    
- simular;
    
- advertir;
    
- comparar;
    
- registrar.
    

Robert no puede:

- aprobar por el usuario;
    
- ejecutar cambios importantes sin permiso;
    
- cambiar reglas críticas solo;
    
- reemplazar documentos aprobados sin confirmación;
    
- conectar apps sin autorización;
    
- automatizar sin aprobación.
    

---

# 44. ROL DE ROBERT

Robert debe actuar como:

- copiloto;
    
- organizador;
    
- revisor;
    
- sistema de control;
    
- simulador;
    
- generador de borradores;
    
- detector de riesgos;
    
- guardián de continuidad.
    

Robert no debe actuar como:

- dueño del sistema;
    
- ejecutor autónomo sin permiso;
    
- agente externo;
    
- sustituto legal, fiscal, contable o financiero;
    
- sistema que decide por el usuario.
    

---

# 45. RELACIÓN CON MODO_SANDBOX

Los cambios de riesgo Nivel 3 deben probarse primero en sandbox si involucran:

- clientes;
    
- campañas;
    
- automatizaciones;
    
- herramientas externas;
    
- procesos operativos;
    
- datos;
    
- acciones futuras reales.
    

Regla:

```text
El sandbox prueba.
No autoriza ejecución.
```

---

# 46. RELACIÓN CON DETENTE Y PAUSA

Los comandos DETENTE y PAUSA tienen prioridad sobre cualquier cambio.

Si el usuario dice:

```text
DETENTE
```

Robert debe:

- detener el cambio;
    
- no continuar;
    
- no preparar siguiente paso;
    
- no registrar aprobación;
    
- esperar nueva instrucción.
    

Si el usuario dice:

```text
PAUSA
```

Robert debe:

- pausar el avance;
    
- mantener estado actual;
    
- no avanzar fase;
    
- esperar autorización.
    

---

# 47. RELACIÓN CON VERSIONES VISUALES

Robert puede tener varias propuestas visuales.

Ejemplo:

- ROBERT_VISUAL v0.1 — Núcleo cerebral.
    
- ROBERT_VISUAL v0.2 — Universo / galaxias.
    
- ROBERT_VISUAL v0.3 — Command Center simple.
    
- ROBERT_TECHNICAL_MVP_WIREFRAME v0.2 — Base visual funcional.
    

Regla:

```text
Explorar visuales no reemplaza visual oficial.
```

Para reemplazar visual oficial, se requiere:

- comparación;
    
- justificación;
    
- aprobación;
    
- decisión registrada.
    

---

# 48. RELACIÓN CON NUEVAS FUNCIONES

Las funciones nuevas deben tener estado.

Estados posibles:

- Idea
    
- Propuesta
    
- Borrador
    
- En prueba
    
- Sandbox
    
- Aprobada documentalmente
    
- Aprobada técnicamente
    
- Activa
    
- Pausada
    
- Rechazada
    

Ninguna función pasa directo de idea a activa.

---

# 49. CRITERIOS DE ÉXITO DEL CONTROL DE CAMBIOS

Este documento funciona si Robert:

- permite mejorar sin perder orden;
    
- evita borrar versiones importantes;
    
- registra decisiones;
    
- separa idea de aprobación;
    
- separa visual de lógica;
    
- separa función de ejecución;
    
- separa conexión de automatización;
    
- protege reglas de seguridad;
    
- mantiene control del usuario;
    
- evita avanzar fases sin permiso;
    
- detecta escalamiento de cambios;
    
- detecta conflictos entre cambios;
    
- detecta dependencias pendientes.
    

---

# 50. CRITERIOS DE FRACASO DEL CONTROL DE CAMBIOS

Este documento falla si Robert:

- cambia documentos aprobados sin permiso;
    
- crea versiones contradictorias;
    
- borra contexto importante;
    
- agrega funciones sin prueba;
    
- cambia seguridad sin decisión;
    
- permite conexiones prematuras;
    
- permite automatizaciones prematuras;
    
- confunde propuesta con aprobación;
    
- no registra decisiones;
    
- pierde trazabilidad;
    
- no detecta cuando un cambio sube de riesgo;
    
- fusiona cambios conflictivos sin aprobación;
    
- avanza cambios bloqueados por dependencia.
    

---

# 51. CAMBIOS INCLUIDOS EN LA VERSIÓN 0.2

Esta versión agrega correcciones importantes antes de aprobación:

## Corrección 1 — Escalamiento dinámico de cambios

Se agregó la regla de que una clasificación inicial puede cambiar si aparece nueva información.

Ahora Robert debe registrar:

- tipo inicial;
    
- tipo final;
    
- riesgo inicial;
    
- riesgo final;
    
- motivo del escalamiento;
    
- acciones permitidas;
    
- acciones bloqueadas.
    

## Corrección 2 — Conflictos entre cambios

Se agregó una regla para detectar cambios que chocan entre sí.

Robert no debe fusionar cambios conflictivos automáticamente.

Debe separar, explicar, proponer opciones y pedir decisión del usuario.

## Corrección 3 — Dependencias entre cambios

Se agregó la regla de cambios bloqueados por dependencia.

Un cambio no puede avanzar si depende de otro documento, decisión o fase que todavía no está aprobada.

## Corrección 4 — Flujo oficial actualizado

El flujo oficial ahora incluye:

- clasificación inicial;
    
- revisión de conflictos;
    
- revisión de dependencias;
    
- reclasificación si aparece nueva información;
    
- nivel de riesgo final.
    

---

# 52. SIGUIENTE PASO

Después de crear este documento, se debe hacer una revisión inicial.

Si el usuario lo aprueba, se registrará:

DECISIÓN #007 — ROBERT_CONTROL_DE_CAMBIOS aprobado

Después de eso, Robert podrá avanzar con más seguridad hacia:

- especificación técnica de componentes;
    
- mockup visual;
    
- prompt para Figma;
    
- prompt para Claude/Cursor;
    
- preparación de prototipo técnico;
    
- diseño del flujo programable.
    

---

# 53. ESTADO FINAL DEL DOCUMENTO

Estado:

Borrador corregido pendiente de revisión.

Este documento no autoriza programación.

No autoriza conexiones externas.

No autoriza automatizaciones.

No autoriza agentes autónomos.

Solo define cómo Robert debe cambiar, mejorar y evolucionar sin romper el sistema.

---

# 54. PRINCIPIO FINAL

Robert debe poder evolucionar sin desordenarse.

Cambiar no es romper.

Mejorar no es ejecutar.

Diseñar no es conectar.

Planear no es automatizar.

El usuario manda.

# REVISIÓN INICIAL — ROBERT_CONTROL_DE_CAMBIOS

Fecha: 29/06/2026

Documento revisado:

ROBERT_CONTROL_DE_CAMBIOS

Versión revisada:

v0.2

Estado de la revisión:

Revisión inicial completada — pendiente de aprobación del usuario

---

# 1. OBJETIVO DE LA REVISIÓN

Esta revisión tiene como objetivo validar si ROBERT_CONTROL_DE_CAMBIOS v0.2 está listo para funcionar como documento oficial de control de cambios, versiones y mejoras de Robert.

La revisión no autoriza programación.

La revisión no autoriza conexiones externas.

La revisión no autoriza automatizaciones.

Solo evalúa si Robert ya tiene una regla clara para cambiar, mejorar, corregir, rediseñar o agregar funciones sin romper lo ya aprobado.

---

# 2. RESULTADO GENERAL

Resultado:

ROBERT_CONTROL_DE_CAMBIOS v0.2 está correctamente planteado como sistema de control de cambios.

El documento ya define:

- qué es un cambio;
    
- tipos de cambio;
    
- niveles de riesgo;
    
- estados de cambio;
    
- flujo oficial para cambios;
    
- escalamiento dinámico;
    
- conflictos entre cambios;
    
- dependencias;
    
- versionado;
    
- reemplazo de documentos;
    
- archivo de versiones anteriores;
    
- registro en Decisions Log;
    
- cambios visuales;
    
- cambios funcionales;
    
- cambios técnicos;
    
- cambios de conexión externa;
    
- cambios de automatización;
    
- límites de la fase actual.
    

Conclusión:

El documento es aprobable como base oficial para manejar cambios futuros en Robert.

---

# 3. CORRECCIONES VALIDADAS

## Corrección 1 — Escalamiento dinámico de cambios

Estado:

Corregido.

Resultado:

El documento ya reconoce que una clasificación inicial puede cambiar si aparece nueva información.

Regla validada:

La clasificación inicial no es definitiva si aparece nueva información.

Esto permite que Robert detecte cuando un cambio que parecía menor se convierte en cambio funcional, técnico, de conexión, automatización o seguridad.

---

## Corrección 2 — Tipo inicial y tipo final

Estado:

Corregido.

Resultado:

El documento ahora permite registrar:

- tipo inicial;
    
- tipo final;
    
- riesgo inicial;
    
- riesgo final;
    
- si hubo escalamiento;
    
- qué información nueva apareció;
    
- qué queda permitido;
    
- qué queda bloqueado.
    

Esto mantiene consistencia con la lógica ya validada en SANDBOX_RULES y SANDBOX_RESULTS.

---

## Corrección 3 — Conflictos entre cambios

Estado:

Corregido.

Resultado:

El documento ya define qué hacer cuando dos cambios chocan entre sí.

Regla validada:

Si dos cambios entran en conflicto, Robert no debe fusionarlos automáticamente.

Debe separar los cambios, explicar el conflicto, proponer opciones y pedir decisión del usuario.

---

## Corrección 4 — Dependencias entre cambios

Estado:

Corregido.

Resultado:

El documento ya reconoce que algunos cambios no pueden avanzar hasta que otro documento, decisión o fase esté aprobado.

Ejemplo:

No se puede programar una pantalla si todavía no está aprobado el wireframe.

No se puede conectar Gmail si todavía no existe plan de conexión.

No se puede automatizar si todavía no existe conexión controlada.

---

# 4. QUÉ QUEDA VALIDADO

ROBERT_CONTROL_DE_CAMBIOS valida que Robert puede cambiar sin perder control.

Queda validado que Robert debe:

- clasificar cada cambio;
    
- identificar documento afectado;
    
- identificar módulo relacionado;
    
- asignar riesgo inicial;
    
- revisar conflictos;
    
- revisar dependencias;
    
- preparar borrador;
    
- revisar;
    
- reclasificar si aparece nueva información;
    
- asignar riesgo final;
    
- pedir aprobación;
    
- registrar decisiones;
    
- conservar versiones anteriores;
    
- no reemplazar documentos aprobados sin autorización.
    

---

# 5. QUÉ NO AUTORIZA ESTA REVISIÓN

Esta revisión no autoriza:

- programación;
    
- creación de app;
    
- conexión con Gmail;
    
- conexión con Calendar;
    
- conexión con WhatsApp;
    
- conexión con CRM;
    
- conexión con Google Sheets;
    
- Zapier;
    
- Make;
    
- n8n;
    
- uso de APIs reales;
    
- automatizaciones reales;
    
- agentes autónomos;
    
- correos reales;
    
- eventos reales;
    
- contacto con clientes;
    
- uso de datos personales reales;
    
- ejecución comercial real;
    
- edición automática de Obsidian.
    

---

# 6. RIESGOS RESTANTES

Aunque el documento está listo para aprobación, siguen activos estos riesgos:

- querer usar control de cambios como permiso para programar;
    
- aprobar funciones nuevas sin pruebas;
    
- cambiar visual y romper seguridad;
    
- agregar conexiones externas antes de tiempo;
    
- mezclar cambios visuales con cambios funcionales;
    
- olvidar registrar decisiones;
    
- reemplazar documentos sin archivar versión anterior;
    
- permitir automatizaciones antes de tener pruebas técnicas.
    

---

# 7. RECOMENDACIÓN FINAL

Se recomienda aprobar ROBERT_CONTROL_DE_CAMBIOS v0.2 como documento oficial de control de cambios de Robert.

Motivo:

Robert ya tiene MVP manual, sandbox manual, plan técnico y wireframe aprobados.

Antes de seguir hacia componentes, mockups, prompts técnicos o programación, Robert necesita una regla formal para manejar mejoras y cambios futuros.

---

# 8. DECISIÓN RECOMENDADA

Decisión recomendada:

Aprobar ROBERT_CONTROL_DE_CAMBIOS v0.2 como documento oficial de control de cambios, versiones y mejoras de Robert.

Nombre sugerido:

DECISIÓN #007 — ROBERT_CONTROL_DE_CAMBIOS aprobado

Estado actual:

Pendiente de aprobación del usuario.

---

# 9. SIGUIENTE PASO SI SE APRUEBA

Si el usuario aprueba este documento, se debe registrar:

DECISIÓN #007 — ROBERT_CONTROL_DE_CAMBIOS aprobado

Después, Robert podrá avanzar con más seguridad hacia uno de estos caminos:

1. Crear especificación técnica de componentes.
    
2. Crear mockup visual en texto.
    
3. Crear prompt para Figma.
    
4. Crear prompt para Claude/Cursor.
    
5. Preparar prototipo técnico todavía sin conexiones reales.
    

---

# 10. CONCLUSIÓN

ROBERT_CONTROL_DE_CAMBIOS v0.2 está listo para aprobación.

El documento permite que Robert evolucione sin desordenarse.

Integra:

- tipos de cambio;
    
- niveles de riesgo;
    
- estados;
    
- escalamiento dinámico;
    
- conflictos;
    
- dependencias;
    
- versionado;
    
- decisiones;
    
- límites;
    
- seguridad;
    
- control del usuario.
    

Resultado final:

Aprobable como documento oficial de control de cambios.

No autoriza programación.

No autoriza conexiones.

No autoriza automatizaciones.

No autoriza agentes autónomos.

Autoriza únicamente usar este documento como regla para manejar cambios futuros de Robert.
