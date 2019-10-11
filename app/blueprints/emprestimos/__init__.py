# app/blueprints/emprestimos/__init__.py
from flask import Blueprint
emprestimos = Blueprint ('emprestimos',__name__)
from . import routes