# ROBERT_CANONICAL_MODEL

**Versión:** 0.2  
**Estado:** Aprobado e integrado  
**Tipo:** Modelo canónico de conceptos  
**Ubicación:** `09_ARCHITECTURE/ROBERT_CANONICAL_MODEL.md`  
**Fase relacionada:** Fase 10 — MVP técnico básico en preparación  
**Dependencia:** `ROBERT_SYSTEM_ARCHITECTURE.md`

---

## 1. Propósito

`ROBERT_CANONICAL_MODEL` define el vocabulario, los límites y las relaciones fundamentales de Robert.

Su función es evitar que distintos documentos, modelos de IA, agentes, skills, tools, módulos o implementaciones utilicen significados incompatibles para los mismos conceptos.

Este documento define conceptos y relaciones, pero **no activa capacidades por sí mismo**.

No autoriza:

- autonomía real;
- ejecución externa;
- acceso automático a nuevas herramientas;
- agentes ejecutivos;
- memoria automática;
- modificaciones automáticas;
- conexiones externas;
- despliegue.

---

## 2. Autoridad y jerarquía

Este documento actúa como modelo conceptual canónico.

```text
ROBERT_CANONICAL_MODEL
        ↓
define significado

ROBERT_SYSTEM_ARCHITECTURE
        ↓
define organización

TECHNICAL SPECS
        ↓
definen representación y comportamiento

IMPLEMENTATION
        ↓
define código e infraestructura
