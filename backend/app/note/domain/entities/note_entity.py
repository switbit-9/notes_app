from datetime import datetime
from typing import Any, Callable
from backend.app.core.error.invalid_operation_exception import InvalidOperationError
import copy

class NoteEntity:

    def __init__(
        self,
        id_: int | None,
        title: str,
        description: str,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id_ = id_
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def __eq__(self, other) -> bool:
        if isinstance(other, NoteEntity):
            return self.id_ == other.id_

        return False

    def update_entity(
        self,
        entity_update_model: 'NoteUpdateModel',
        get_update_data_fn: Callable[['NoteUpdateModel'], dict[str, Any]]
    ) -> 'NoteEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity


    def mark_entity_as_deleted(self) -> 'NoteEntity':
        if self.is_deleted:
            raise InvalidOperationError('Note is marked as deleted')

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity
