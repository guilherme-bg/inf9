from flask_wtf import FlaskForm
from ...models.models import Livros, Usuario
from wtforms import StringField, SubmitField, HiddenField, RadioField
from wtforms.validators import InputRequired,Length,EqualTo

class FormEmprestimo(FlaskForm):
    livro = RadioField('Livro', choices='' , validators=[InputRequired()])
    usuario = RadioField('Usuário', choices='', validators=[InputRequired()])
    submit = SubmitField('Enviar')
    def __init__(self, *args, **kwargs):
        super()
        livros = Livros.query.all()
        usuarios = Usuario.query.all()
        self.usuario.choices = [(user.id, user.nome) for user in usuarios]
        self.livro.choices = [(livro.id, livro.titulo) for livro in livros]
