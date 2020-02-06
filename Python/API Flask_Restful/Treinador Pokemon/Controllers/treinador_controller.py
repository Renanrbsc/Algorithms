from flask import request

from Dao.treinador_dao import TreinadorDao
from Model.treinador_model import TreinadorModel
from Controllers.base_controller import BaseController


class TreinadorController(BaseController):
    def __init__(self):
        super().__init__(TreinadorDao())

    def post(self):
        self.carrega_parametros()
        treinador = TreinadorModel(self.nome, self.sobrenome, self.idade, self.cidade, self.id_pokemon)
        return super().post(treinador)

    def put(self, id):
        self.carrega_parametros()
        treinador = TreinadorModel(self.nome, self.sobrenome, self.idade, self.cidade, self.id_pokemon, id)
        return super().put(treinador)

    def carrega_parametros(self):
        self.nome = request.json['nome']
        self.sobrenome = request.json['sobrenome']
        self.idade = int(request.json['idade'])
        self.cidade = request.json['cidade']
        self.id_pokemon = request.json['id_pokemon']
