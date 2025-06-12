import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/piadb")

settings = Settings()





class Settings(BaseSettings):
    # --- Basic Project Info ---
    PROJECT_NAME: str = "PIA Mining Network"
    API_VERSION: str = "v1"

    # --- Server Settings ---
    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # Change this in production!

    # --- Database ---
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/piadb")

    # --- Telegram Bot ---
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    BOT_USERNAME: str = os.getenv("BOT_USERNAME", "")

    # --- Frontend/Base URLs ---
    API_URL: str = os.getenv("API_URL", "http://localhost:8000")

    # --- Crypto Settings ---
    MINING_INTERVAL_HOURS: int = 12
    DEFAULT_REWARD: int = 10
    REFERRAL_REWARD: int = 5

    # --- Admin Controls ---
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "admin@example.com")

    class Config:
        case_sensitive = True
        env_file = ".env"


# Instantiate settings
settings = Settings()
