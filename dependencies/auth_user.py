from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.config import settings
from jose import JWTError, jwt
from schemas.user_schema import TokenData, UserSchema, UserInDB
from auth.password_hashing import get_user
from sqlalchemy.orm import Session
from database import get_db

from utils.jwt_decode import verify_token

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth_2_scheme), db: Session= Depends(get_db)):
    credential_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)

    try:
        payload = verify_token(token)
        username: str = payload.get("sub") #type: ignore
        if username is None: 
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    user = get_user(db, token_data.username)
    
    #  user = get_user(UserClass, token_data) # type: ignore
    if user is None: 
        raise credential_exception
    if user:
        user = UserSchema.model_validate(user)
    return user

async def get_current_active_user(current_user: UserSchema= Depends(get_current_user)):
    if current_user.is_deleted: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Inactive User")
    return current_user
