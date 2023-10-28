from abc import abstractmethod
from typing import cast, Tuple

from backend.app.note.error.note_excpetion import NoteNotFoundError
from backend.app.core.application.use_case.use_case import BaseUseCase
from backend.app.note.domain.entities.note_api_model import NoteUpdateModel, NoteReadModel
from backend.app.note.domain.entities.note_entity import NoteEntity
from backend.app.note.infrastructure.repositories import NoteUnitOfWork


class BaseUpdateNoteUseCase(BaseUseCase[Tuple[int, NoteUpdateModel], NoteReadModel]):

    unit_of_work: NoteUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[int, NoteUpdateModel]) -> NoteReadModel:
        raise NotImplementedError()


class UpdateNoteUseCase(BaseUpdateNoteUseCase):

    def __init__(self, unit_of_work: NoteUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[int, NoteUpdateModel]) -> NoteReadModel:
        id_, update_data = args
        existing_task = self.unit_of_work.repository.find_by_id(id_)

        if existing_task is None:
            raise NoteNotFoundError()

        update_entity = existing_task.update_entity(
            update_data,
            lambda task_data: task_data.dict(exclude_unset=True)
        )

        try:
            updated_task = self.unit_of_work.repository.update(update_entity)
            self.unit_of_work.commit()
        except Exception:
            self.unit_of_work.rollback()
            raise


        return NoteReadModel.from_entity(cast(NoteEntity, updated_task))
