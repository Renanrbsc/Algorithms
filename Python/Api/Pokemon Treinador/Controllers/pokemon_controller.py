from flask_restful import Resource
from flask import request
from Dao.pokemon_dao import PokemonDao
from Model.pokemon_model import PokemonModel

class PokemonController(Resource):
    def __init__(self):
        self.dao = PokemonDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.get_all()

    def post(self):
        nome = request.json['nome']
        tipo = request.json['tipo']
        altura = float(request.json['altura'])
        peso = float(request.json['peso'])
        categoria = request.json['categoria']
        habilidade = request.json['habilidade']
        habilidade2 = request.json['habilidade2']
        fraqueza = request.json['fraqueza']
        fraqueza2 = request.json['fraqueza2']
        descricao = request.json['descricao']
        pokemon = PokemonModel(nome,tipo,altura,peso,categoria,habilidade,habilidade2,fraqueza,fraqueza2,descricao)
        msg = self.dao.insert(pokemon)
        return msg

    def put(self, id):
        nome = request.json['nome']
        tipo = request.json['tipo']
        altura = float(request.json['altura'])
        peso = float(request.json['peso'])
        categoria = request.json['categoria']
        habilidade = request.json['habilidade']
        habilidade2 = request.json['habilidade2']
        fraqueza = request.json['fraqueza']
        fraqueza2 = request.json['fraqueza2']
        descricao = request.json['descricao']
        pokemon = PokemonModel(nome,tipo,altura,peso,categoria,habilidade,habilidade2,fraqueza,fraqueza2,descricao, id)
        msg = self.dao.update(pokemon)
        return msg

    def delete(self, id):
        msg = self.dao.remove(id)
        return msg
