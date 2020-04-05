from random import randint


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def calcular_idade_atraves_do_ano(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gerar_id():
        random_id = randint(10000, 19999)
        return random_id


# criando um objeto com inicio no classmethod que retorna a propria classe com as conversões
primeira_pessoa = Pessoa.calcular_idade_atraves_do_ano('Renan', 1998)

# criando o objeto da classe sem o classmethod
# primeira_pessoa = Pessoa('Renan', 21)

print(f"Espaço de memoria do objeto 'primeira_pessoa' da classe 'Pessoa': {primeira_pessoa}")
print(f"Nome: {primeira_pessoa.nome}, Idade: {primeira_pessoa.idade}")
primeira_pessoa.get_ano_nascimento()
print(f"Gerando id pelo metodo estatico da classe Pessoa: {Pessoa.gerar_id()}")
print(f"Gerando id pelo metodo estatico do objeto primeira_pessoa: {primeira_pessoa.gerar_id()}")
