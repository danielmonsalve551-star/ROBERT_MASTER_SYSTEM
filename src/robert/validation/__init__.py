"""Deterministic, audited validation without approval or execution authority."""

from robert.validation.handler import ValidationHandler
from robert.validation.inputs import ValidationTarget

__all__ = ["ValidationHandler", "ValidationTarget"]
