from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session
from backend.app.note.infrastructure.models import Note
from backend.app.note.domain.entities import NoteReadModel
from backend.app.core.domain.services.base_query_service import QueryService


class BaseNoteQueryService(QueryService[NoteReadModel]):
    pass


class NoteQueryService(BaseNoteQueryService):

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id_: int) -> NoteReadModel | None:
        result = self.session.get(Note, id_)

        if result is None:
            return None

        return result.to_read_model()

    def findall(self) -> Sequence[NoteReadModel]:
        statement = select(Note)

        result = self.session.execute(statement).scalars().all()

        if len(result) == 0:
            return []

        return [task.to_read_model() for task in result]
