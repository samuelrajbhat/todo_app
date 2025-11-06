from fastapi import status, HTTPException

from models.todo_models import Todo_Model
from datetime import datetime

from tasks.task import write_notification

def add_new_todo(todo_data, db, current_user):
    new_todo= Todo_Model(
        todo_name= todo_data.todo_name,
        description= todo_data.description,
        priority= todo_data.priority,
        status= todo_data.status,
        owner_id=current_user.id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    notification_task = write_notification.delay(new_todo.todo_name, current_user.username, todo_operation = "created")
    
    return {"created_todo": new_todo, "task_id": notification_task.id}

def list_all_todos(db, current_user):
    list_of_all_todos = db.query(Todo_Model).filter(Todo_Model.is_deleted == False,
                                                    Todo_Model.owner_id == current_user.id).all()
    return list_of_all_todos

def soft_delete_todo(todo_id: int, db, current_user):
    todo = db.query(Todo_Model).filter(Todo_Model.id == todo_id, Todo_Model.is_deleted == False, Todo_Model.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_name = todo.todo_name
    todo.is_deleted = True
    todo.deleted_at = datetime.now()
    db.commit()
    notification_task = write_notification.delay(todo_name, current_user.username, todo_operation = "deleted")
    return {"deleted_todo_id": todo_id, "task_id": notification_task.id}

def update_todo_status(todo_id: int, todo_data, db, current_user):
    todo_update = db.query(Todo_Model).filter(Todo_Model.id == todo_id, Todo_Model.is_deleted == False, Todo_Model.owner_id == current_user.id).first()
    if not todo_update:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_update.status = todo_data.status
    db.commit()
    db.refresh(todo_update)
    notification_task = write_notification.delay(todo_update.todo_name, current_user.username, todo_operation = "updated")

    return {"updated_todo": todo_update, "task_id": notification_task.id}
