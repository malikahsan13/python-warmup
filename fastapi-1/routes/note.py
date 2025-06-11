from fastapi import Request, APIRouter
from pydantic import BaseModel
from typing import Union
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from bson.errors import InvalidId

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# @note.get("/", response_class=HTMLResponse)
@note.get("/")
async def getIndex(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "note": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"],
        })
    return {"message": "Notes", "notes": newDocs}

@note.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@note.post("/note")
async def createNote(note: Note):
    conn.notes.notes.insert_one(dict(note))
    return {"message": "Note created", "note": note}


@note.put("/note/{note_id}")
async def updateNote(note_id: str, note: Note):
    
    try:
        oid = ObjectId(note_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid note ID")
    
    conn.notes.notes.update_one({"_id": oid}, {"$set": dict(note)})
    return {"message": "Note updated", "note": note}
