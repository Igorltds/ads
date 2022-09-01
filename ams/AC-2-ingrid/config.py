import os


class BaseConfig(object):
    SECRET_KEY = '\x8d\xae\xae\xdfU\xa63\xd1\xaf9\x04Ewp\xdd\xe7\x15\xd0\xc3\xfa\xc8\xf6\xd2\x1c'
    DEBUG = True
    DB_NAME = 'sis_web'
    DB_USER = 'sis_web'
    DB_PASS = '123'
    DB_SERVICE = '172.17.0.2'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
