from celery import Celery
from celery.task import Task

app = Celery(broker='amqp://')


HOST = 'localhost'
DB_NAME = 'val'
DB_USER = 'postgres'
DB_PASS = '1'


@app.task(name="save")
def save(item):
    f = open('test.txt', 'w')
    f.write(str(item))


if __name__ == '__main__':
    app.worker_main()