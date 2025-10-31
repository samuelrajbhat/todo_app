from pydantic import BaseModel

# User schema for creating and updating user information

class UserSchema(BaseModel):
    id: int
    username: str
    full_name: str
    email: str
    password: str
    is_deleted: bool = False


class UserInDB(UserSchema):
    hashed_password: str
