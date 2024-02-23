from fastapi import APIRouter, Depends
from sqlmodel import Session

from crud.token import TokenInterface
from crud.user import UserInterface
from dependencies.auth import get_active_user, verify_login
from dependencies.core import get_db
from models.user import User
from schemas.token import TokenCreateSchema, TokenSchema
from schemas.user import UserSchema
from utils.hash import encode_jwt

router = APIRouter(prefix='/auth', tags=['auth'])


@router.get('/me', response_model=UserSchema)
async def me(
    user: User = Depends(get_active_user),
):
    return user


@router.post('/login', response_model=TokenSchema)
async def obtain_token(
    login: TokenCreateSchema = Depends(verify_login),
    db: Session = Depends(get_db)
):
    jwt_payload = {
        'sub': login.username,
        'username': login.username,
    }
    token = encode_jwt(jwt_payload)

    TokenInterface().create(db, token)

    return TokenSchema(access_token=token)


@router.get('/confirm/{user_id}')
async def confirm_user_email(
    user_id: int,
    db: Session = Depends(get_db)
):
    return UserInterface().update(db, user_id, {'is_active': True})
