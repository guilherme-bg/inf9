from flask_sqlalchemy import SQLAlchemy
from passlib.hash import argon2
from flask_login import UserMixin

db=SQLAlchemy()

def hash_my_password(p):
    return argon2.hash(p)

def check_my_password(u, p):
    return argon2.verify(p, u.password_hash)

class Usuario(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    nome= db.Column(db.String(100))
    email= db.Column(db.String(100))
    password_hash=db.Column(db.String(80))
    def __init__(self,password, email, nome):
        self.nome = nome
        self.email = email
        self.password_hash = hash_my_password(password)
