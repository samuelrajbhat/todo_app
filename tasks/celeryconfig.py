broker_url = 'pyamqp://samuel:123456@172.24.189.86//'
# result_backend = 'rpc://'
result_backend = 'db+postgresql://samuel:123456@localhost/celery_state'



# 172.24.189.86 this is the internal ip of RabbitMQ running in WSL