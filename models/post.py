from sqlmodel import Field, SQLModel


class Post(SQLModel, table=True):

    id: int | None = Field(primary_key=True, index=True, default=None)
    title: str
    description: str
