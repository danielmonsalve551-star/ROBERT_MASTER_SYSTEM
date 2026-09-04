"""Deterministic eligibility filtering; model preference never grants authority."""

from robert.contracts.model import ModelRequest
from robert.model.errors import ModelRoutingError
from robert.model.inputs import (
    ModelAvailability,
    ModelRequirements,
    ModelSelection,
    snapshot,
)
from robert.model.registry import ModelRegistry


class ModelRouter:
    def __init__(self, registry: ModelRegistry) -> None:
        self._registry = registry

    def rank(
        self, request: ModelRequest, requirements: ModelRequirements
    ) -> tuple[ModelSelection, ...]:
        request = snapshot(ModelRequest, request)
        requirements = snapshot(ModelRequirements, requirements)
        required = set(requirements.required_capabilities)
        preferred = set(requirements.preferred_capabilities)
        candidates = []
        for profile in self._registry.profiles:
            state = self._registry.runtime_state(profile.model_id)
            capabilities = set(profile.capabilities)
            if state.availability not in (
                ModelAvailability.AVAILABLE,
                ModelAvailability.DEGRADED,
            ):
                continue
            if state.rate_limited:
                continue
            if request.provider_requirement and request.provider_requirement != profile.provider:
                continue
            if not required.issubset(capabilities):
                continue
            if requirements.context_units > profile.context_window:
                continue
            if request.sensitivity not in profile.allowed_sensitivities:
                continue
            if request.tool_request_allowed and not profile.tool_support:
                continue
            if (
                requirements.structured_output_required or bool(request.output_contract)
            ) and not profile.structured_output_support:
                continue
            score = (
                state.availability == ModelAvailability.AVAILABLE,
                len(preferred & capabilities),
                profile.priority,
                -len(profile.limitations),
            )
            candidates.append((score, profile))
        candidates.sort(key=lambda item: item[1].model_id)
        candidates.sort(key=lambda item: item[0], reverse=True)
        if not candidates:
            raise ModelRoutingError("no model satisfies the mandatory request constraints")
        return tuple(
            ModelSelection(
                model_id=profile.model_id,
                provider=profile.provider,
                adapter_id=profile.adapter_id,
                selection_reason=(
                    "required capabilities, provider, context, sensitivity and runtime state "
                    "satisfied; deterministic preference ranking applied"
                ),
            )
            for _, profile in candidates
        )
