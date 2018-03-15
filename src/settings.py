'''
    magic-cards settings

    Constants to configure RabbitMQ and MySQL connections along other information.
'''
# Database
# DB_HOST = '127.0.0.1'  # for unittest
DB_HOST = 'tcgplace-cards-db'
DB_PASSWD = 'root'
DB_USER = 'root'
DB_NAME = 'tcgplace'
DB_TABLE = 'magiccard'

# RabbitMQ
# MQ_HOST = '127.0.0.1'  # for unittest
MQ_HOST = 'rabbitmq'
MQ_MOVE_QUEUE = 'moving_cards'

# Constants
ALL = 'all'
TXT_FILE = '/tmp/cards_db.txt'

FIELDS = [
    'GathererId',
    'Variation',
    'SearchName',
    'PtBRSearchName',
    'EnglishName',
    'PtBRName',
    'LinkName',
    'Color',
    'ManaCost',
    'CollectionNumber',
    'ConvertedManaCost',
    'Rarity',
    'Rules',
    'FlavorText',
    'SuperTypes',
    'CardTypes',
    'UnseriousSubTypes',
    'Power',
    'Toughness',
    'Loyalty',
    'ExpansionId',
    'ArtistId',
    'FlipName',
    'FlipRules',
    'FlipSuperTypes',
    'FlipTypes',
    'FlipPower',
    'FlipToughness',
    'FlipGathererId',
    'SplitManaCost',
    'SplitConvertedManaCost']
