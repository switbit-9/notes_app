from backend.app.core.domain.services.base_query_service import QueryService
from backend.app.note.domain.entities import NoteReadModel


class BaseNoteQueryService(QueryService[NoteReadModel]):
    pass
