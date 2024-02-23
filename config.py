import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent

load_dotenv()


class AuthJWT(BaseModel):
    public_key: Path = BASE_DIR / 'certs' / 'jwt_public.pem'
    private_key: Path = BASE_DIR / 'certs' / 'jwt_private.pem'
    algorithm: str = 'RS256'


class Email(BaseModel):
    username: str = os.getenv('MAIL_USERNAME') or ''
    password: str = os.getenv('MAIL_PASSWORD') or ''
    host: str = os.getenv('MAIL_HOST') or ''
    port: int = int(os.getenv('MAIL_PORT') or 0)


class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()
    email: Email = Email()

    salt: str = os.getenv('SALT') or ''
    host: str = 'http://127.0.0.1:8000/%s'
    confirmation_url: str = 'http://127.0.0.1:8000/auth/confirm/%s'


settings = Settings()
