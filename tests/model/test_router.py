import pytest

from robert.model import (
    ModelAvailability,
    ModelCapability,
    ModelRegistry,
    ModelRequirements,
    ModelRouter,
    ModelRoutingError,
)
from tests.memory.conftest import changed
from tests.model.conftest import make_profile, make_state


def test_router_selects_best_eligible_fit_deterministically(model_request, requirements):
    preferred = make_profile(model_id="model_b", adapter_id="adapter_b", priority=20)
    other = make_profile(
        model_id="model_a",
        adapter_id="adapter_a",
        priority=100,
        capabilities=(ModelCapability.REASONING, ModelCapability.STRUCTURED_OUTPUT),
    )
    registry = ModelRegistry(
        (other, preferred),
        (make_state(other.model_id), make_state(preferred.model_id)),
    )

    ranked = ModelRouter(registry).rank(model_request, requirements)

    assert [item.model_id for item in ranked] == ["model_b", "model_a"]
    assert "deterministic" in ranked[0].selection_reason


@pytest.mark.parametrize(
    "case",
    [
        "missing_capability",
        "unavailable",
        "disabled",
        "rate_limited",
        "context_limit",
        "provider",
        "sensitivity",
        "tool_support",
        "structured_output",
    ],
)
def test_router_excludes_models_that_fail_mandatory_constraints(model_request, requirements, case):
    profile = make_profile()
    state = make_state()
    if case == "missing_capability":
        requirements = changed(
            requirements,
            required_capabilities=[ModelCapability.VISION],
        )
    elif case == "unavailable":
        state = make_state(availability=ModelAvailability.UNAVAILABLE)
    elif case == "disabled":
        state = make_state(availability=ModelAvailability.DISABLED)
    elif case == "rate_limited":
        state = make_state(rate_limited=True)
    elif case == "context_limit":
        requirements = changed(requirements, context_units=1001)
    elif case == "provider":
        model_request = changed(model_request, provider_requirement="OTHER_PROVIDER")
    elif case == "sensitivity":
        model_request = changed(model_request, sensitivity="RESTRICTED")
    elif case == "tool_support":
        model_request = changed(model_request, tool_request_allowed=True)
    elif case == "structured_output":
        profile = make_profile(
            capabilities=(ModelCapability.REASONING, ModelCapability.SUMMARIZATION)
        )
    router = ModelRouter(ModelRegistry((profile,), (state,)))

    with pytest.raises(ModelRoutingError, match="mandatory"):
        router.rank(model_request, requirements)


def test_registry_rejects_missing_or_duplicate_runtime_identity():
    profile = make_profile()
    with pytest.raises(ValueError, match="runtime"):
        ModelRegistry((profile,), ())
    with pytest.raises(ValueError, match="duplicate"):
        ModelRegistry((profile, profile), (make_state(),))


def test_fallback_ranking_prefers_available_over_degraded(model_request, requirements):
    degraded = make_profile(model_id="model_degraded", adapter_id="adapter_degraded", priority=100)
    available = make_profile(model_id="model_available", adapter_id="adapter_available", priority=1)
    registry = ModelRegistry(
        (degraded, available),
        (
            make_state(degraded.model_id, ModelAvailability.DEGRADED),
            make_state(available.model_id),
        ),
    )
    assert ModelRouter(registry).rank(model_request, requirements)[0].model_id == "model_available"


def test_requirements_bound_retry_attempts():
    with pytest.raises(ValueError):
        ModelRequirements(max_attempts=4)
