from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):

    id: int | None = Field(primary_key=True, index=True, default=None)
    username: str = Field(unique=True)
    email: str = Field(unique=True)
    password: bytes
    is_active: bool = False
