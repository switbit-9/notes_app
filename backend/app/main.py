from fastapi import FastAPI

from backend.app.core.database.database import engine
from backend.app.core.infrastructure.models import models
from backend.app.note.api.routes import notes_router

app = FastAPI()
app.include_router(notes_router)


@app.on_event('startup')
def startup_event():
    models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
