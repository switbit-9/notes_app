from pydantic import BaseModel, Field

from backend.app.note.error.note_excpetion import NoteNotFoundError, NotesNotFoundError


class ErrorMessageNoteNotFound(BaseModel):
    detail: str = Field(example=NoteNotFoundError.message)


class ErrorMessageNotesNotFound(BaseModel):
    detail: str = Field(example=NotesNotFoundError.message)

