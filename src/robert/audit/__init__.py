"""Append-only audit foundation for governed Robert operations."""

from robert.audit.catalog import ERROR_AND_BLOCKING_EVENT_CATALOG, ErrorAndBlockingEvent
from robert.audit.event_builder import AuditEventBuilder
from robert.audit.outcome_builder import ErrorAndBlockBuilder
from robert.audit.storage import JsonLinesAuditStore
from robert.audit.writer import AuditWriteError, AuditWriter

__all__ = [
    "ERROR_AND_BLOCKING_EVENT_CATALOG",
    "AuditEventBuilder",
    "AuditWriteError",
    "AuditWriter",
    "ErrorAndBlockBuilder",
    "ErrorAndBlockingEvent",
    "JsonLinesAuditStore",
]
