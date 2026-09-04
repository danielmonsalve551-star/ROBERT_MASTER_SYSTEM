"""Immutable model profiles and explicitly supplied runtime state."""

from types import MappingProxyType

from robert.model.inputs import ModelProfile, ModelRuntimeState, snapshot


class ModelRegistry:
    def __init__(
        self,
        profiles: tuple[ModelProfile, ...],
        runtime_states: tuple[ModelRuntimeState, ...],
    ) -> None:
        profiles = tuple(snapshot(ModelProfile, item) for item in profiles)
        runtime_states = tuple(snapshot(ModelRuntimeState, item) for item in runtime_states)
        if not profiles:
            raise ValueError("at least one model profile is required")
        if len({item.model_id for item in profiles}) != len(profiles):
            raise ValueError("duplicate model profile")
        if len({item.model_id for item in runtime_states}) != len(runtime_states):
            raise ValueError("duplicate model runtime state")
        profile_ids = {item.model_id for item in profiles}
        if {item.model_id for item in runtime_states} != profile_ids:
            raise ValueError("every profile requires exactly one runtime state")
        self._profiles = MappingProxyType({item.model_id: item for item in profiles})
        self._states = MappingProxyType({item.model_id: item for item in runtime_states})

    @property
    def profiles(self) -> tuple[ModelProfile, ...]:
        return tuple(self._profiles.values())

    def profile(self, model_id: str) -> ModelProfile:
        return self._profiles[model_id]

    def runtime_state(self, model_id: str) -> ModelRuntimeState:
        return self._states[model_id]
