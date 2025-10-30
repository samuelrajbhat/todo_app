from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from datetime import datetime


class Todo_Model(BaseModel):
    __tablename__= "todos"

id = Column(Integer, PrimaryKey= True, index=True)
todo_name = Column(String(100), nullable=False)
description = Column(String(250), nullable=True)
priority = Column(Integer, default=3)
creation_date = Column(DateTime, default=datetime.now)
updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
