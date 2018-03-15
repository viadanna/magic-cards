'''
    magic-cards consumer

    A RabbitMQ consumer that saves data to JSON.
'''
import json
import logging
import os
from threading import Lock

from connection import pika_conn
from dao import get_cards, read_file, write_file
from settings import ALL, MQ_HOST, MQ_MOVE_QUEUE

cache = {}
lock = Lock()

debug = os.getenv('DEBUG', False)
logger = logging.getLogger('consumer')
logging.basicConfig(level=logging.DEBUG if debug else logging.WARN)


def on_message(ch, method, properties, body):
    '''
    Parse messages received by RabbitMQ
    '''
    logger.debug('Message received')
    try:
        message = body.decode('utf-8')
        if message == ALL:
            global cache
            cache = {card['GathererId']: card for card in get_cards()}
        else:
            data = json.loads(message)
            for card in data:
                cache[card['GathererId']] = card
    except Exception as e:
        logger.exception(e)
    else:
        with lock:
            write_file(cache)
            logger.warn('Text file updated')


def start():
    '''
    Setup RabbitMQ queue binding
    '''
    logger.info('Starting consumer')

    try:
        global cache
        cache = read_file()
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

    with pika_conn(MQ_HOST, MQ_MOVE_QUEUE) as channel:
        channel.basic_consume(
            on_message,
            queue=MQ_MOVE_QUEUE,
            no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()


if __name__ == '__main__':
    start()
