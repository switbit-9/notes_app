from backend.app.core.application.repository.unit_of_work import AbstractUnitOfWork
from backend.app.note.infrastructure.repositories.repository import NoteRepository
from backend.app.note.domain.reposiries.note_unit_of_work import BaseNoteUnitOfWork
from sqlalchemy.orm import Session

class NoteUnitOfWork(BaseNoteUnitOfWork):

    def __init__(self, session: Session, repository: NoteRepository):
        self.session: Session = session
        self.repository: NoteRepository = repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()