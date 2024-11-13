from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        extra="ignore",
    )

    token: str
    admin: int
    logging_level: str = "INFO"
    api_url: str = "http://localhost:5555/translate"


config = Config()
