from db import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True)
    senha = db.Column(db.String())
    acertos_portugues = db.Column(db.Integer, default=0)
    acertos_matematica = db.Column(db.Integer, default=0)

