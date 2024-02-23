from typing import Optional

from sqlmodel import Session, select

from crud.interface import DBInterface
from models.token import Token


class TokenInterface(DBInterface[Token]):
    def get_by_token(self, db: Session, token: str) -> Optional[Token]:
        sql = select(Token).where(Token.token == token)
        return db.exec(sql).first()

    def create(self, db: Session, token: str) -> Token:
        db_token = Token(token=token)
        db.add(db_token)
        db.commit()
        return db_token
