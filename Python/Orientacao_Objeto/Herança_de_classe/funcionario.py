from random import randint
from Orientacao_Objeto_Python.Herança_de_classe.pessoa_base import PessoaBase


class Funcionario(PessoaBase):

    def __init__(self, nome: str, sobrenome: str, idade: int, cpf: str, local: str):
        super().__init__(nome, sobrenome, idade)
        self.cpf = cpf
        self.local = local
        self.id_funcionario = None

    @property
    def id_funcionario(self) -> int:
        return self._id_funcionario

    @id_funcionario.setter
    def id_funcionario(self, id_funcionario: None) -> None:
        if id_funcionario is None:
            id_funcionario = self.gerador_de_id()
        self._id_funcionario = id_funcionario

    def mostrar_dados(self) -> None:
        print(f'{super().nome_completo()}\n'
              f'Idade: {super().idade}\n'
              f'{super().ano_de_nascimento()}\n'
              f'CPF: {self.cpf}\n'
              f'Local de Trabalho: {self.local}\n'
              f'Id funcionario: {self.id_funcionario}\n')

    @staticmethod
    def gerador_de_id() -> int:
        random_id_funcionario = randint(100, 999)
        return random_id_funcionario
