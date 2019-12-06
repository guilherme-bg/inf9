from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, RadioField
from wtforms.validators import InputRequired,Length,EqualTo

class FormEndereco(FlaskForm):
    endereco = StringField('Endereço', [validators.required()])
    submit = SubmitField('Buscar')