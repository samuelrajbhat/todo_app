from fastapi import status, HTTPException

from models.todo_models import Todo_Model


def add_new_todo(todo_data, db):
    new_todo= Todo_Model(
        todo_name= todo_data.todo_name,
        description= todo_data.description,
        priority= todo_data.priority,
        status= todo_data.status
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
