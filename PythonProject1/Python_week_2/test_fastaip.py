from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    text: str
    done: bool = False

tasks_db = []

@app.get("/tasks")
def get_tasks():
    return tasks_db

@app.post("/tasks")
def add_task(task: Task):
    tasks_db.append(task.model_dump())
    return {"status": "ok", "task": task}