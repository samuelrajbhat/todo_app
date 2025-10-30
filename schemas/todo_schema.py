from pydantic import BaseModel
from  datetime import datetime
from typing import Optional
from models.todo_models import TodoStatus, PriorityLevel


class TodoForm(BaseModel):
    todo_name: str
    description: str | None = None
    priority: Optional[PriorityLevel] = PriorityLevel.LOW  
    status: Optional[TodoStatus] = TodoStatus.PENDING 

