import pytest

from robert.skill import SkillRegistry, SkillStatus
from tests.memory.conftest import changed


def test_registry_returns_only_explicit_exact_identity(registry, manifest):
    assert registry.get(manifest.skill_id) == manifest
    assert registry.get("similar_skill") is None
    assert not hasattr(registry, "route")
    assert not hasattr(registry, "resolve")


def test_disabled_skill_is_not_available(manifest):
    registry = SkillRegistry((changed(manifest, status=SkillStatus.DISABLED),))
    assert registry.get(manifest.skill_id) is None


def test_registry_rejects_empty_and_duplicate_catalogs(manifest):
    with pytest.raises(ValueError, match="at least one"):
        SkillRegistry(())
    with pytest.raises(ValueError, match="duplicate"):
        SkillRegistry((manifest, manifest))


def test_manifest_rejects_external_effects_and_wildcard_requesters(manifest):
    with pytest.raises(ValueError, match="external effects"):
        changed(manifest, external_effects_allowed=True)
    with pytest.raises(ValueError, match="explicit"):
        changed(manifest, compatible_requesters=["*"])
