from fastapi import FastAPI
from models.request import RequestBody

from agent.planner import create_plan
from agent.executor import execute_tasks
from services.doc_generator import generate_doc

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"AI Agent running"
    }

@app.post("/agent")
def agent(req: RequestBody):

    plan = create_plan(
        req.request
    )

    results = execute_tasks(
        plan["tasks"]
    )

    document = generate_doc(
        req.request,
        results
    )

    return {
        "request": req.request,
        "plan": plan,
        "document": document
    }
# python -m uvicorn app:app --reload