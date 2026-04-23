# uvicorn fast_api_1:app --reload писать для запуска сервера
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
tasks_db = []
class TaskCreate(BaseModel):
    task_name: str
    done: bool = False
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            tasks_db.remove(task)
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
@app.post("/tasks")
def create_task(task:TaskCreate):
    new_id = len(tasks_db)+1
    new_task = {"id": new_id, "task_name": task.task_name, "done": task.done}
    tasks_db.append(new_task)
    return new_task
