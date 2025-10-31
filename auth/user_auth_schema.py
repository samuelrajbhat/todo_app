from pydantic import BaseModel
from typing import Annotated
from fastapi import Form


class UserForm(BaseModel):
    full_name: str
    username: str
    password: str
    email: str
    
    @classmethod
    def as_form(
        cls,
        full_name: Annotated[str, Form()],
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
        email: Annotated[str, Form()],
    ) -> "UserForm":
        return cls(
            full_name=full_name,
            username=username,
            password=password,
            email=email
        )