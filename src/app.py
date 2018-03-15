'''
    magic-cards app

    A simple web service that offer endpoints for moving card data from MySQL
    to a JSON text file.

    Also provides an endpoint to fetch card data by id.
'''
import json
import logging
import os

import pika
from flask import Flask, abort

from connection import pika_conn
from dao import get_cards, read_file
from settings import ALL, MQ_MOVE_QUEUE, MQ_HOST

app = Flask(__name__)
debug = os.getenv('DEBUG', False)
logger = logging.getLogger('app')
logging.basicConfig(level=logging.DEBUG if debug else logging.WARN)


def _publish(channel, message, properties=None):
    '''
    Publishes a single message to given channel
    '''
    logger.debug('Publishing message')
    return channel.basic_publish(
        exchange='',
        routing_key=MQ_MOVE_QUEUE,
        body=message,
        properties=properties)


def _move_cards(card_list):
    '''
    Take a list of cards and publish to RabbitMQ
    '''
    logger.debug('Moving cards')
    found = False
    with pika_conn(MQ_HOST, MQ_MOVE_QUEUE) as channel:
        found = True
        properties = pika.BasicProperties(content_type='application/json')
        _publish(channel, json.dumps(card_list), properties)
    print('Done')
    return found


@app.route('/movecards/<int:expansion_id>', methods=['POST'])
def move_expansion(expansion_id):
    '''
    Endpoint to select which expansion to move
    '''
    if _move_cards(list(get_cards(expansion_id=expansion_id))):
        return 'done', 200
    else:
        abort(404)


@app.route('/moveall', methods=['GET'])
def move_all():
    '''
    Async endpoint moving all cards
    '''
    with pika_conn(MQ_HOST, MQ_MOVE_QUEUE) as channel:
        _publish(channel, ALL)
    return 'ok', 202


@app.route('/card/<card_id>', methods=['GET'])
def get_card(card_id):
    '''
    Endpoint returning a single card
    '''
    try:
        return json.dumps(read_file()[card_id])
    except (KeyError, FileNotFoundError, json.decoder.JSONDecodeError):
        abort(404)


@app.route('/')
def index():
    abort(403)


if __name__ == '__main__':
    app.run(debug=debug, host=os.getenv('HOST', '0.0.0.0'))
