
import os
# Background task to handle long-running operations

def check_file_exist(file_name: str) -> bool:
    return os.path.exists(file_name)
    
def write_notification(todo_title: str, current_user: str,  todo_operation:str):

    file_name = "log.txt"
    mode = "a" if os.path.exists(file_name) else "w"

    with open("log.txt", mode= mode) as notification_file:
        content = f"todo : {todo_title} {todo_operation} by {current_user} \n"
        notification_file.write(content)



