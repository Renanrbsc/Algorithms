from Orientacao_Objeto_Python.Herança_de_classe.pessoa_base import PessoaBase


class Cliente(PessoaBase):

    def __init__(self, nome: str, sobrenome: str, idade: int, cpf: str, despesas: float):
        super().__init__(nome, sobrenome, idade)
        self.cpf = cpf
        self.despesas = despesas

    def mostrar_dados(self) -> None:
        print(f'{super().nome_completo()}\n'
              f'Idade: {super().idade}\n'
              f'{super().ano_de_nascimento()}\n'
              f'CPF: {self.cpf}\n'
              f'Valor a Pagar: R${self.despesas}\n')



