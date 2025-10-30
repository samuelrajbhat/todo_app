from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
from database import engine, Base
from models import todo_models
from schemas.todo_schema import TodoForm
from services.todo_services import add_new_todo, list_all_todos, soft_delete_todo
app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")

def display_root_message():
    return{"Message": "Welcome to todo app"}

@app.get("/home")
def display_home_message(db: Session = Depends(get_db)):
    return {"Message": "Welcome to the home page"}

@app.get("/todos")
def list_all_todo_items(db:Session = Depends(get_db)):
    todos = list_all_todos(db)
    return{"todos": todos}

@app.post("/todos/")
def add_todo_item(todo_data:TodoForm, db: Session = Depends(get_db)):
    todo = add_new_todo(todo_data, db)
    return{"message": f"{todo}"}

@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    todo = soft_delete_todo(todo_id, db)
    return {"message": f"Todo item with id {todo} deleted successfully"}