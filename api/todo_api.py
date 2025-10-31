from fastapi import APIRouter, Depends

from services.todo_services import add_new_todo, list_all_todos, soft_delete_todo, update_todo_status
from schemas.todo_schema import TodoForm, TodoStatusUpdateForm
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/api")

@router.get("/todos")
def list_all_todo_items(db:Session = Depends(get_db)):
    todos = list_all_todos(db)
    return{"todos": todos}

@router.post("/todos")
def add_todo_item(todo_data:TodoForm, db: Session = Depends(get_db)):
    todo = add_new_todo(todo_data, db)
    return{"message": f"{todo}"}

@router.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    todo = soft_delete_todo(todo_id, db)
    return {"message": f"Todo item with id {todo} deleted successfully"}

@router.put("/todos/{todo_id}/status")
def update_todo(todo_id: int, todo_data: TodoStatusUpdateForm, db: Session = Depends(get_db)):
    todo_update= update_todo_status(todo_id, todo_data, db)
    return {"message": f"Todo item with id {todo_id} status updated successfully"} 
