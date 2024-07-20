import os


class AzureOpenAISettings(BaseSettings):
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    OPENAI_API_VERSION: str = "2023-07-01"  # Updated API version
    AZURE_OPENAI_DEPLOYMENT: str
    AZURE_OPENAI_MODEL: str  # Added new field

    class Config:
        env_file = None
        if os.getenv("RUN_ENV") != "production":
            env_file = ".env"


settings = AzureOpenAISettings()
