# User models for the user table used for authentication and authorization
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from models.todo_models import Todo_Model


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True)
    full_name = Column(String(100))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_deleted = Column(Boolean, default=False)

# Foreignkey relationship to link users to their todos
    todos: Mapped[List["Todo_Model"]] = relationship("Todo_Model", back_populates="owner")