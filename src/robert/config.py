"""Environment-backed configuration for the Stage 0 foundation."""

import os
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Settings(BaseModel):
    """Validated runtime settings with safe local defaults."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    environment: Literal["development", "test", "production"] = "development"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    api_host: str = "127.0.0.1"
    api_port: int = Field(default=8000, ge=1, le=65535)

    @classmethod
    def from_environment(cls) -> "Settings":
        """Load only the Stage 0 configuration keys from the environment."""

        return cls(
            environment=os.getenv("ROBERT_ENVIRONMENT", "development"),
            log_level=os.getenv("ROBERT_LOG_LEVEL", "INFO"),
            api_host=os.getenv("ROBERT_API_HOST", "127.0.0.1"),
            api_port=os.getenv("ROBERT_API_PORT", "8000"),
        )
