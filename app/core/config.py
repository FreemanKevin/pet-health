from pydantic_settings import BaseSettings
from pydantic import Field, validator

class Settings(BaseSettings):
    # PostgreSQL 配置
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"  # 默认值
    POSTGRES_PORT: int = 5432         # 默认值
    DATABASE_URL: str = Field(default="", env="DATABASE_URL")

    # MinIO 配置
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_SECURE: bool = False  # 默认值
    MINIO_BUCKET: str

    @validator('DATABASE_URL', pre=True)
    def build_database_url(cls, v, values):
        if not v:
            return f"postgresql://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@{values['POSTGRES_HOST']}:{values['POSTGRES_PORT']}/{values['POSTGRES_DB']}"
        return v

    @validator('MINIO_SECURE', pre=True)
    def parse_minio_secure(cls, value):
        if isinstance(value, str):
            return value.lower() in ('true', '1', 't', 'y', 'yes')
        return value

    @validator('POSTGRES_USER', 'POSTGRES_PASSWORD', pre=True)
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            return value.strip()
        return value

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()