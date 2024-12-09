from os import getenv
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = "postgresql+psycopg://postgres:reyasakura1@localhost:5432/db_fastapi"
    db_echo: bool = True


settings = Setting()
