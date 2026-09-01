"""Minimal bootable API surface for Stage 0."""

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

from robert.config import Settings


class HealthResponse(BaseModel):
    """Non-operational health response for foundation verification."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    status: str
    service: str
    version: str
    autonomy_level: int
    execution_authority: str


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create the Stage 0 application without business or autonomous logic."""

    resolved_settings = settings or Settings.from_environment()
    app = FastAPI(
        title="Robert Master System",
        version="0.1.0",
        description="Stage 0 technical foundation. No execution authority.",
    )
    app.state.settings = resolved_settings

    @app.get("/health", response_model=HealthResponse, tags=["foundation"])
    def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            service="robert-master-system",
            version=app.version,
            autonomy_level=0,
            execution_authority="NONE",
        )

    return app


app = create_app()
