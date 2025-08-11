from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    database_url: Optional[str] = Field('postgresql+asyncpg://myuser:mypassword@database:5432/mydatabase')
    postgres_user: Optional[str] = Field('myuser')
    postgres_password: Optional[str] = Field('mypassword')
    postgres_db: Optional[str] = Field('mydatabase')

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


appsettings = AppSettings()
