from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime, timedelta
from passlib.hash import argon2
from flask_login import UserMixin

db=SQLAlchemy()

def hash_my_password(p):
    return argon2.hash(p)

def check_my_password(u, p):
    return argon2.verify(p, u.password_hash)

PERIODO_EMPRESTIMO     = timedelta(days=7)
DATA_ESTIMADA          = datetime.now()+PERIODO_EMPRESTIMO

emprestimo = db.Table('emprestimos',
                        db.Column('id',db.Integer,primary_key=True),
                        db.Column('id_livro',db.Integer,db.ForeignKey('livros.id')),
                        db.Column('id_usuario',db.Integer,db.ForeignKey('usuario.id')),
                        db.Column('data_emprestimo',db.DateTime(),default=datetime.now()),
                        db.Column('data_estimada',db.DateTime(),default=DATA_ESTIMADA),
                        db.Column('data_devolucao',db.DateTime())
                        )


class Usuario(db.Model, UserMixin):
    id= db.Column(db.Integer(), primary_key=True)
    nome= db.Column(db.String(100))
    email= db.Column(db.String(100))
    password_hash=db.Column(db.String(80))
    livro = db.relationship('Livros',secondary=emprestimo, backref=db.backref('emprestado', lazy='dynamic')) #backref
    #usuario = db.relationship('Livro', secondary=emprestimo, backref=db.backref('emprestado', lazy='dynamic'))
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
    status = db.Column(db.Integer,default=0) # 0=livre, 1=emprestado
    #usuario = db.relationship('Usuario',secondary=emprestimo) #backref
    def __init__(self,titulo, autor, isbn, ano, editora, sinopse, situacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano
        self.editora = editora
        self.sinopse = sinopse
        self.situacao = situacao

# Relação Muitos-para-Muitos (ou Many-to-Many)

"""
class Emprestimo(db.Model):
    __tablename__='emprestimos'
    id = db.Column(db.Integer, primary_key=True)
    id_livro
    id_usuario
"""    
 



