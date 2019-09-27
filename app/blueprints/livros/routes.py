from flask import render_template, flash, redirect, request
from . import livros
from .forms import FormRegistro, FormEditar, FormDeletar
from ... import db
from ...models.models import Livros
from flask_login import login_required, login_user, logout_user

@livros.route('/livros')
@login_required
def lista_livro():
    dados = Livros.query.all()
    print(dados)
    return render_template('livros/livro.tpl', dados=dados)

@livros.route('/livro/<int:id>')
@login_required
def visualiza_livro(id):
    dados = Livros.query.filter_by(id = id).first()
    return render_template('livros/livro_detalhes.tpl', dado = dados)

@livros.route('/registrarlivro', methods=['GET'])
@login_required
def registrar_get():
    form = FormRegistro()
    return render_template('livros/registro.tpl', form=form)

@livros.route('/registrarlivro', methods=['POST'])
@login_required
def registrar_post():
    form = FormRegistro()
    if form.validate_on_submit():
        try:
            novo_livro=Livros( titulo = form.titulo.data,
                                  autor = form.autor.data,
                                  isbn = form.isbn.data,
                                  ano = form.ano.data,
                                  editora = form.editora.data,
                                  sinopse = form.sinopse.data)
            db.session.add(novo_livro)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash('Ferrou!' +str(e), 'danger')
    else:
        flash('Dados invalidos!'+ str(form.errors) , 'danger')
    return redirect('/registrar')

@livros.route('/livros/editar/<int:_id_>', methods=['GET'])
@login_required
def edit_livro_get(_id_):
    livro = Livros.query.filter_by(id=_id_).first()
    print(livro)
    form = FormEditar(obj=livro)
    return render_template('livros/livro_editar.tpl', form=form)

@livros.route('/livros/editar/<int:_id_>',methods=['POST'])
@login_required
def edit_livro_post(_id_):
    form = FormEditar(request.form)
    if form.validate_on_submit():
        print(form.id, form.titulo)
        u = Livros.query.filter_by(id=form.id.data).first()
        form.populate_obj(u)
        db.session.commit()
        flash('Livro alterado com sucesso.','success')
    else :
        flash('Não alterado. Problemas nos dados.'+str(form.errors),'danger')
    return redirect('/livros')

@livros.route('/livros/excluir/<int:_id_>',methods=['GET'])
@login_required
def del_livro_get(_id_):
    livro = Livros.query.filter_by(id = _id_).first()
    form = FormDeletar(obj=livro)
    return render_template('livros/livro_deletar.tpl', form  = form, dado = livro)

@livros.route('/livros/excluir/<int:_id_>',methods=['POST'])
@login_required
def del_livro_post(_id_):
    form = FormDeletar(request.form)
    flash('Tem certeza que quer deletar este livro?.', 'danger')
    if form.validate_on_submit():
        u = Livros.query.filter_by(id=form.id.data).first()
        db.session.delete(u)
        db.session.commit()
        flash('Livro deletado com sucesso.', 'success')
    else :
        flash('Falha ao deletar livro.','danger')
    return redirect('/livros')
