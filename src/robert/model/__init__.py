"""Stage 6 provider-independent, audited model interface."""

from robert.model.adapter import (
    AdaptedModelResult,
    ModelAdapter,
    ModelProvider,
    StructuredProviderAdapter,
)
from robert.model.errors import (
    ModelErrorType,
    ModelProviderError,
    ModelRoutingError,
    NormalizedModelError,
)
from robert.model.inputs import (
    ModelAvailability,
    ModelCapability,
    ModelProfile,
    ModelRequirements,
    ModelRuntimeState,
    ModelSelection,
    ModelToolRequestDraft,
    ProviderModelOutput,
)
from robert.model.interface import ModelCallResult, ModelInterface
from robert.model.registry import ModelRegistry
from robert.model.router import ModelRouter

__all__ = [
    "AdaptedModelResult",
    "ModelAdapter",
    "ModelAvailability",
    "ModelCallResult",
    "ModelCapability",
    "ModelErrorType",
    "ModelInterface",
    "ModelProfile",
    "ModelProvider",
    "ModelProviderError",
    "ModelRegistry",
    "ModelRequirements",
    "ModelRoutingError",
    "ModelRouter",
    "ModelRuntimeState",
    "ModelSelection",
    "ModelToolRequestDraft",
    "NormalizedModelError",
    "ProviderModelOutput",
    "StructuredProviderAdapter",
]
