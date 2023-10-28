from fastapi import APIRouter

router = APIRouter(
    prefix='/notes',
    tags=['notes'],
)

from backend.app.note.api.routes.delete_note_route import delete_task
from backend.app.note.api.routes.update_task_route import update_task
from backend.app.note.api.routes.create_note_route import create_task
from backend.app.note.api.routes.get_note_route import get_task
from backend.app.note.api.routes.get_notes_route import get_tasks

notes_router = router