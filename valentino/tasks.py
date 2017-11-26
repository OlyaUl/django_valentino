from celery import Celery
from celery.task import Task

from valentino.models import Product

app = Celery(broker='amqp://')

HOST = 'localhost'
DB_NAME = 'val'
DB_USER = 'postgres'
DB_PASS = '1'


@app.task(name="save")
def save(item):
    '''f = open('test.txt', 'w')
    f.write(str(item))'''
    Product.objects.get_or_create(
        name=item.get('name'),
        model=item.get('model'),
        category=item.get('category'),
        description=item.get('description'),
        url=item.get('url'),
        image=item.get('image'),
        site=item.get('site'),
        date=item.get('date'),
        currency=item.get('currency'),
        price=item.get('price'),
        size=item.get('size'),
        # sale_price=item.get('sale_price') or "",

    )


if __name__ == '__main__':
    app.worker_main()
