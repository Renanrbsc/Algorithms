from Orientacao_Objeto.Exercicio_classes.pessoa import Pessoa, RetornoSalario


class Engenheiro(Pessoa):
    def __init__(self, graduacao: str, projeto: str, nome: str, sobrenome: str,
                       idade: int, numero_de_horas_salario: str, pais: str, 
                       estado: str, cidade: str, bairro: str, rua: str):

        calcular_salario = RetornoSalario(numero_de_horas_salario, 50)
        super().__init__(nome, sobrenome, idade, calcular_salario.calcular_salario_bruto(),
                                                         pais, estado, cidade, bairro, rua)

        self.graduacao = graduacao
        self.projeto = projeto

    @property
    def graduacao(self) -> str:
        return self._graduacao

    @graduacao.setter
    def graduacao(self, graduacao: str) -> None:
        self._graduacao = graduacao

    @property
    def projeto(self) -> str:
        return self._projeto

    @projeto.setter
    def projeto(self, projeto: str) -> None:
        self._projeto = projeto

    def __str__(self):
        return f"----- Engenheiro ----- \n" \
               f"Graduação: {self.graduacao} \n" \
               f"Projeto Atual: {self.projeto} \n" \
               f"{super().__str__()}"
