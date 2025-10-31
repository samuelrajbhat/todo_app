from fastapi import APIRouter, Depends, Security

from services.todo_services import add_new_todo, list_all_todos, soft_delete_todo, update_todo_status
from schemas.todo_schema import TodoForm, TodoStatusUpdateForm
from sqlalchemy.orm import Session
from database import get_db
from dependencies.auth_user import get_current_active_user 
from models.user_models import Users

protected_router = APIRouter(prefix="/api",
                   dependencies=[Security(get_current_active_user)])

@protected_router.get("/home")
def display_home_message(db: Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    
    return {"Message": "Welcome to the home page", "user": current_user.username}



@protected_router.get("/todos")
def list_all_todo_items(db:Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    todos = list_all_todos(db, current_user)
    return{"todos": todos}

@protected_router.post("/todos")
def add_todo_item(todo_data:TodoForm, db: Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    print(">>>>>>>", current_user)
    todo = add_new_todo(todo_data, db, current_user)
    return{"message": f"{todo}"}

@protected_router.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    todo = soft_delete_todo(todo_id, db, current_user)
    return {"message": f"Todo item with id {todo} deleted successfully"}

@protected_router.put("/todos/{todo_id}/status")
def update_todo(todo_id: int, todo_data: TodoStatusUpdateForm, db: Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    todo_update= update_todo_status(todo_id, todo_data, db, current_user)
    return {"message": f"Todo item with id {todo_id} status updated successfully"} 
