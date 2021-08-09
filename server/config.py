import os

class Config(object):
    IPSTACK_URL = 'http://api.ipstack.com'
    IPSTACK_KEY = os.environ.get('IPSTACK_KEY') or '0d83726f94cb71cc104eaa6a85f19786'
    DB_USER = 'omerpr23'
    DB_NAME = 'anima'
    DB_PASS = '************'
    DB_URL = 'mongodb+srv://{user}:{password}@cluster0.ixngl.mongodb.net/{dbname}?retryWrites=true&w=majority'.format(user = DB_USER, password= DB_PASS, dbname = DB_NAME)