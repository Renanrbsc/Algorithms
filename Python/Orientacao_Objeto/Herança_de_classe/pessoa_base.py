class PessoaBase:
    _ano_atual = 2020

    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self._idade = idade

    @property
    def idade(self) -> int:
        return self._idade

    def nome_completo(self) -> str:
        return f'Nome Completo: {self.nome} {self.sobrenome}'

    def ano_de_nascimento(self) -> str:
        return f'Ano de nascimento: {self._ano_atual - self.idade}'



