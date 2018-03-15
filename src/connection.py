import pika
from contextlib import contextmanager


@contextmanager
def pika_conn(host, queue):
    '''
    A simple context manager for RabbitMQ connection handling
    '''
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=host))
        channel = connection.channel()
        channel.queue_declare(queue)

        yield channel
    finally:
        connection.close()
