"""Audited SkillInvocation → internal procedure → SkillResult boundary."""

from robert.audit import AuditEventBuilder, AuditWriter
from robert.audit.redaction import redact_sensitive_values
from robert.contracts.skill import SkillInvocation, SkillResult
from robert.skill.inputs import SkillProcedureOutput, SkillStatus, snapshot
from robert.skill.procedure import SkillProcedure
from robert.skill.registry import SkillRegistry


class SkillRunner:
    def __init__(
        self,
        registry: SkillRegistry,
        procedures: tuple[SkillProcedure, ...],
        writer: AuditWriter,
    ) -> None:
        if len({item.skill_id for item in procedures}) != len(procedures):
            raise ValueError("duplicate Skill procedure")
        self._registry = registry
        self._procedures = {item.skill_id: item for item in procedures}
        self._writer = writer

    def run(self, invocation: SkillInvocation, *, requester: str) -> SkillResult:
        invocation = snapshot(SkillInvocation, invocation)
        manifest = self._registry.get(invocation.skill_id)
        error = self._preflight(invocation, requester, manifest)
        if error is not None:
            return self._result(invocation, requester, "BLOCKED", None, error)
        assert manifest is not None
        procedure = self._procedures.get(manifest.skill_id)
        if procedure is None or (procedure.skill_id, procedure.version) != (
            manifest.skill_id,
            manifest.version,
        ):
            return self._result(
                invocation, requester, "BLOCKED", None, "SKILL_PROCEDURE_UNAVAILABLE"
            )
        try:
            output = snapshot(SkillProcedureOutput, procedure.process(invocation))
        except (ValueError, TypeError):
            return self._result(invocation, requester, "FAILED", None, "INVALID_SKILL_INPUT")
        except Exception:
            return self._result(invocation, requester, "FAILED", None, "SKILL_PROCEDURE_FAILED")
        error = self._validate_output(manifest, output)
        if error is not None:
            return self._result(invocation, requester, "FAILED", None, error)
        return self._result(invocation, requester, "COMPLETED", output, None)

    @staticmethod
    def _preflight(invocation, requester, manifest):
        if manifest is None:
            return "SKILL_NOT_AVAILABLE"
        if manifest.status not in (SkillStatus.IMPLEMENTED, SkillStatus.AVAILABLE):
            return "SKILL_NOT_AVAILABLE"
        if requester not in manifest.compatible_requesters:
            return "REQUESTER_NOT_AUTHORIZED"
        if invocation.skill_version != manifest.version:
            return "SKILL_VERSION_MISMATCH"
        if redact_sensitive_values(invocation.model_dump(mode="json")) != invocation.model_dump(
            mode="json"
        ):
            return "SENSITIVE_DATA_REJECTED"
        if any(field not in invocation.inputs for field in manifest.required_inputs):
            return "MISSING_INPUT"
        if any(field not in invocation.context for field in manifest.required_context):
            return "MISSING_CONTEXT"
        expected = manifest.output_contract.model_dump(mode="json")
        if invocation.expected_output != expected:
            return "OUTPUT_CONTRACT_MISMATCH"
        if tuple(invocation.constraints) != manifest.constraints:
            return "CONSTRAINT_MISMATCH"
        if tuple(invocation.tool_requirements) != manifest.tool_requirements:
            return "TOOL_REQUIREMENT_MISMATCH"
        if tuple(invocation.model_requirements) != manifest.model_requirements:
            return "MODEL_REQUIREMENT_MISMATCH"
        if tuple(invocation.memory_requirements) != manifest.memory_requirements:
            return "MEMORY_REQUIREMENT_MISMATCH"
        if tuple(invocation.validation_requirements) != manifest.validation_requirements:
            return "VALIDATION_REQUIREMENT_MISMATCH"
        if invocation.preconditions:
            return "CALLER_PRECONDITIONS_UNSUPPORTED"
        return None

    @staticmethod
    def _validate_output(manifest, output):
        if redact_sensitive_values(output.model_dump(mode="json")) != output.model_dump(
            mode="json"
        ):
            return "SENSITIVE_OUTPUT_REJECTED"
        if not isinstance(output.output, dict):
            return "OUTPUT_CONTRACT_FAILED"
        fields = set(output.output)
        required = set(manifest.output_contract.required)
        if not required.issubset(fields):
            return "OUTPUT_CONTRACT_FAILED"
        if not manifest.output_contract.allow_additional and fields != required:
            return "OUTPUT_CONTRACT_FAILED"
        if output.tool_requests and not manifest.tool_requirements:
            return "UNAUTHORIZED_TOOL_REQUEST"
        if output.model_requests and not manifest.model_requirements:
            return "UNAUTHORIZED_MODEL_REQUEST"
        if output.memory_candidates and not manifest.memory_requirements:
            return "UNAUTHORIZED_MEMORY_CANDIDATE"
        return None

    def _result(self, invocation, requester, status, output, error):
        output = output or SkillProcedureOutput(output=None)
        event = self._writer.write(
            AuditEventBuilder().build(
                task_id=invocation.task_id,
                event_type="SKILL_RUN_COMPLETED" if status == "COMPLETED" else "SKILL_RUN_FAILED",
                actor=requester,
                component="SKILL_RUNNER",
                action="PROCESS_SKILL_INVOCATION",
                target=invocation.skill_id,
                result={
                    "status": status,
                    "external_side_effects": False,
                    "tool_requests_executed": False,
                    "model_requests_executed": False,
                    "memory_written": False,
                    "execution_authority": "NONE",
                },
                metadata={"skill_version": invocation.skill_version, "error_code": error},
            )
        )
        return SkillResult(
            contract_version="0.1",
            task_id=invocation.task_id,
            skill_id=invocation.skill_id,
            skill_version=invocation.skill_version,
            status=status,
            output=output.output,
            derived_data=output.derived_data,
            tool_requests=list(output.tool_requests) if status == "COMPLETED" else [],
            model_requests=list(output.model_requests) if status == "COMPLETED" else [],
            memory_candidates=list(output.memory_candidates) if status == "COMPLETED" else [],
            validation_requests=list(output.validation_requests) if status == "COMPLETED" else [],
            warnings=list(output.warnings),
            errors=[{"code": error}] if error else [],
            audit_refs=[event.event_id],
        )
