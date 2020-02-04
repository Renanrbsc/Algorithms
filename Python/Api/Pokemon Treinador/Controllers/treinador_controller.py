from flask_restful import Resource
from flask import request
from Dao.treinador_dao import TreinadorDao
from Model.treinador_model import TreinadorModel

class TreinadorController(Resource):
    def __init__(self):
        self.dao = TreinadorDao()
        
    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.get_all()
    
    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        cidade = request.json['cidade']
        id_pokemon1 = request.json['id_pokemon1']
        id_pokemon2 = request.json['id_pokemon2']
        id_pokemon3 = request.json['id_pokemon3']
        treinador = TreinadorModel(nome,sobrenome,idade,cidade,id_pokemon1,id_pokemon2,id_pokemon3)
        msg = self.dao.insert(treinador)
        return msg
    
    def put(self, id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        cidade = request.json['cidade']
        id_pokemon1 = request.json['id_pokemon1']
        id_pokemon2 = request.json['id_pokemon2']
        id_pokemon3 = request.json['id_pokemon3']
        treinador = TreinadorModel(nome,sobrenome,idade,cidade,id_pokemon1,id_pokemon2,id_pokemon3,id)
        msg = self.dao.update(treinador)
        return msg
    
    def delete(self, id):
        return self.dao.remove(id)
    
    
        