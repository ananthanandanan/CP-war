import os


class AzureOpenAISettings(BaseSettings):
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    OPENAI_API_VERSION: str = "2023-05-15"
    AZURE_OPENAI_DEPLOYMENT: str

    class Config:
        env_file = None
        if os.getenv("RUN_ENV") != "production":
            env_file = ".env"


settings = AzureOpenAISettings()
