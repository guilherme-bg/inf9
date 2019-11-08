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
    try:
        U = request.form.get('usuario')
        L = request.form.get('livro')
        usuario = Usuario.query.filter_by(id=U).first()
        livro   = Livros.query.filter_by(id=L).first()
        livro.emprestado.append(usuario)
        livro.status = 1
        db.session.add(livro)
        db.session.commit()
        flash('Emprestado para o usuario [{}] o livro [{}] do autor [{}].'.format(usuario.nome,livro.titulo,livro.autor),'success')
    except Exception as e:
        flash('NÃO emprestado para o usuario {} o livro {} do autor {}.'.format(usuario.nome,livro.titulo,livro.autor), 'danger')
    return redirect(url_for('emprestimo_lista'))

@emprestimos.route('/emprestimos')
@login_required
def emprestimo_lista():
    dados = Livros.query.all()
    my_sql = Template("""SELECT  blablabla

                """)

        sql_raw = my_sql.safe_substitute(uid=usuario_id,lid=livro_id)
        sql = text(sql_raw)
        result = db.engine.execute(sql)
        resultados = [row for row in result]

    print(dados)
    return render_template('emprestimos/emprestimos.tpl', dados=dados, dados_emprestimo = dados_emprestimo)


