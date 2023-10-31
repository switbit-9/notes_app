import sys
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from backend.app.config import Settings
from backend.app.dependencies import get_settings

__SETTINGS: Settings = get_settings()

__SQLALCHEMY_DATABASE_URL = 'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'.format(
    **dict(__SETTINGS)
)
# sys.stdout.write("=========================")
# sys.stdout.write(__SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    __SQLALCHEMY_DATABASE_URL,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_session() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
