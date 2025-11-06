from celery import Celery
import os

# from . import celeryconfig

celery_app = Celery('simple_task')
celery_app.config_from_object('tasks.celeryconfig')

@celery_app.task
def add(x,y):
    print(x+y)
    return x + y


@celery_app.task
def write_notification(todo_title: str, current_user: str,  todo_operation:str):

    file_name = "log.txt"
    mode = "a" if os.path.exists(file_name) else "w"

    with open("log.txt", mode= mode) as notification_file:
        content = f"todo : {todo_title} {todo_operation} by {current_user} \n"
        notification_file.write(content)
