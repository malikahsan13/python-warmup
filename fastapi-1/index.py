from fastapi import FastAPI
from routes.note import note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(note)

