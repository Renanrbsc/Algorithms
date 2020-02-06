from flask_restful import Resource
from flask import request
from Dao.pessoa_dao import PessoaDao
from Model.pessoa_model import PessoaModel

class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()
        
    def get(self, codigo=None):
        if codigo:
            return self.dao.get_by_id(codigo)
        return self.dao.get_all()
    
    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        genero = request.json['genero']
        email = request.json['email']
        telefone = request.json['telefone']
        pessoa = PessoaModel(nome,sobrenome,idade,genero,email,telefone)
        msg = self.dao.insert(pessoa)
        return msg
    
    def put(self, codigo):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        genero = request.json['genero']
        email = request.json['email']
        telefone = request.json['telefone']
        pessoa = PessoaModel(nome, sobrenome, idade, genero, email, telefone, codigo)
        msg = self.dao.update(pessoa)
        return msg
    
    def delete(self, codigo):
        return self.dao.remove(codigo)
    
    
        