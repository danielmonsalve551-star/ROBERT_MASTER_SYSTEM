# Model Interface — Stage 6

`robert.model` implementa el límite proveedor-independiente entre `ModelRequest` y `ModelResponse`.
No configura clientes de red, credenciales, agentes, herramientas ejecutables ni persistencia.

## Flujo

```text
AUTHORIZED REQUESTER
→ MODEL ROUTER
→ MODEL ADAPTER
→ INJECTED PROVIDER PORT
→ VALIDATED MODEL RESPONSE
→ REQUIRED AUDIT
```

Componentes:

- `inputs.py`: perfiles, estado runtime, requisitos y vocabulario interno cerrado;
- `registry.py`: perfiles y estados explícitos, completos e inmutables;
- `router.py`: filtro obligatorio y ranking determinista;
- `adapter.py`: puerto de proveedor y traducción a contratos canónicos;
- `errors.py`: taxonomía normalizada sin errores crudos del proveedor;
- `interface.py`: autorización del requester, validación, fallback limitado y auditoría.

## Límites obligatorios

```text
MODEL OUTPUT ≠ TRUTH
MODEL OUTPUT ≠ DECISION
MODEL OUTPUT ≠ MEMORY WRITE
MODEL TOOL REQUEST ≠ TOOL AUTHORIZATION
ADAPTER ≠ GOVERNANCE
AVAILABLE MODEL ≠ AUTHORIZED MODEL
```

`tool_request_allowed=true` únicamente permite devolver objetos `ToolRequest` canónicos con
`REQUEST_ONLY_NO_EXECUTION`. El paquete no contiene ruta de ejecución de Tools.

`memory_write_allowed=true` se rechaza en Stage 6. Los identificadores de candidatos que devuelva un
Model permanecen como datos; este paquete no tiene acceso de escritura a un repositorio de Memory.

Toda llamada devuelta requiere un `AuditEvent` persistido. El Audit conserva referencias, identidad
del modelo, selección y estado; nunca copia el Context ni el output completo.

## Proveedores

`StructuredProviderAdapter` recibe un objeto que implementa `ModelProvider`. El repositorio no incluye
un cliente HTTP, SDK de proveedor, secretos ni configuración productiva. Los tests usan un proveedor
determinista en proceso. Una conexión real requiere una etapa y autorización separadas.

## Verificación

```bash
uv run pytest tests/model -W error
uv run ruff check src/robert/model tests/model
uv run ruff format --check src/robert/model tests/model
```
