from pydantic import BaseSettings
from functools import lru_cache

from .settings import ENV, URL, DB


class Settings(BaseSettings):
    env: str = ENV
    url: str = URL
    db: str = DB


@lru_cache
def start_settings() -> Settings:
    settings = Settings()
    print(f"Загрузка настроек: {settings.env}")
    return settings
