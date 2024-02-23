from typing import Sequence

from fastapi import APIRouter, Depends
from sqlmodel import Session

from crud.post import PostInterface
from dependencies.core import get_db
from schemas.post import PostCreateSchema, PostSchema, PostUpdateSchema

router = APIRouter(prefix='/posts', tags=['posts'])


@router.get('/', response_model=Sequence[PostSchema])
async def get_posts(
    db: Session = Depends(get_db)
):
    return PostInterface().all(db)


@router.post('/', response_model=PostSchema)
async def create_post(
    post: PostCreateSchema, db: Session = Depends(get_db)
):
    return PostInterface().create(db, post)


@router.patch('/{post_id}/', response_model=PostSchema)
async def update_post(
    post_id: int, post: PostUpdateSchema, db: Session = Depends(get_db)
):
    update_data = post.model_dump(exclude_unset=True)
    return PostInterface().update(db, post_id, update_data)


@router.delete('/{post_id}/', status_code=204)
async def delete_post(
    post_id: int, db: Session = Depends(get_db)
):
    PostInterface().delete(db, post_id)
