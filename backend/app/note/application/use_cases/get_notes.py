from abc import abstractmethod
from typing import Sequence

from backend.app.core.application.use_case.use_case import BaseUseCase
from backend.app.note.domain.entities.note_api_model import NoteReadModel
from backend.app.note.application.services import NoteQueryService


class BaseGetNotesUseCase(BaseUseCase[None, Sequence[NoteReadModel]]):

    service: NoteQueryService

    @abstractmethod
    def __call__(self, args: None) -> Sequence[NoteReadModel]:
        raise NotImplementedError()


class GetNotesUseCase(BaseGetNotesUseCase):

    def __init__(self, service: NoteQueryService):
        self.service: NoteQueryService = service

    def __call__(self, args: None) -> Sequence[NoteReadModel]:
        try:
            notes = self.service.findall()
        except Exception:
            raise

        return notes