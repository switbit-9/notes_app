from abc import abstractmethod
from typing import Tuple

from backend.app.note.error.note_excpetion import NoteNotFoundError
from backend.app.core.application.use_case.use_case import BaseUseCase
from backend.app.note.domain.entities.note_api_model import NoteReadModel
from backend.app.note.application.services import NoteQueryService


class BaseGetNoteUseCase(BaseUseCase[Tuple[int], NoteReadModel]):

    service: NoteQueryService

    @abstractmethod
    def __call__(self, args: Tuple[int]) -> NoteReadModel:
        raise NotImplementedError()


class GetNoteUseCase(BaseGetNoteUseCase):

    def __init__(self, service: NoteQueryService):
        self.service: NoteQueryService = service

    def __call__(self, args: Tuple[int]) -> NoteReadModel:
        id_, = args
        try:
            note = self.service.find_by_id(id_)
            if note is None:
                raise NoteNotFoundError()
        except Exception:
            raise

        return note