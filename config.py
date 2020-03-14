import os

class Config(object):
    SECRET_KEY = os.urandom(32)
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///housing'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''

    def __init__(self, database_url):
        self.SQLALCHEMY_DATABASE_URI = database_url

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql:///housing_test'
    TESTING = True
