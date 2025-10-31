# User models for the user table used for authentication and authorization
from sqlalchemy import Column, Integer, String, Boolean

from database import Base



class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True)
    full_name = Column(String(100))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_deleted = Column(Boolean, default=False)
