from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def showHelloWorld():
    return {"hello":"world"}


@app.get("get_items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}