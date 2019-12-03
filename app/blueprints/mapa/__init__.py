# app/blueprints/mapa/__init__.py
from flask import Blueprint
mapa = Blueprint ('mapa',__name__)
from . import routes