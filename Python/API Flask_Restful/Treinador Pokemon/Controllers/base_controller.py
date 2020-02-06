from flask_restful import Resource


class BaseController(Resource):
    def __init__(self, dao):
        self.dao = dao

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.get_all()

    def post(self, model):
        return self.dao.insert(model)

    def put(self, model):
        return self.dao.update(model)

    def delete(self, id):
        return self.dao.remove(id)
