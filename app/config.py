from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Line News Aggregator"
    DATABASE_URL: str
    
    # Добавляем новые настройки:
    LINE_CHANNEL_SECRET: str
    LINE_CHANNEL_ACCESS_TOKEN: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()