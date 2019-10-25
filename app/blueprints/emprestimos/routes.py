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

@emprestimos.route('/registraremprestimo', methods=['POST'])
@login_required
def emprestimo_cadastro_post():
    form = FormEmprestimo()
    if form.validate_on_submit():
        try:
            novo_emprestimo= emprestimo(usuario = form.usuario.data, livro = form.livro.data)
            db.session.add(novo_emprestimo)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash('Ferrou!' +str(e), 'danger')
    else:
        flash('Dados invalidos!'+ str(form.errors) , 'danger')
    return redirect('/registrar')