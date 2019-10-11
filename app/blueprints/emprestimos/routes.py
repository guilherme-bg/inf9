from flask import render_template, flash, redirect, request
from .forms import FormEmprestimo
from . import emprestimos
from ... import db
from ...models.models import Livros, Usuario, emprestimo
from flask_login import login_required, login_user, logout_user

@emprestimos.route('/registraremprestimo', methods=['GET'])
@login_required
def emprestimo_cadastro_get():
    form = FormEmprestimo()
    return render_template('emprestimos/registro.tpl', form=form)