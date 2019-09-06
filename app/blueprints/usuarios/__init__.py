# app/blueprints/usuarios/__init__.py
from flask import Blueprint
usuarios = Blueprint ('usuarios',__name__)
from . import routes