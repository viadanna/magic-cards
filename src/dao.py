'''
    magic-cards dao

    Utility functions to help deal with querying SQL and dealing with text files.
'''
import MySQLdb
import json

from settings import FIELDS, DB_HOST, DB_NAME, DB_PASSWD, DB_TABLE, DB_USER, TXT_FILE


def _get_db():
    ''' Get a connection with the database '''
    return MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME)


def get_cards(expansion_id=None):
    '''
    Generator returning single cards for queried expansion or
    all cards if no expansion was informed.
    '''
    cursor = _get_db().cursor()
    sql = 'SELECT * from {}'.format(DB_TABLE)
    if expansion_id:
        sql = '{} WHERE ExpansionId = {};'.format(sql, expansion_id)
    else:
        sql += ';'
    cursor.execute(sql)
    while True:
        row = cursor.fetchone()
        if row:
            d = dict(zip(FIELDS, row))
            yield d
        else:
            cursor.close()
            break


def write_file(content, filename=TXT_FILE):
    '''
    Store given object in text file
    '''
    with open(filename, 'w') as f:
        json.dump(content, f)


def read_file(filename=TXT_FILE):
    '''
    Read JSON text file as object
    '''
    with open(filename, 'r') as f:
        return json.load(f)
