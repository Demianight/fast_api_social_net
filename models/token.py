from sqlmodel import Field, SQLModel


class Token(SQLModel, table=True):

    id: int | None = Field(primary_key=True, index=True, default=None)
    token: str

    iat: int | None = None
    exp: int | None = None
