from pydantic import BaseModel


class PostSchemaBase(BaseModel):
    title: str
    description: str


class PostSchema(PostSchemaBase):
    id: int


class PostCreateSchema(PostSchemaBase):
    class Config:
        from_attributes = True


class PostUpdateSchema(PostSchemaBase):
    title: str | None = None
    description: str | None = None

    class Config:
        from_attributes = True
