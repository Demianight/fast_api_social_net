from functools import cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent

load_dotenv()


class AuthJWT(BaseModel):
    public_key: Path = BASE_DIR / 'certs' / 'jwt_public.pem'
    private_key: Path = BASE_DIR / 'certs' / 'jwt_private.pem'
    algorithm: str = 'RS256'


class Mail(BaseModel):
    username: str
    password: str
    host: str
    port: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_nested_delimiter='_'
    )

    auth_jwt: AuthJWT = AuthJWT()
    mail: Mail

    salt: str

    host: str = 'http://127.0.0.1:8000/%s'
    confirmation_url: str = 'http://127.0.0.1:8000/auth/confirm/%s'


@cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
