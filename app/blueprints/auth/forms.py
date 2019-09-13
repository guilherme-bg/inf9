from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired,Email,Length,EqualTo

class FormRegistro(FlaskForm):
    nome = StringField('Nome',validators=[InputRequired()])
    email = StringField('Email',validators=[InputRequired(),Email(message='Email inválido!')])
    password = PasswordField('Senha',validators=[InputRequired(),Length(min=8)])
    password2 = PasswordField('Confirme a senha',validators=[InputRequired(),EqualTo('password')])
    submit = SubmitField('Enviar')

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Email(message='Email inválido!')])
    password = PasswordField('Senha',validators=[InputRequired(),Length(min=8)])
    submit = SubmitField('Log in')

