
# Background task to handle long-running operations

def write_notification(todo_message: str, ):
    with open("log.txt", mode= "w") as notification_file:
        content = f"todo created: {todo_message} "
        notification_file.write(content)

