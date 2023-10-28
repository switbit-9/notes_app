import time

from fastapi import Depends, status, HTTPException

from backend.app.note.dependencies import get_notes_use_case
from backend.app.note.domain.entities.note_api_model import NoteReadModel
from backend.app.note.application.use_cases.get_notes import GetNotesUseCase
from backend.app.note.api.schemas.note_error_message import ErrorMessageNotesNotFound
from backend.app.note.api.routes import router


@router.get(
    '/',
    response_model=list[NoteReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageNotesNotFound
        }
    }
)
def get_tasks(
    skip: int = 0,
    limit: int = 100,
    get_tasks_use_case_: GetNotesUseCase = Depends(get_notes_use_case)
):
    time.sleep(5)
    try:
        tasks = get_tasks_use_case_(None)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return tasks
