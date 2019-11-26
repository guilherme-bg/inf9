from flask import render_template, flash, redirect, request, Flask, url_for
from .forms import FormEmprestimo
from . import emprestimos
from ... import db, mail
from ...models.models import Livros, Usuario, emprestimo
from flask_login import login_required, login_user, logout_user
from datetime import datetime
from sqlalchemy import text
from string import Template
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap

def envia_email(_email_):
    msg = Message(subject="[inf9] Email de emprestimo",
                      sender='patinhas.douradas.adocoes@gmail.com',
                      recipients=_email_, 
                      body='Você registrou um empréstimo!!!' )
    print(_email_, type(_email_))
    try:
        mail.send(msg)
        flash('Enviou!', 'success')
        return True
    except Exception as e:
        flash('Não enviou' + str(e), 'danger')
        return False
    

@emprestimos.route('/registraremprestimo', methods=['GET'])
@login_required
def emprestimo_cadastro_get():
    form = FormEmprestimo()
    return render_template('emprestimos/registro.tpl', form=form)

@emprestimos.route('/registraremprestimo', methods=['POST'])
@login_required
def emprestimo_cadastro_post():
    try:
        U = request.form.get('usuario')
        L = request.form.get('livro')	
        usuario = Usuario.query.filter_by(id=U).first()
        livro   = Livros.query.filter_by(id=L).first()
        print(usuario.email)
        ok = envia_email([usuario.email])
        if(ok):
            livro.emprestado.append(usuario)
            livro.status = 1        
            db.session.add(livro)
            db.session.commit()
        return redirect(url_for('emprestimos.emprestimo_cadastro_get'))        
        flash('Emprestado para o usuario [{}] o livro [{}] do autor [{}].'.format(usuario.nome,livro.titulo,livro.autor),'success')
    except Exception as e:
        flash('NÃO emprestado para o usuario {} o livro {} do autor {}.'.format(usuario.nome,livro.titulo,livro.autor), 'danger')
    return redirect(url_for('emprestimos.emprestimo_livros'))


@emprestimos.route('/emprestimos')
@login_required
def emprestimo_lista():
    dados = Livros.query.all()
    my_sql = Template("""SELECT uid, lid from emprestimos
                """)
    sql_raw = my_sql.safe_substitute(uid=id_usuario,lid=id_livro)
    sql = text(sql_raw)
    result = db.engine.execute(sql)
    resultados = [row for row in result]
    return render_template('emprestimos/emprestimos.tpl', resultados = resultados)

@emprestimos.route('/livrosemprestimos')
@login_required
def emprestimo_livros():
    dados = Livros.query.all()
    return render_template('emprestimos/livro.tpl', dados = dados)

@emprestimos.route('/devolveremprestimo/<int:_id_>', methods=['GET'])
@login_required
def devolucao_emprestimo(_id_):
    livro = Livros.query.filter_by(id = _id_).first()
    date_time =  datetime.now()
    data_devol = date_time.strftime("%Y-%m-%d")
    my_sql = Template("""UPDATE emprestimos 
                    SET data_devolucao = '$data'
                    WHERE id_livro = '$lid'
                """)
    sql_raw = my_sql.safe_substitute(data = data_devol, lid = _id_)
    sql = text(sql_raw)
    result = db.engine.execute(sql)
    livro.status = 0
    db.session.commit()
    return redirect(url_for('emprestimos.emprestimo_livros'))





