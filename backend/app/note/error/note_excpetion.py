from backend.app.core.error.base_exeption import BaseError

class NoteNotFoundError(BaseError):
    message = 'Note does not exist.'

class NotesNotFoundError(BaseError):
    message = 'Notes do not exist'


class NoteAlreadyExistsError(BaseError):
    message = 'Note already exists'
