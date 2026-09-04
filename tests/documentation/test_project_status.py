from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.parametrize(
    "path",
    [
        "README.md",
        "00_HOME/ROBERT_HOME.md",
        "01_CONTEXT/ROBERT_CONTEXT_MASTER.md",
        "09_ARCHITECTURE/ROBERT_BUILD_ORDER.md",
    ],
)
def test_master_documents_agree_on_current_stage(path):
    content = (ROOT / path).read_text(encoding="utf-8")
    assert "STAGES 0–7 COMPLETE" in content
    assert "AUTHORIZED_BUILD_BOUNDARY:" in content
    assert "STAGE_7:" in content
    assert "STAGE_8:" in content
    assert "STAGE_8: NOT AUTHORIZED" in content or "STAGE_8:\nNOT AUTHORIZED" in content
    assert "STAGE_7: NOT AUTHORIZED" not in content
    assert "STAGE_7:\nNOT AUTHORIZED" not in content
    assert "STAGES 0–4 COMPLETE" not in content


def test_home_header_matches_current_status_footer():
    content = (ROOT / "00_HOME/ROBERT_HOME.md").read_text(encoding="utf-8")
    header = content.split("# OBJETIVO")[0]
    assert "**Versión:** 0.22" in header
    assert "DECISIÓN #049" in header
    assert "CAMBIO #075" in header
    assert "VERSION:\n0.22" in content


def test_context_header_no_longer_claims_stage_zero_only():
    content = (ROOT / "01_CONTEXT/ROBERT_CONTEXT_MASTER.md").read_text(encoding="utf-8")
    header = content.split("Uso principal:")[0]
    assert "Stages 0–7 implementados" in header
    assert "Stage 0 autorizado" not in content
    assert "TECHNICAL_IMPLEMENTATION = STAGE 0 COMPLETE" not in content
    assert "RUN PHASE 10 EXIT AUDIT AGAIN" not in content


@pytest.mark.parametrize(
    "path,heading",
    [
        ("03_DECISIONS/ROBERT_DECISIONS_LOG.md", "# DECISIÓN #047 —"),
        ("04_SECURITY/ROBERT_CONTROL_DE_CAMBIOS.md", "# CAMBIO #073 —"),
        ("03_DECISIONS/ROBERT_DECISIONS_LOG.md", "# DECISIÓN #048 —"),
        ("04_SECURITY/ROBERT_CONTROL_DE_CAMBIOS.md", "# CAMBIO #074 —"),
        ("03_DECISIONS/ROBERT_DECISIONS_LOG.md", "# DECISIÓN #049 —"),
        ("04_SECURITY/ROBERT_CONTROL_DE_CAMBIOS.md", "# CAMBIO #075 —"),
    ],
)
def test_new_governance_records_exist_exactly_once(path, heading):
    assert (ROOT / path).read_text(encoding="utf-8").count(heading) == 1


def test_implementation_and_audit_reports_are_present():
    for name in (
        "ROBERT_GOVERNANCE_CORE_IMPLEMENTATION.md",
        "ROBERT_STAGE_3_PREIMPLEMENTATION_AUDIT.md",
    ):
        content = (ROOT / "09_ARCHITECTURE" / name).read_text(encoding="utf-8")
        assert "#045" in content and "#071" in content


def test_validation_implementation_records_current_boundary():
    content = (ROOT / "09_ARCHITECTURE/ROBERT_VALIDATION_CORE_IMPLEMENTATION.md").read_text(
        encoding="utf-8"
    )
    assert "#046" in content and "#072" in content
    assert "STAGES 0–4 COMPLETE" in content
    assert "STAGE_5: NOT AUTHORIZED" in content


def test_context_memory_implementation_records_current_boundary():
    content = (
        ROOT / "09_ARCHITECTURE/ROBERT_CONTEXT_AND_MEMORY_INTERFACES_IMPLEMENTATION.md"
    ).read_text(encoding="utf-8")
    assert "#047" in content and "#073" in content
    assert "STAGES 0–5 COMPLETE" in content
    assert "STAGE_6: NOT AUTHORIZED" in content
    assert "AUTOMATIC_MEMORY_WRITE: DISABLED" in content


def test_model_interface_implementation_records_current_boundary():
    content = (ROOT / "09_ARCHITECTURE/ROBERT_MODEL_INTERFACE_IMPLEMENTATION.md").read_text(
        encoding="utf-8"
    )
    assert "#048" in content and "#074" in content
    assert "STAGES 0–6 COMPLETE" in content
    assert "STAGE_7: NOT AUTHORIZED" in content
    assert "REAL_PROVIDER_CONNECTIONS: DISABLED" in content


def test_skill_layer_implementation_records_current_boundary():
    content = (ROOT / "09_ARCHITECTURE/ROBERT_SKILL_LAYER_IMPLEMENTATION.md").read_text(
        encoding="utf-8"
    )
    assert "#049" in content and "#075" in content
    assert "STAGES 0–7 COMPLETE" in content
    assert "STAGE_8: NOT AUTHORIZED" in content
    assert "EXTERNAL_EFFECTS: DISABLED" in content
