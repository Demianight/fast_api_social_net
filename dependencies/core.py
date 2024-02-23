from dotenv import load_dotenv
from sqlmodel import Session

from database.config import engine


def get_db():
    with Session(engine) as db:
        return db


def load_env():
    load_dotenv()
