"""Explicit Skill catalog; lookup is not routing authority."""

from types import MappingProxyType

from robert.skill.inputs import SkillManifest, SkillStatus, snapshot


class SkillRegistry:
    def __init__(self, manifests: tuple[SkillManifest, ...]) -> None:
        manifests = tuple(snapshot(SkillManifest, item) for item in manifests)
        if not manifests:
            raise ValueError("at least one Skill manifest is required")
        if len({item.skill_id for item in manifests}) != len(manifests):
            raise ValueError("duplicate Skill identity")
        names = {(item.name.casefold(), item.version) for item in manifests}
        if len(names) != len(manifests):
            raise ValueError("duplicate Skill name and version")
        self._manifests = MappingProxyType({item.skill_id: item for item in manifests})

    @property
    def manifests(self) -> tuple[SkillManifest, ...]:
        return tuple(self._manifests.values())

    def get(self, skill_id: str) -> SkillManifest | None:
        """Return only an exact explicitly requested Skill; never select or route."""
        manifest = self._manifests.get(skill_id)
        if manifest is None or manifest.status == SkillStatus.DISABLED:
            return None
        return manifest
