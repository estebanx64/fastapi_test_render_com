from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI"
    secret_key: str


settings = Settings()
