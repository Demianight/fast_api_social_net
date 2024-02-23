
from typing import Optional, Protocol

from sqlmodel import Session


class DBInterface[V](Protocol):
    def all(self, db: Session) -> list[V]:
        ...

    def get(self, db: Session, pk: int) -> Optional[V]:
        ...

    def create(self, db: Session, obj) -> V:
        ...

    def update(self, db: Session, pk: int, update_data: dict) -> V:
        ...

    def delete(self, db: Session, pk) -> V:
        ...
