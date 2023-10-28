from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from backend.app.core.infrastructure.models.models import Base
from backend.app.note.domain.entities import NoteEntity, NoteReadModel

class Note(Base):
    """
        Task DTO is an object associated with user entity
    """
    __tablename__ = 'notes'

    title: Mapped[str] | str = Column(String, index=True)
    description: Mapped[str] | str = Column(String)


    def to_entity(self) -> NoteEntity:
        return NoteEntity(
            id_=self.id_,
            title=self.title,
            is_deleted=self.is_deleted,
            description=self.description,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    def to_read_model(self) -> NoteReadModel:
        return NoteReadModel(
            id_=self.id_,
            title=self.title,
            is_deleted=self.is_deleted,
            description=self.description,
            updated_at=self.updated_at,
            created_at=self.created_at
        )

    def to_dict(self):
        return {
            'id_': self.id_,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'is_deleted': self.is_deleted,
        }

    @staticmethod
    def from_entity(task: NoteEntity) -> 'Note':
        return Note(
            id_=task.id_,
            title=task.title,
            is_deleted=task.is_deleted,
            description=task.description,
            updated_at=task.updated_at,
            created_at=task.created_at
        )
