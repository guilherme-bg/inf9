from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from passlib.hash import argon2
from flask_login import UserMixin

db=SQLAlchemy()

def hash_my_password(p):
    return argon2.hash(p)

def check_my_password(u, p):
    return argon2.verify(p, u.password_hash)

class Usuario(db.Model, UserMixin):
    id= db.Column(db.Integer(), primary_key=True)
    nome= db.Column(db.String(100))
    email= db.Column(db.String(100))
    password_hash=db.Column(db.String(80))
    def __init__(self,password, email, nome):
        self.nome = nome
        self.email = email
        self.password_hash = hash_my_password(password)

class Livros(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    titulo= db.Column(db.String(100))
    autor= db.Column(db.String(100))
    isbn= db.Column(db.String(100))
    ano= db.Column(db.String(4))
    editora= db.Column(db.String(100))
    sinopse= db.Column(db.String(500))
    situacao= db.column(db.Boolean)    
    def __init__(self,titulo, autor, isbn, ano, editora, sinopse, situacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano
        self.editora = editora
        self.sinopse = sinopse
        self.situacao = situacao

class Emprestimo(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    idUsuario= db.Column(db.Integer(), ForeignKey("usuario.id"))
    idLivro= db.Column(db.Integer(), ForeignKey("livros.id"))
    dataEmprestimo= db.Column(db.DateTime())
    dataPrevista= db.Column(db.DateTime())
    dataEfetiva= db.Column(db.DateTime())
    def __init__(self, idUsuario, idLivro, dataEmprestimo, dataPrevista, dataEfetiva):
        self.idUsuario = idUsuario
        self.idLivro = idLivro
        self.dataEmprestimo = dataEmprestimo
        self.dataPrevista = dataPrevista
        self.dataEfetiva = dataEfetiva
