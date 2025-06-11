from fastapi import APIRouter, HTTPException
from app.database import db
from app.schemas import Task, CreateTask
from bson import ObjectId
from datetime import datetime

router = APIRouter()

def task_serializer(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "created_at": task["created_at"],
        "updated_at": task["updated_at"],
        }
    
@router.post("/", response_model=Task)
async def create_task(task: CreateTask):
    now = datetime.utcnow()
    task_dict = task.dict()
    task_dict.update({"created_at": now, "updated_at": now})
    result = await db.tasks.insert_one(task_dict)
    new_task = await db.tasks.find_one({"_id":result.inserted_id})
    return task_serializer(new_task)

@router.get("/")
async def get_tasks():
    tasks = await db.tasks.find().to_list(100)
    return [task_serializer(task) for task in tasks]

@router.put("/{task_id}")
async def update_task(task_id: str, task: CreateTask):
    new_task = task.dict()
    new_task["updated_at"] = datetime.utcnow()
    
    result = await db.tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": new_task}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    
    updated_task = await db.tasks.find_one({"_id": ObjectId(task_id)})
    return task_serializer(updated_task)


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        old_task = await db.tasks.find_one({"_id": ObjectId(task_id)})
        if old_task is None:
            return {"message": "Task not found"}
        result = await db.tasks.delete_one({"_id": ObjectId(task_id)})
        if result:
            return {"message": "Task deleted successfully"}
        else:
            return {"message": "Task not found"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Task not found")
        
        