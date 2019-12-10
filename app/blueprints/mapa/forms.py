from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, RadioField
from wtforms.validators import InputRequired,Email,Length,EqualTo

class FormEndereco(FlaskForm):
    endereco = StringField('Endereço', validators=[InputRequired()])
    submit = SubmitField('Buscar')