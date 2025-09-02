# app/core/config.py
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Commerce Agent"
    APP_ENV: str = "production"

    # Server
    PORT: int = 8000

    # DB
    DATABASE_URL: str

    # JWT
    JWT_SECRET_KEY: str = "change-this-to-a-long-random-secret"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Email
    SMTP_SERVER: str | None = None
    SMTP_PORT: int | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None

    # CORS (comma-separated string in .env, e.g. "*", or "https://a.com,https://b.com")
    CORS_ORIGINS: str = "*"

    # Load .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Back-compat alias so main.py can use settings.PROJECT_NAME if referenced anywhere
    @computed_field
    @property
    def PROJECT_NAME(self) -> str:
        return self.APP_NAME

    # Parsed CORS list
    @computed_field
    @property
    def CORS_ORIGINS_LIST(self) -> List[str]:
        raw = self.CORS_ORIGINS.strip()
        if not raw:
            return []
        if raw == "*":
            return ["*"]
        return [o.strip() for o in raw.split(",") if o.strip()]


settings = Settings()


def get_cors_origins() -> List[str]:
    return settings.CORS_ORIGINS_LIST
