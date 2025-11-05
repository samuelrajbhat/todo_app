from celery import Celery

# from . import celeryconfig

celery_app = Celery('simple_task')
celery_app.config_from_object('tasks.celeryconfig')

@celery_app.task
def add(x,y):
    print(x+y)
    return x + y