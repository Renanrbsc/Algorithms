from Orientacao_Objeto.Exercicio_classes.endereco import Endereco


class RetornoSalario:
    def __init__(self, numero_horas_trabalhadas: str, salario_por_hora: int):
        self.numero_horas_trabalhadas = numero_horas_trabalhadas
        self.salario_por_hora = salario_por_hora

    @property
    def numero_horas_trabalhadas(self):
        print(f'Nome: {self._numero_horas_trabalhadas}')
        return self._numero_horas_trabalhadas

    @numero_horas_trabalhadas.setter
    def numero_horas_trabalhadas(self, numero_horas_trabalhadas: str):
        self._numero_horas_trabalhadas = int(numero_horas_trabalhadas)

    def calcular_salario_bruto(self) -> int:
        return self._numero_horas_trabalhadas * self.salario_por_hora


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int,
                       salario: str, pais: str, estado: str,
                       cidade: str, bairro: str, rua: str):

        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.salario = salario
        self.endereco = Endereco(pais, estado, cidade, bairro, rua)

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def sobrenome(self) -> str:
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome: str) -> None:
        self._sobrenome = sobrenome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, salario: str) -> None:
        if isinstance(salario, str):
            salario = salario.replace('R$', '')
        self._salario = float(salario)

    def __str__(self):
        return f"----- Dados Pessoais ----- \n" \
               f"Nome: {self.nome} \n" \
               f"Sobrenome: {self.sobrenome} \n" \
               f"Idade: {self.idade} \n" \
               f"Salario: {self.salario} \n" \
               f"----- Endereco ----- \n" \
               f"{self.endereco}"
