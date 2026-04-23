from json import JSONDecodeError
from fastapi import FastAPI
import json
app = FastAPI()
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}
except JSONDecodeError:
    data = {}

@app.get("/analytics/summary")
def analysis():
    return data
@app.get("/analytics/chart")
def analysis_chart():
    by_manager = data.get("by_manager", {})
    labels = list(by_manager.keys())
    values = list(by_manager.values())
    return {"labels": labels, "values": values}
