from abc import abstractmethod
from typing import Sequence

from backend.app.core.application.repository.base_repository import BaseRepository
from backend.app.note.domain.entities.note_entity import NoteEntity


class BaseNoteRepository(BaseRepository[NoteEntity]):
    pass


