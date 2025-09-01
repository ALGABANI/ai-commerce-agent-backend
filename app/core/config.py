from typing import List
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    PROJECT_NAME: str = "AI Commerce Agent"
    API_V1_STR: str = "/api"

    # Database
    DATABASE_URL: str  # e.g. postgresql+psycopg://user:pass@host/db?sslmode=require

    # Security
    JWT_SECRET_KEY: str  # set a strong random string
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    # CORS
    # Comma-separated list, e.g. "https://gabanilogistics.com,https://www.gabanilogistics.com"
    CORS_ORIGINS: str = ""

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()


def get_cors_origins() -> List[str]:
    if not settings.CORS_ORIGINS:
        return []
    return [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()]
