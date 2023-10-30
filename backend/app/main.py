from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # You can specify the HTTP methods you want to allow
    allow_headers=["*"],  # You can specify the HTTP headers you want to allow
)
