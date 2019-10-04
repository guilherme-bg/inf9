from flask import render_template, flash, redirect, request
from . import livros
from .forms import FormRegistro, FormEditar, FormDeletar
from ... import db
from ...models.models import Livros
from flask_login import login_required, login_user, logout_user

@emprestimo.route('/emprestimo', methods=['GET'])
@login.required
def passo_1():
    