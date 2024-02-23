from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, EmailStr


class UserSchemaBase(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr


class UserSchema(UserSchemaBase):
    id: int
    is_active: bool


class UserCreateSchema(UserSchemaBase):
    password: Annotated[str, MinLen(5), MaxLen(30)]

    class Config:
        from_attributes = True


class UserUpdateSchema(UserSchemaBase):
    username: Annotated[str | None, MinLen(3), MaxLen(20)] = None
    password: Annotated[str | None, MinLen(5), MaxLen(30)] = None

    class Config:
        from_attributes = True
