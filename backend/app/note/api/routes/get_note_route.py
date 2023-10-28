from fastapi import Depends, status, HTTPException

from backend.app.note.error.note_excpetion import NoteNotFoundError
from backend.app.note.dependencies import get_note_use_case
from backend.app.note.domain.entities.note_api_model import NoteReadModel
from backend.app.note.application.use_cases.get_note import GetNoteUseCase
from backend.app.note.api.routes import router
from backend.app.note.api.schemas.note_error_message import ErrorMessageNoteNotFound


@router.get(
    '/{id_}/',
    response_model=NoteReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageNoteNotFound
        }
    }
)
def get_task(
    id_: int,
    get_task_use_case_: GetNoteUseCase = Depends(get_note_use_case)
):
    try:
        task = get_task_use_case_((id_, ))
    except NoteNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return task
