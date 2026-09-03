import pytest

from robert.audit import AuditWriteError, AuditWriter
from robert.governance import GovernanceEngine, SecurityContext


@pytest.mark.parametrize("with_permission", [True, False])
def test_audit_failure_never_returns_an_allowed_result(request_data, grant, now, with_permission):
    class UnavailableStore:
        def append(self, payload):
            raise OSError("synthetic storage failure")

    engine = GovernanceEngine(AuditWriter(UnavailableStore()), clock=lambda: now)
    with pytest.raises(AuditWriteError):
        engine.evaluate(
            request_data,
            grant=grant if with_permission else None,
            security=SecurityContext(verified=True),
        )
