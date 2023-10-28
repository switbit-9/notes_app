from fastapi import status, Depends, HTTPException, Response, Request

from backend.app.note.dependencies import get_create_note_use_case
from backend.app.note.domain.entities.note_api_model import NoteCreateModel, NoteReadModel
from backend.app.note.application.use_cases.create_note import CreateNoteUseCase
from backend.app.note.api.routes import router


@router.post(
    '/',
    response_model=NoteReadModel,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    data: NoteCreateModel,
    response: Response,
    request: Request,
    create_task_use_case: CreateNoteUseCase = Depends(get_create_note_use_case)
):
    try:
        note = create_task_use_case((data, ))
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    response.headers['location'] = f"{request.url.path}{note.id_}"
    return note
