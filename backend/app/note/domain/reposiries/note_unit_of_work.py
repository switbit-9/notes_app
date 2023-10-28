from backend.app.core.infrastructure.unit_of_work.unit_of_work import AbstractUnitOfWork
from backend.app.note.domain.reposiries.repositories import BaseNoteRepository


class BaseNoteUnitOfWork(AbstractUnitOfWork[BaseNoteRepository]):
    pass
