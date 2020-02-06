import sys

sys.path.append(r'C:\Users\Usuario\Documents\GitHub\Desbravando-Algoritmos\Python\Api\Produtos')

from flask import Flask
from flask_restful import Api

from Controller.produtos_controller import ProdutoController

app = Flask(__name__)
api = Api(app)

api.add_resource(ProdutoController, '/api/produto', endpoint='produtos')
api.add_resource(ProdutoController, '/api/produto/<int:id>', endpoint='produto')

if __name__ == '__main__':
    app.run(debug=True, port=80)

