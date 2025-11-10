from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
from database import engine, Base
from models import todo_models, user_models
from celery.result import AsyncResult
from tasks.task import add


from api.todo_api import protected_router as todo_router
from auth.auth_api import router as auth_router


app = FastAPI() 
# Assigns the lifespan to the FastAPI app.
# Base.metadata.create_all(bind=engine)

app.include_router(todo_router)
app.include_router(auth_router)


@app.get("/")
def display_root_message():
    return{"Message": "Welcome to todo app"}


@app.post("/celery/")
def test_celery_task(x: int, y: int):
    task = add.delay(x,y)
    return{"task_id": task.id}


@app.get("/celery")
async def get_result_from_celery(task_id: str):
    task_result = AsyncResult(task_id)
    print(">>>>",task_result.state)

    if task_result.ready():
        return{"task_id": task_id, "result": task_result.result
               }
    else:
        return{"status": "pending"}
