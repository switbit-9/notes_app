from functools import lru_cache
from backend.app.config import Settings


@lru_cache()
def get_settings():
    return Settings()