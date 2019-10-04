# app/blueprints/emprestimo/__init__.py
from flask import Blueprint
emprestimo = Blueprint ('emprestimo',__name__)
from . import routes