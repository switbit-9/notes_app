import time

from fastapi import HTTPException, Depends, status

from backend.app.note.error.note_excpetion import NoteNotFoundError
from backend.app.note.dependencies import get_delete_note_use_case
from backend.app.note.domain.entities.note_api_model import NoteReadModel
from backend.app.note.application.use_cases.delete_note import DeleteNoteUseCase
from backend.app.note.api.routes import router
from backend.app.note.api.schemas.note_error_message import ErrorMessageNoteNotFound


@router.delete(
    '/{id_}/',
    response_model=NoteReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageNoteNotFound
        }
    }
)
def delete_task(
    id_: int,
    delete_task_use_case: DeleteNoteUseCase = Depends(get_delete_note_use_case)
):
    try:
        time.sleep(7)
        task = delete_task_use_case((id_, ))
    except NoteNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return task
