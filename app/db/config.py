from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: AnyUrl = Field(..., env="DATABASE_URL")
    debug: bool = Field(default=False, env="DEBUG")



settings = Settings()
