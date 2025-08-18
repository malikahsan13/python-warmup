from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def showHelloWorld():
    return {"hello":"world"}


@app.get("/get_items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/get_items_query")
def get_item_query(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/get_item_both/{item_id}")
def get_item_both(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}