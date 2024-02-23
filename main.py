from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.config import create_db
from dependencies.core import load_env
from routers import auth, posts, users


@asynccontextmanager
async def startup(app: FastAPI):
    create_db()
    load_env()
    yield


app = FastAPI(lifespan=startup)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/')
async def root():
    return 'Hello, world'
