# ملف config خاص بالإعدادات العامة
from functools import lru_cache
from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = Field("AI Commerce Agent", alias="APP_NAME")
    APP_ENV: str = "production"

    # DB URL جاي من .env
    DATABASE_URL: str

    # JWT
    JWT_SECRET_KEY: str = Field(..., alias="SECRET_KEY")
    JWT_ALGORITHM: str = Field("HS256", alias="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # SMTP Email
    SMTP_SERVER: str | None = None
    SMTP_PORT: int | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None

    # CORS
    CORS_ORIGINS: str = "*"

    # ربط الملف بالـ .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

settings = get_settings()

def get_cors_origins() -> List[str] | str:
    raw = settings.CORS_ORIGINS.strip()
    if raw == "*":
        return "*"
    return [o.strip() for o in raw.split(",") if o.strip()]
