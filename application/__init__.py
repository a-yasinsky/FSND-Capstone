import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import *

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    env = os.environ.get('__ENV__', '')
    if env == 'production':
        database_url = os.environ.get('DATABASE_URL', '')
        config = ProductionConfig(database_url)
    elif env == 'testing':
        config = TestingConfig()
    else:
        config = DevelopmentConfig()
        app.config.from_object(config)
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    with app.app_context():
        # Include our Routes
        from . import routes
        return app
