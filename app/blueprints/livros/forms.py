from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired,Length,EqualTo

class FormRegistro(FlaskForm):
    titulo = StringField('Titulo',validators=[InputRequired()])
    autor = StringField('Autor',validators=[InputRequired()])
    isbn = StringField('Isbn',validators=[InputRequired()])
    ano = StringField('Ano',validators=[InputRequired()])
    editora = StringField('Editora',validators=[InputRequired()])
    sinopse = StringField('Sinopse',validators=[InputRequired()])
    submit = SubmitField('Enviar')