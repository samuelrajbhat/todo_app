from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
from database import engine, Base
from models import todo_models, user_models



from api.todo_api import protected_router as todo_router
from auth.auth_api import router as auth_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(todo_router)
app.include_router(auth_router)

@app.get("/")
def display_root_message():
    return{"Message": "Welcome to todo app"}


