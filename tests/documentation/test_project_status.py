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
    assert "STAGES 0–4 COMPLETE" in content
    assert "AUTHORIZED_BUILD_BOUNDARY:" in content
    assert "STAGE_5:" in content
    assert "STAGE_4: NOT AUTHORIZED" not in content
    assert "STAGE_4:\nNOT AUTHORIZED" not in content
    assert "STAGES 0–3 COMPLETE" not in content


def test_home_header_matches_current_status_footer():
    content = (ROOT / "00_HOME/ROBERT_HOME.md").read_text(encoding="utf-8")
    header = content.split("# OBJETIVO")[0]
    assert "**Versión:** 0.19" in header
    assert "DECISIÓN #046" in header
    assert "CAMBIO #072" in header
    assert "VERSION:\n0.19" in content


def test_context_header_no_longer_claims_stage_zero_only():
    content = (ROOT / "01_CONTEXT/ROBERT_CONTEXT_MASTER.md").read_text(encoding="utf-8")
    header = content.split("Uso principal:")[0]
    assert "Stages 0–4 implementados" in header
    assert "Stage 0 autorizado" not in content
    assert "TECHNICAL_IMPLEMENTATION = STAGE 0 COMPLETE" not in content
    assert "RUN PHASE 10 EXIT AUDIT AGAIN" not in content


@pytest.mark.parametrize(
    "path,heading",
    [
        ("03_DECISIONS/ROBERT_DECISIONS_LOG.md", "# DECISIÓN #046 —"),
        ("04_SECURITY/ROBERT_CONTROL_DE_CAMBIOS.md", "# CAMBIO #072 —"),
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
