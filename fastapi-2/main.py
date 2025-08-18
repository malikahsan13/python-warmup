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
        content={"error": "Invalid request", "details": exc.errors()}
    )
    
@app.exception_handler(Exception)
def generic_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "details": str(exc)}
    )
    
@app.post("/user")
def create_user(user: User):
    users = []
    try:
        # Simulate a database operation 
        # For example, you can use a database library like SQLAlchemy or asyncpg
        # For simplicity, we'll just store the user in memory
        users.append(user)
        return {"message": "User created successfully", "user": user}
    except ValueError as ve:
        raise HTTPException(status_code=400, details=f"Invalid input: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, details=f"Internal Server Error: {str(e)}")