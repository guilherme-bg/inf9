from flask import Flask
from config import app_config
from flask_migrate import Migrate
from app.models.models import db, Usuario
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
import os

bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()


config_name = os.environ.get('FLASK_ENV')

def create_app():
    app = Flask('teste')
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login_get'
    from .blueprints.auth import auth
    from .blueprints.home import home
    from .blueprints.usuarios import usuarios
    from .blueprints.livros import livros
    from .blueprints.emprestimos import emprestimos
    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(usuarios)
    app.register_blueprint(livros)
    app.register_blueprint(emprestimos)
    return app

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.filter_by(id=int(user_id)).first()
