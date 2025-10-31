from pydantic import BaseModel


# Token serialization model

class Token(BaseModel):
    access_token: str
    token_type: str

