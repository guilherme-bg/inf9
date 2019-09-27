from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import InputRequired,Length,EqualTo

class FormRegistro(FlaskForm):
    titulo = StringField('Titulo',validators=[InputRequired()])
    autor = StringField('Autor',validators=[InputRequired(), Length(min=3)])
    isbn = StringField('Isbn',validators=[InputRequired(), Length(min=6)])
    ano = StringField('Ano',validators=[InputRequired()])
    editora = StringField('Editora',validators=[InputRequired(), Length(min=6)])
    sinopse = StringField('Sinopse',validators=[InputRequired(), Length(min=20,max=2048)])
    submit = SubmitField('Enviar')

class FormEditar(FormRegistro):
    id = HiddenField()

class FormDeletar(FlaskForm):
    id = HiddenField()
    submit = SubmitField('Deletar')