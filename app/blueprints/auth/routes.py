from flask import render_template, flash, redirect
from . import auth
from .forms import FormRegistro, FormLogin
from ... import db
from ...models.models import Usuario, check_my_password
from flask_login import login_required, login_user, logout_user

@auth.route('/registrar', methods=['GET'])
def registrar_get():
    form = FormRegistro()
    return render_template('auth/registro.tpl', form=form)

@auth.route('/registrar', methods=['POST'])
def registrar_post():
    form = FormRegistro()
    if form.validate_on_submit():
        try:
            novo_usuario=Usuario( nome = form.nome.data,
                                  email = form.email.data,
                                  password = form.password.data)
            db.session.add(novo_usuario)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash('Ferrou!' +str(e), 'danger')
    else:
        flash('Dados invalidos!'+ str(form.errors) , 'danger')
    return redirect('/registrar')

@auth.route('/login', methods=['GET'])
def login_get():
    form = FormLogin()
    return render_template('auth/login.tpl', form = form)

@auth.route('/login', methods=['POST'])
def login_post():
    form = FormLogin()
    if form.validate_on_submit():
        try:
            usuario = Usuario.query.filter_by(email = form.email.data).first()
            if usuario is not None and check_my_password(usuario, form.password.data):
                login_user(usuario)
                flash('Beleza', 'Success')
                return redirect('/')
            else:
                flash('Dados invalidos!', 'danger')
                return redirect('/login')
        except Exception as e:
            flash('Dados inválidos!2'+str(e),'danger')
    else:
        flash('Dados invalidos' + str(form.errors), 'danger')
        return redirect('/login')

@auth.route('/logout', methods = ['GET'])
def logout():
    logout.user()
    flash('obrigado por usar o app.', 'success')
    return redirect('login')
