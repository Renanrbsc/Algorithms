import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()


class PokemonModel(BaseAlchemy):
    __tablename__ = "POKEMON"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    tipo = db.Column(db.String(length=50))
    altura = db.Column(db.Float())
    peso = db.Column(db.Float())
    categoria = db.Column(db.String(length=50))
    habilidade = db.Column(db.String(length=10))
    habilidade2 = db.Column(db.String(length=100))
    fraqueza = db.Column(db.String(length=50))
    fraqueza2 = db.Column(db.String(length=50))
    descricao = db.Column(db.String(length=255))

    def __init__(self, nome, tipo, altura, peso, categoria, habilidade,
                 habilidade2, fraqueza, fraqueza2, descricao, id=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso
        self.categoria = categoria
        self.habilidade = habilidade
        self.habilidade2 = habilidade2
        self.fraqueza = fraqueza
        self.fraqueza2 = fraqueza2
        self.descricao = descricao

    def __str__(self):
        descricao = self.descricao.replace('.', '.\n')
        return f"""Codigo: {self.id}
Nome: {self.nome}
tipo: {self.tipo}
Altura: {str(self.altura) + ' m'}
Peso: {str(self.peso) + ' kg'}
Categoria: {self.categoria}
Habilidade: {self.habilidade}
Habilidade2: {self.habilidade}
Fraqueza: {self.fraqueza}
Fraqueza2: {self.fraqueza2}
Descricao: {descricao}"""


