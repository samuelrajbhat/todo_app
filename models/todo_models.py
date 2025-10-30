from sqlalchemy import Column, Integer, String, DateTime, Enum
from database import Base
from datetime import datetime
import enum


# Enum for todo status
class TodoStatus(str, enum.Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


# Enum to set Todo priority (use IntEnum for numeric ordering)
class PriorityLevel(enum.IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Todo_Model(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    todo_name = Column(String(100), nullable=False)
    description = Column(String(250), nullable=True)
    priority = Column(Enum(PriorityLevel), default=PriorityLevel.LOW)
    creation_date = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status = Column(Enum(TodoStatus), default=TodoStatus.PENDING)