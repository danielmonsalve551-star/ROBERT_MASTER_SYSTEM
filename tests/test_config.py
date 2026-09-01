from pydantic import ValidationError
from pytest import MonkeyPatch, raises

from robert.config import Settings


def test_settings_load_safe_defaults(monkeypatch: MonkeyPatch) -> None:
    for name in (
        "ROBERT_ENVIRONMENT",
        "ROBERT_LOG_LEVEL",
        "ROBERT_API_HOST",
        "ROBERT_API_PORT",
    ):
        monkeypatch.delenv(name, raising=False)

    settings = Settings.from_environment()

    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.api_host == "127.0.0.1"
    assert settings.api_port == 8000


def test_settings_validate_environment_values(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("ROBERT_ENVIRONMENT", "test")
    monkeypatch.setenv("ROBERT_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("ROBERT_API_PORT", "9000")

    settings = Settings.from_environment()

    assert settings.environment == "test"
    assert settings.log_level == "DEBUG"
    assert settings.api_port == 9000


def test_settings_reject_invalid_port() -> None:
    with raises(ValidationError):
        Settings(api_port=0)
