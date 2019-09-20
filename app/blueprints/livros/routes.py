from flask import render_template, flash, redirect
from . import livros
from .forms import FormRegistro
from ... import db
from ...models.models import Livros

@livros.route('/livros')
def lista_livro():
    dados = Livros.query.all()
    print(dados)
    return render_template('livros/livro.tpl', dados=dados)
@livros.route('/livro/<int:id>')
def visualiza_livro(id):
    dados = Livros.query.filter_by(id = id).first()
    return render_template('livros/livro_detalhes.tpl', dado = dados)
@livros.route('/registrarlivro', methods=['GET'])
def registrar_get():
    form = FormRegistro()
    return render_template('livros/registro.tpl', form=form)
@livros.route('/registrarlivro', methods=['POST'])
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