from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
from database import engine, Base
from models import todo_models

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")

def display_root_message():
    return{"Message": "Welcome to todo app"}

@app.get("/home")
def display_home_message(db: Session = Depends(get_db)):
    return {"Message": "Welcome to the home page"}