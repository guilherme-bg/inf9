from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import InputRequired,Length,EqualTo

class FormPasso1(FlaskForm):
    livro = RadioField('Sinopse',validators=[InputRequired(), Length(min=20,max=2048)])
    submit = SubmitField('Enviar')

