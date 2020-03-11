import os

class Config(object):
    SECRET_KEY = os.urandom(32)
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///housing'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://fjyzwmhqaeuodf:3feca8069b17223256647cd4a51b31156fcd635b57eddbbd7b09e8cd8aa90fd3@ec2-35-168-54-239.compute-1.amazonaws.com:5432/d4i0uocujmq25a'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
