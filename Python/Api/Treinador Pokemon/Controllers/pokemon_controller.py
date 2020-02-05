from flask import request

from Dao.pokemon_dao import PokemonDao
from Model.pokemon_model import PokemonModel
from Controllers.base_controller import BaseController


class PokemonController(BaseController):
    def __init__(self):
        super().__init__(PokemonDao())

    def post(self):
        self.carrega_parametros()
        model = PokemonModel(self.nome, self.tipo, self.altura, self.peso, self.categoria,
                             self.habilidade, self.habilidade2, self.fraqueza, self.fraqueza2, self.descricao)
        return super().post(model)

    def put(self, id):
        self.carrega_parametros()
        model = PokemonModel(self.nome, self.tipo, self.altura, self.peso, self.categoria,
                             self.habilidade, self.habilidade2, self.fraqueza, self.fraqueza2, self.descricao, self.id)
        return super().put(model)

    def carrega_parametros(self):
        self.nome = request.json['nome']
        self.tipo = request.json['tipo']
        self.altura = float(request.json['altura'])
        self.peso = float(request.json['peso'])
        self.categoria = request.json['categoria']
        self.habilidade = request.json['habilidade']
        self.habilidade2 = request.json['habilidade2']
        self.fraqueza = request.json['fraqueza']
        self.fraqueza2 = request.json['fraqueza2']
        self.descricao = request.json['descricao']
