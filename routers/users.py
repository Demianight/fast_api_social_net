from typing import Sequence
from uuid import uuid4

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlmodel import Session

from crud.user import UserInterface
from dependencies.core import get_db
from schemas.user import UserCreateSchema, UserSchema, UserUpdateSchema
from utils.confirmation import send_mail

router = APIRouter(prefix='/users', tags=['users'])


@router.get('', response_model=Sequence[UserSchema])
async def get_users(
    db: Session = Depends(get_db)
):
    return UserInterface().all(db)


@router.post('', response_model=UserSchema)
async def create_user(
    user: UserCreateSchema,
    tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):

    user_db = UserInterface().create(db, user)

    tasks.add_task(send_mail, user.email, str(user_db.id))

    return user_db


@router.patch('{user_id}/', response_model=UserSchema)
async def update_user(
    user_id: int, user: UserUpdateSchema, db: Session = Depends(get_db)
):
    update_data = user.model_dump(exclude_unset=True)
    return UserInterface().update(db, user_id, update_data)


@router.delete('{user_id}/', status_code=204)
async def delete_user(
    user_id: int, db: Session = Depends(get_db)
):
    UserInterface().delete(db, user_id)
