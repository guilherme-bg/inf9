from flask import render_template
from . import usuarios
from ...models.models import Usuario

@usuarios.route('/usuarios')
def lista_usuario():
    dados = Usuario.query.all()
    print(dados)
    return render_template('usuarios/usuario.tpl', dados=dados)
@usuarios.route('/usuario/<int:id>')
def visualiza_usuario(id):
    dados = Usuario.query.filter_by(id = id).first()
    return render_template('usuarios/usuario_detalhes.tpl', dado = dados)
@usuarios.route('/usuario/inserir)
def registra_usuario():
    