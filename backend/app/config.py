import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_name: str = 'Notes'

    db_host: str = os.environ.get('DB_HOST')
    db_user: str = os.environ.get('DB_USER')
    db_port: int = os.environ.get('DB_PORT')
    db_pass: str = os.environ.get('DB_PASS')
    db_name: str = os.environ.get('DB_NAME')
