from typing import Optional, Sequence

import bcrypt
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from crud.interface import DBInterface
from models.user import User
from schemas.user import UserCreateSchema


class UserInterface(DBInterface[User]):
    def all(self, db: Session) -> Sequence[User]:
        sql = select(User)
        return db.exec(sql).all()

    def get(self, db: Session, pk: int) -> Optional[User]:
        return db.get(User, pk)

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, user: UserCreateSchema) -> User:
        db_post = User(
            username=user.username,
            email=user.email,
            password=self.hash_password(user.password)
        )

        db.add(db_post)
        db.commit()
        return db_post

    def delete(self, db: Session, pk: int) -> None:
        user = db.get(User, pk)
        if not user:
            raise HTTPException(404, 'No such user exist')

        db.delete(user)
        db.commit()

    def update(self, db: Session, pk: int, update_data: dict) -> User:
        user = db.get(User, pk)
        if not user:
            raise HTTPException(404, 'No such user exist')

        for key, val in update_data.items():
            setattr(user, key, val)

        db.add(user)
        db.commit()

        return user

    @staticmethod
    def hash_password(password: str) -> bytes:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt=salt)

    @staticmethod
    def validate_password(password: str, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password)
