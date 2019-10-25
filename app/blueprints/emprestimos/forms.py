from flask_wtf import FlaskForm
from ...models.models import Livros, Usuario
from wtforms import StringField, SubmitField, HiddenField, RadioField
from wtforms.validators import InputRequired,Length,EqualTo

class FormEmprestimo(FlaskForm):
    livro = RadioField('Livro', choices=None,coerce=int, validators=[InputRequired()])
    usuario = RadioField('Usuário', choices=None,coerce=int, validators=[InputRequired()])
    def __init__(self, *args, **kwargs):
        super(FormEmprestimo, self).__init__(*args, **kwargs)
        self.usuarios = Usuario.query.order_by('nome').all()
        self.usuario.choices = [(usr.id,usr.nome) for usr in self.usuarios]
        self.livros = Livros.query.order_by('titulo').all()
        self.livro.choices = [(lvr.id,lvr.titulo) for lvr in self.livros]
	