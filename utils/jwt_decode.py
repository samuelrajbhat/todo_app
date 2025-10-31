from jose import jwt, JWTError
from datetime import datetime, timedelta
from core.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM

def create_access_token(data: dict, expires_delta: timedelta or None = None): #type: ignore
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM) # type: ignore
    return encoded_jwt

# verifies the token from client side againt the server token
def verify_token(token: str):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM) # type: ignore
        return payload
    except JWTError:
        return None