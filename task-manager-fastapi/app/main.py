from fastapi import FastAPI
from app.routes import task_routes

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
app.include_router(task_routes.router, prefix="/tasks", tags=["Tasks"])
