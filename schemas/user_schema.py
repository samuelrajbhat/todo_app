from pydantic import BaseModel

# User schema for creating and updating user information

class UserSchema(BaseModel):
    id: int
    username: str
    full_name: str
    email: str
    is_deleted: bool
    model_config = {
        "from_attributes": True 
        # To allow instantiating this pydantic model from SQLAlchemy objects (or any other  attributes) using model_validate()

    }
    

class UserInDB(UserSchema):
    hashed_password: str
    model_config = {
        "from_attributes": True 
        # To allow instantiating this pydantic model from SQLAlchemy objects (or any other  attributes) using model_validate()

    }
    

class Access_token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username : str or None = None # type: ignore