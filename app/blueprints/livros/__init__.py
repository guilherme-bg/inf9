# app/blueprints/livros/__init__.py
from flask import Blueprint
livros = Blueprint ('livros',__name__)
from . import routes