from pydantic import Field, BaseModel
from pydantic import Field
from datetime import datetime
from backend.app.note.domain.entities.note_entity import NoteEntity

class NoteBaseModel(BaseModel):
    title: str = Field(example='Note title')
    description: str = Field(example='Note description')


class NoteCreateModel(NoteBaseModel):
    pass

class NoteUpdateModel(NoteBaseModel):
    pass

class NoteReadModel(NoteBaseModel):
    id_: int = Field(example=1)
    created_at: datetime
    updated_at: datetime


    class Config(object):
        orm_mode = True

    @classmethod
    def from_entity(cls, entity: NoteEntity) -> 'NoteReadModel':
        return cls(
            id_=entity.id_,
            title=entity.title,
            description=entity.description,
            is_deleted=entity.is_deleted,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )