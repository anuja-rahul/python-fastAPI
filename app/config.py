from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # SQLALCHEMY_DATABASE_URL: str
    HOST: str
    DBNAME: str
    USER: str
    PASSWORD: str
    PORT: str

    class Config:
        env_file = ".env"


settings = Settings()