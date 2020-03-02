import os


class Config:

    # General Config
    SECRET_KEY = os.urandom(32)

    # Database
    # Connect to the database
    connection_string = 'postgresql:///housing'
    SQLALCHEMY_DATABASE_URI = connection_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False
