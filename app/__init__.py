from flask import Flask
from config import app_config
from flask_migrate import Migrate
from app.models.models import db
import os

migrate = Migrate()

config_name = os.environ.get('FLASK_ENV')

def create_app():
    app = Flask('teste')
    app.config.from_object(app_config[config_name])
    from .blueprints.home import home
    app.register_blueprint(home)
    db.init_app(app)
    migrate.init_app(app, db)
    return app
