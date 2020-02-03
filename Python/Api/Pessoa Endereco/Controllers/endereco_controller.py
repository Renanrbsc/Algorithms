from flask_restful import Resource
from flask import request
from Dao.endereco_dao import EnderecoDao
from Model.endereco_model import EnderecoModel

class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.get_all()

    def post(self):
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        sigla = request.json['sigla']
        cidade = request.json['cidade']
        bairro = request.json['bairro']
        cep = int(request.json['cep'])
        address = EnderecoModel(logradouro,numero,sigla,cidade,bairro,cep)
        msg = self.dao.insert(address)
        return msg

    def put(self, id):
        logradouro = request.json['logradouro']
        numero = int(request.json['numero'])
        sigla = request.json['sigla']
        cidade = request.json['cidade']
        bairro = request.json['bairro']
        cep = int(request.json['cep'])
        address = EnderecoModel(logradouro,numero,sigla,cidade,bairro,cep, id)
        msg = self.dao.update(address)
        return msg

    def delete(self, id):
        msg = self.dao.remove(id)
        return msg



    

