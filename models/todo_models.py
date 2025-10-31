from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, ForeignKey
from database import Base
from datetime import datetime
import enum

from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.user_models import Users


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

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    todo_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    priority: Mapped[PriorityLevel] = mapped_column(Enum(PriorityLevel), default=PriorityLevel.LOW)
    creation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)
    status = Column(Enum(TodoStatus), default=TodoStatus.PENDING)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)

    # Foreignkey linking to link the table rows to the owner

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    owner: Mapped["Users"] = relationship(back_populates="todos")