from flask import Flask
from config import app_config
import os

config_name = os.environ.get('FLASK_ENV')

def create_app():
    app = Flask('teste')
    app.config.from_object(app_config[config_name])
    from .blueprints.home import home
    app.register_blueprint(home)
    return app
