from typing import Sequence

from fastapi import HTTPException
from sqlmodel import Session, select

from crud.interface import DBInterface
from models import Post
from schemas.post import PostCreateSchema


class PostInterface(DBInterface[Post]):
    def all(self, db) -> Sequence[Post]:
        sql = select(Post)
        return db.exec(sql).all()

    def create(self, db: Session, post: PostCreateSchema) -> Post:
        db_post = Post(title=post.title, description=post.description)
        db.add(db_post)
        db.commit()
        return db_post

    def delete(self, db: Session, pk: int) -> None:
        post = db.get(Post, pk)
        if not post:
            raise HTTPException(404, 'No such post exist')

        db.delete(post)
        db.commit()

    def update(self, db: Session, pk: int, update_data: dict) -> Post:
        post = db.get(Post, pk)
        if not post:
            raise HTTPException(404, 'No such post exist')

        for key, val in update_data.items():
            setattr(post, key, val)

        db.add(post)
        db.commit()

        return post
