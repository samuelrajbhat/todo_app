from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def display_root_message():
    return{"Message": "Welcome to todo app"}
