"""Stage 5 context assembly without persistence or model/provider disclosure."""

from robert.context.assembly import ContextAssembler, ContextAssemblyError
from robert.context.inputs import ContextFragment

__all__ = ["ContextAssembler", "ContextAssemblyError", "ContextFragment"]
