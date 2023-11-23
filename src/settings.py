from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    config_path: str = Field(default="config/ai_models.json",
                             alias="CONFIG_PATH")

    class Config:
        # P.S - This is relative to where you're running the code from:
        env_file = ".env"


settings = Settings()
