from passlib.context import CryptContext
from schemas.user_schema import UserInDB, UserSchema
from models.user_models import Users
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse


pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str): # type: ignore

    user = db.query(Users).filter(Users.username == username).first()
    print (">>>>>>>>>>",user)
    
    if user:
        return user
    else: 
        return None

def authenticate_user(db, username:str, password: str):
    user = get_user(db, username= username)
    print("User fetched for authentication>>>>>>>>>>>>", user)
    user = UserInDB.model_validate(user)
    if not  user :
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

print("Hashed",get_password_hash("123456"))

def add_new_user(db, formdata):

    username = formdata.username
    if db.query(Users).filter(Users.username == username).first():
        raise HTTPException(status_code=400, detail= "Username already taken")
    new_user = Users(username = formdata.username,
                         email = formdata.email,
                         full_name = formdata.full_name,
                         hashed_password= get_password_hash(formdata.password))
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        response=  JSONResponse(status_code=status.HTTP_201_CREATED,
                            content={"message":f"{formdata.username} added succesfull"}
        )
        print("Response>>>>>>>>>>>>",response)
        return response
    except Exception as e:
        return JSONResponse( status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"error": str(e)}
        )
