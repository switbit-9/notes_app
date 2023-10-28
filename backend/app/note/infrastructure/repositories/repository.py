from typing import Sequence

from sqlalchemy import select, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from backend.app.note.infrastructure.models.note import Note
from backend.app.note.domain.entities.note_entity import NoteEntity
from backend.app.note.domain.reposiries import BaseNoteRepository


class NoteRepository(BaseNoteRepository):

    def __init__(self, session: Session):
        self.session: Session = session

    def create(self, entity: NoteEntity) -> NoteEntity:
        task = Note.from_entity(entity)

        self.session.add(task)
        self.session.commit()

        return task.to_entity()

    def findall(self) -> Sequence[NoteEntity]:
        statement = select(Note)

        try:
            result: Sequence[Note] = self.session.execute(statement).scalars().all()
        except NoResultFound:
            return []

        return [task.to_entity() for task in result]

    def find_by_id(self, id_: int) -> NoteEntity | None:
        result: Note | None = self.session.get(Note, id_)

        if result is None:
            return None

        return result.to_entity()

    def update(self, entity: NoteEntity) -> NoteEntity:
        task = Note.from_entity(entity)
        update_data = task.to_dict()

        for key in [Note.updated_at.key, Note.created_at.key]:
            update_data.pop(key)

        statement = update(
            Note
        ).filter_by(
            id_=task.id_
        ).values(
            update_data
        ).returning(
            Note
        )

        task_mapping = self.session.execute(statement).mappings().one()
        result = Note(**task_mapping)

        return task.to_entity()

    def delete_by_id(self, id_: int) -> NoteEntity:
        statement = delete(
            Note
        ).filter_by(
            id_=id_
        ).returning(
            *Note.__table__.columns
        )

        result: Note = self.session.execute(statement).scalar_one()

        return result.to_entity()
