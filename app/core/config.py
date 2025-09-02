# app/core/config.py
from __future__ import annotations

from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Commerce Agent"
    APP_ENV: str = "production"

    # Database
    DATABASE_URL: str  # required

    # Auth/JWT
    SECRET_KEY: str  # required
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Email (optional)
    SMTP_SERVER: Optional[str] = None
    SMTP_PORT: Optional[int] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    # Server
    PORT: Optional[int] = 10000

    # CORS (comma-separated string or "*")
    CORS_ORIGINS: Optional[str] = "*"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,   # allow SECRET_KEY / secret_key, etc.
        extra="ignore",         # ignore unknown env vars instead of failing
    )

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def normalize_cors(cls, v: Optional[str]) -> str | List[str]:
        if not v or v.strip() == "*":
            return ["*"]
        # Support comma-separated list
        return [item.strip() for item in v.split(",") if item.strip()]

    # Expose normalized list form for downstream use
    @property
    def cors_origins_list(self) -> List[str]:
        value = self.CORS_ORIGINS
        if isinstance(value, list):
            return value
        if not value:
            return ["*"]
        if value == "*":
            return ["*"]
        return [s.strip() for s in str(value).split(",") if s.strip()]


settings = Settings()


def get_cors_origins() -> List[str]:
    return settings.cors_origins_list
