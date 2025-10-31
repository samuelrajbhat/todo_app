from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from models.token_model import Token
from auth.user_auth_schema import UserForm
from auth.password_hashing import authenticate_user, add_new_user
from utils.jwt_decode import create_access_token
# from schemas.user_schemas import UserClass
from database import get_db
from sqlalchemy.orm import Session
from typing import Annotated



router = APIRouter()


@router.post("/signup")
async def signup(formdata: Annotated[UserForm, Depends(UserForm.as_form)], db: Session = Depends(get_db)):
# async def signup(formdata: UserForm, db: Session = Depends(get_db)):

    print("jnskfsdf>>>>>>>>>>>>>>>>>>>>",formdata)
    add_new_user(db,formdata)
    

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}