# # ORM
# # ---- SqlAlchemy
# # ---- Instalação do framework
# # --- pip3 install sqlalchemy
#
# # ---- Conector do Mysql
# # ---- Instalação do conector do Mysql
# # ---- pip3 install mysql-connector-python

from Controller.pokemon_controller import PokemonController
from Model.pokemon_model import PokemonModel


class Views:
    def __init__(self):
        self.Poke_controller = PokemonController()
        self.op = None
        self.id = None

    def menu(self):
        print('-=' * 20)
        print('1 - Listar todos pokemon')
        print('2 - Buscar ID pokemon')
        print('3 - Inserir pokemon')
        print('4 - Alterar pokemon')
        print('5 - Deletar pokemon')
        print('-=' * 20)
        self.op = int(input("Digite a opcao: "))
        print('-=' * 20)

    def parameters(self):
        if self.op == 2 or self.op == 4 or self.op == 5:
            self.id = int(input("Digite a id do Pokemon:"))
        if self.op == 3 or self.op == 4:
            Pokemon = PokemonModel(nome=input("Digite o nome:"),
                                   tipo=input("Digite o tipo:"),
                                   altura=float(input("Digite a altura:")),
                                   peso=float(input("Digite o peso:")),
                                   categoria=input("Digite a categoria:"),
                                   habilidade=input("Digite a habilidade:"),
                                   habilidade2=input("Digite a habilidade2:"),
                                   fraqueza=input("Digite a fraqueza:"),
                                   fraqueza2=input("Digite a fraqueza2:"),
                                   descricao=input("Digite a descricao:")
                                   )
            return Pokemon

    def conditions(self):
        if self.op == 1:
            pokemon_all = self.Poke_controller.get_all()
            for pokemon in pokemon_all:
                print(pokemon)

        if self.op == 2:
            self.parameters()
            print(self.Poke_controller.get_by_id(self.id))

        if self.op == 3:
            print('----Adicionar Pokemon----')
            Pokemon = self.parameters()
            print(self.Poke_controller.post(Pokemon))

        if self.op == 4:
            print('----Alterar Pokemon----')
            Pokemon = self.parameters()
            print(self.Poke_controller.put(self.id, Pokemon))

        if self.op == 5:
            print('----Remover Pokemon----')
            self.parameters()
            print(self.Poke_controller.delete(self.id))


views = Views()

while True:
    views.menu()
    views.conditions()
