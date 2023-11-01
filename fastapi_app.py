from fastapi import FastAPI, HTTPException
import db
from model import Task


app = FastAPI()

@app.get("/tasks")
async def get_tasks() -> list[Task]:
    """Get response with all tasks."""
    return db.get_all_tasks()


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> Task:
    """Delete task and return it if successful."""
    deleted_task = db.delete_task(task_id)
    print(task_id)
    if not deleted_task:
        raise HTTPException(404, "Task not found")
    return deleted_task


@app.post("/tasks", status_code=201)
def add_task(task: Task) -> Task:
    added_task = db.add_task(task)
    return added_task


@app.put("/tasks")
def update_task(task: Task) -> Task:
    updated_task = db.update_task(task)
    if not updated_task:
        raise HTTPException(400, "Could not update task")
    return updated_task
