"""
Hands-On 6 : Configuration
Centralised, environment-driven configuration for the ORM layer.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_ENGINE = os.getenv("DB_ENGINE", "postgresql")  # postgresql | mysql
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "college_db_orm")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

    # Connection pool tuning
    POOL_SIZE = int(os.getenv("DB_POOL_SIZE", 5))
    MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", 10))
    POOL_TIMEOUT = int(os.getenv("DB_POOL_TIMEOUT", 30))
    POOL_RECYCLE = int(os.getenv("DB_POOL_RECYCLE", 1800))  # seconds

    ECHO_SQL = os.getenv("DB_ECHO", "False").lower() == "true"

    @property
    def sqlalchemy_url(self) -> str:
        if self.DB_ENGINE == "mysql":
            return (
                f"mysql+mysqlconnector://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT or 3306}/{self.DB_NAME}"
            )
        # default: postgresql
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT or 5432}/{self.DB_NAME}"
        )


config = Config()
