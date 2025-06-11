from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    
class CreateTask(TaskBase):
    pass
    
class Task(TaskBase):
    pass
