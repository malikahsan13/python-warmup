from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def showHelloWorld():
    return {"hello":"world"}