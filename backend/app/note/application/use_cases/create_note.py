from abc import abstractmethod
from typing import Tuple

from backend.app.core.application.use_case.use_case import BaseUseCase
from backend.app.note.domain.entities.note_api_model import NoteCreateModel,NoteReadModel
from backend.app.note.domain.entities.note_entity import NoteEntity
from backend.app.note.infrastructure.repositories import NoteUnitOfWork


class BaseCreateNoteUseCase(BaseUseCase[Tuple[NoteCreateModel], NoteReadModel]):

    unit_of_work: NoteUnitOfWork

    @abstractmethod
    def __call__(self, args: Tuple[NoteCreateModel]) -> NoteReadModel:
        raise NotImplementedError()


class CreateNoteUseCase(BaseCreateNoteUseCase):

    def __init__(self, unit_of_work: NoteUnitOfWork):
        self.unit_of_work = unit_of_work

    def __call__(self, args: Tuple[NoteCreateModel]) -> NoteReadModel:
        data, = args

        task = NoteEntity(
            id_=None,
            **data.dict()
        )


        try:
            new_task = self.unit_of_work.repository.create(task)
            created_task = self.unit_of_work.repository.find_by_id(new_task.id_)
            return NoteReadModel.from_entity(created_task)

        except Exception as _e:
            self.unit_of_work.rollback()
            raise



