from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.note.domain.reposiries import (
    BaseNoteUnitOfWork,
    BaseNoteRepository
)
from backend.app.note.infrastructure.repositories import (
    NoteUnitOfWork,
    NoteRepository
)

from backend.app.note.application.services import NoteQueryService, BaseNoteQueryService

from backend.app.note.application.use_cases import (
    BaseUpdateNoteUseCase,
    BaseGetNotesUseCase,
    BaseGetNoteUseCase,
    BaseDeleteNoteUseCase,
    BaseCreateNoteUseCase,
    UpdateNoteUseCase,
    GetNoteUseCase,
    GetNotesUseCase,
    DeleteNoteUseCase,
    CreateNoteUseCase
)

from backend.app.core.database.database import get_session


def get_note_query_service(
    session: Session = Depends(get_session)
) -> BaseNoteQueryService:
    return NoteQueryService(session)


def get_note_repository(session: Session = Depends(get_session)) -> BaseNoteRepository:
    return NoteRepository(session)


def get_note_unit_of_work(
    session: Session = Depends(get_session),
    note_repository: BaseNoteRepository = Depends(get_note_repository)
) -> BaseNoteUnitOfWork:
    return NoteUnitOfWork(session, note_repository)


def get_notes_use_case(
    note_query_service: BaseNoteQueryService = Depends(get_note_query_service)
) -> BaseGetNotesUseCase:
    return GetNotesUseCase(note_query_service)


def get_create_note_use_case(
    note_unit_of_work: BaseNoteUnitOfWork = Depends(get_note_unit_of_work)
) -> BaseCreateNoteUseCase:
    return CreateNoteUseCase(note_unit_of_work)


def get_delete_note_use_case(
    note_unit_of_work: BaseNoteUnitOfWork = Depends(get_note_unit_of_work)
) -> BaseDeleteNoteUseCase:
    return DeleteNoteUseCase(note_unit_of_work)


def get_note_use_case(
    note_query_service: BaseNoteQueryService = Depends(get_note_query_service)
) -> BaseGetNoteUseCase:
    return GetNoteUseCase(note_query_service)


def get_update_note_use_case(
    note_unit_of_work: BaseNoteUnitOfWork = Depends(get_note_unit_of_work)
) -> BaseUpdateNoteUseCase:
    return UpdateNoteUseCase(note_unit_of_work)
