from fastapi import FastAPI, HTTPException
app = FastAPI()
tasks_db = []
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

