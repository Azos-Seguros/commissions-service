from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings


class EnvironmentEnum(str, Enum):
    """Enum for Environment label values."""

    MAIN = "main"
    STAGING = "staging"
    DEV = "dev"
    TEST = "test"


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file.

    Attributes:
        db_uri: Complete database connection URI
    """

    azos_env: str = Field(default="test")
    project_id: str = Field(default="project_id")
    log_level: str = Field(default="INFO")
    log_file_path: str = Field(default="app.log")
    root_path: str = Field(default="")

    # Database settings
    postgres_uri: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/commissions_db"
    )

    # MongoDB settings
    mongodb_uri: str = Field(default="mongodb://localhost:27017/commissions_db")

    class Config:
        env_file = ".env"
        extra = "ignore"

    def is_test_env(self) -> bool:
        """True if the environment point to test."""
        return self.azos_env.strip().lower() in ["test"]

    def is_development_env(self) -> bool:
        """True if the environment point to development."""
        return self.azos_env.strip().lower() in ["dev", "development"]

    def is_staging_env(self) -> bool:
        """True if the environment point to staging."""
        return self.azos_env.strip().lower() in ["staging"]

    def is_production_env(self) -> bool:
        """True if the environment point to production."""
        return self.azos_env.strip().lower() in ["prod", "production", "main"]

    def get_service_name(self) -> str:
        """Return a string for service name."""
        return "commissions-service"

    def get_env_label(self) -> str:
        """Return a string label for environment."""
        if self.is_production_env():
            return EnvironmentEnum.MAIN.value
        if self.is_staging_env():
            return EnvironmentEnum.STAGING.value
        if self.is_development_env():
            return EnvironmentEnum.DEV.value
        return EnvironmentEnum.TEST.value


settings = Settings()
