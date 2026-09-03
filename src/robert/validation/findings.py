"""Internal findings mapped into canonical ValidationResult.checks and .issues."""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class CheckFinding:
    check_id: str
    validation_type: str
    status: Literal["PASS", "FAIL", "UNKNOWN"]
    message: str
    required: bool = True
    conflict: bool = False

    def as_check(self) -> dict:
        return dict(
            check_id=self.check_id,
            validation_type=self.validation_type,
            status=self.status,
            message=self.message,
            required=self.required,
        )

    def as_issue(self) -> dict | None:
        if self.status == "PASS":
            return None
        kind = "CONFLICT" if self.conflict else "FAILED_CHECK"
        if self.status == "UNKNOWN":
            kind = "UNAVAILABLE"
        if not self.required:
            kind = "WARNING"
        return dict(
            check_id=self.check_id,
            kind=kind,
            message=self.message,
            required=self.required,
            conflict=self.conflict,
        )
