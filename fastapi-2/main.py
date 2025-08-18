from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse

class User(BaseModel):
    id: int
    name: str
    age: int = None
    dob: str = None

app = FastAPI()

@app.exception_handler(RequestValidationError)
def validation_error_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": "Invalid request 111", "details": exc.errors()}
    )
    
