# app/core/config.py
from __future__ import annotations

from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


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

    # CORS (keep as string; parse later)
    CORS_ORIGINS: str = "*"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def cors_origins_list(self) -> List[str]:
        v = (self.CORS_ORIGINS or "").strip()
        if not v or v == "*":
            return ["*"]
        return [s.strip() for s in v.split(",") if s.strip()]


settings = Settings()


def get_cors_origins() -> List[str]:
    return settings.cors_origins_list
