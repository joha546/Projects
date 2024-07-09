from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, 
                template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
                static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'static')))
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

# Import models here to ensure they are registered with SQLAlchemy
from .auth import models