from flask_restful import Resource

from Dao.produto_dao import ProdutoDao


class ProdutoController(Resource):
    def __init__(self):
        self.dao = ProdutoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.get_all()

    def post(self):
        return 'Insert'

    def put(self, id):
        return f'Update {id}'

    def delete(self, id):
        return f'remove {id}'

