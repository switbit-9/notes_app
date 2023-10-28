from abc import abstractmethod
from typing import cast, Tuple

from backend.app.note.error.note_excpetion import NoteNotFoundError
from backend.app.core.application.use_case.use_case import BaseUseCase
from backend.app.note.domain.entities.note_entity import NoteEntity
from backend.app.note.domain.entities.note_api_model import NoteReadModel
from backend.app.note.infrastructure.repositories import NoteUnitOfWork


class BaseDeleteNoteUseCase(BaseUseCase):
    unit_of_work: NoteUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> NoteReadModel:
        raise NotImplementedError()


class DeleteNoteUseCase(BaseDeleteNoteUseCase):

    def __init__(self, unit_of_work: NoteUnitOfWork):
        self.unit_of_work: NoteUnitOfWork = unit_of_work

    def __call__(self, args: Tuple[int]) -> NoteReadModel:
        id_, = args

        existing_user = self.unit_of_work.repository.find_by_id(id_)

        if existing_user is None:
            raise NoteNotFoundError()

        marked_task = existing_user.mark_entity_as_deleted()

        try:
            deleted_user = self.unit_of_work.repository.update(marked_task)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise

        return NoteReadModel.from_entity(cast(NoteEntity, deleted_user))
