from flask import Flask, render_template
from flask_restful import Api

from Controllers.pessoa_controller import PessoaController
from Controllers.endereco_controller import EnderecoController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa', endpoint='many_people')
api.add_resource(PessoaController, '/api/pessoa/<int:codigo>', endpoint='people')

api.add_resource(EnderecoController, '/api/endereco', endpoint='enderecos')
api.add_resource(EnderecoController, '/api/endereco/<int:id>', endpoint='endereco')


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
