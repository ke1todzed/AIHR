from pydantic_settings import BaseSettings
from pydantic import Field, AnyUrl

class Settings(BaseSettings):
    database_url: AnyUrl = Field(..., env="DATABASE_URL")
    debug: bool = Field(default=False, env="DEBUG")



settings = Settings()