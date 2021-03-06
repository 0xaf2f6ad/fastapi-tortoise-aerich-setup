from pydantic import BaseSettings
import dotenv
import os

dotenv.load_dotenv()


class _CoreConfig(BaseSettings):
    APP_NAME: str = "BoilerPlate API"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG_MODE: bool = os.getenv("DEBUG_MODE") == "true" or False
    DEBUG_SECRET: str = f"debugsecret101"


class _SecretsConfig(BaseSettings):
    SECRET: str = "supersecret"
    INTERNAL_API_KEY: str = "internalsupersecret"
    JWT_ACCESS_SECRET: str = "jwtas"
    JWT_REFRESH_SECRET: str = "jwtrs"
    SECURITY_ALGORITHM: str = "HS512"
    DEBUG_USER_PASSWORD: str = "debugger"


class _DBConfig(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL") or ""


class _MicroserviceUrls(BaseSettings):
    ...


class _OtherConfig(BaseSettings):
    ...


class _Settings(
    _DBConfig, _CoreConfig, _SecretsConfig, _MicroserviceUrls, _OtherConfig
):
    """yeye main secret initiation object"""


settings = _Settings()

global_vars = {}

print("[+] Settings :: \n> ", settings)
