from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session

from crud.token import TokenInterface
from crud.user import UserInterface
from dependencies.core import get_db
from models.token import Token
from models.user import User
from schemas.token import TokenCreateSchema
from utils.hash import decode_jwt

http_bearer = HTTPBearer()


def get_token(
    creds: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
    db: Session = Depends(get_db)
) -> Token:

    if not (token := TokenInterface().get_by_token(db, creds.credentials)):
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            'Invalid token'
        )
    return token


def get_user(
    token: Token = Depends(get_token),
    db: Session = Depends(get_db)

) -> User:
    payload = decode_jwt(token.token)
    username = payload['username']

    if not (user := UserInterface().get_by_username(db, username)):
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            'Invalid token'
        )
    return user


def get_active_user(
        user: User = Depends(get_user)
):
    if not user.is_active:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            'User inactive'
        )
    return user


def verify_login(
        login: TokenCreateSchema,
        db: Session = Depends(get_db)
):
    user = UserInterface().get_by_username(db, login.username)
    if (
        not user or
        not UserInterface.validate_password(login.password, user.password)
    ):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            'Wrong username or password'
        )

    return login
