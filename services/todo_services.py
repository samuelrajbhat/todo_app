from fastapi import status, HTTPException

from models.todo_models import Todo_Model
from datetime import datetime


def add_new_todo(todo_data, db, current_user):
    new_todo= Todo_Model(
        todo_name= todo_data.todo_name,
        description= todo_data.description,
        priority= todo_data.priority,
        status= todo_data.status,
        current_user=current_user.id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def list_all_todos(db, current_user):
    list_of_all_todos = db.query(Todo_Model).filter(Todo_Model.is_deleted == False,
                                                    Todo_Model.owner_id == current_user.id).all()
    return list_of_all_todos

def soft_delete_todo(todo_id: int, db, current_user):
    todo = db.query(Todo_Model).filter(Todo_Model.id == todo_id, Todo_Model.is_deleted == False, Todo_Model.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.is_deleted = True
    todo.deleted_at = datetime.now()
    db.commit()

def update_todo_status(todo_id: int, todo_data, db, current_user):
    todo_update = db.query(Todo_Model).filter(Todo_Model.id == todo_id, Todo_Model.is_deleted == False, Todo_Model.owner_id == current_user.id).first()
    if not todo_update:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_update.status = todo_data.status
    db.commit()
    db.refresh(todo_update)
    return todo_update
