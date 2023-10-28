from fastapi import Depends, HTTPException, status

from backend.app.note.error.note_excpetion import NoteNotFoundError
from backend.app.note.dependencies import get_update_note_use_case
from backend.app.note.domain.entities.note_api_model import NoteReadModel, NoteUpdateModel
from backend.app.note.application.use_cases.update_note import UpdateNoteUseCase
from backend.app.note.api.routes import router
from backend.app.note.api.schemas.note_error_message import ErrorMessageNoteNotFound


@router.put(
    '/{id_}/',
    response_model=NoteReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageNoteNotFound
        }
    }
)
async def update_task(
    id_: int,
    data: NoteUpdateModel,
    update_task_use_case: UpdateNoteUseCase = Depends(get_update_note_use_case)
):
    try:
        user = update_task_use_case((id_, data))
    except NoteNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user
