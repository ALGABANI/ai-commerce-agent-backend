# app/core/config.py
from functools import lru_cache
from typing import List

from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ---- App ----
    PROJECT_NAME: str = Field("AI Commerce Agent", alias="APP_NAME")
    APP_ENV: str = "production"

    # ---- Database ----
    DATABASE_URL: AnyUrl

    # ---- Auth/JWT ----
    JWT_SECRET_KEY: str = Field(..., alias="SECRET_KEY")
    JWT_ALGORITHM: str = Field("HS256", alias="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ---- Email (optional) ----
    SMTP_SERVER: str | None = None
    SMTP_PORT: int | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None

    # ---- CORS ----
    # Accept either CSV string "https://a,https://b" or "*"
    CORS_ORIGINS: str = "*"

    # Render provides PORT env automatically; we don’t need to use it directly
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


def get_cors_origins() -> List[str] | str:
    raw = settings.CORS_ORIGINS.strip()
    if raw == "*":
        return "*"
    # split by comma and trim
    return [o.strip() for o in raw.split(",") if o.strip()]
