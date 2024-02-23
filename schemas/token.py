from pydantic import BaseModel, EmailStr


class TokenSchema(BaseModel):
    access_token: str
    token_type: str = 'Bearer'

    iat: int | None = None
    exp: int | None = None


class TokenCreateSchema(BaseModel):
    username: str
    password: str
    email: EmailStr
