from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb://localhost:27017")

@app.get("/", response_class=HTMLResponse)
async def getIndex(request: Request):
    docs = conn.notes.notes.find({})
    for doc in docs:
        print(doc["note"])
    return templates.TemplateResponse("index.html", { "request": request })

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
