from Orientacao_Objeto.Exercicio_classes.pessoa import Pessoa, RetornoSalario


class Administrador(Pessoa):
    def __init__(self, graduacao: str, setor: str, nome: str, sobrenome: str,
                       idade: int, numero_de_horas_salario: int, pais: str,
                       estado: str, cidade: str, bairro: str, rua: str):

        calcular_salario = RetornoSalario(numero_de_horas_salario,30)
        super().__init__(nome, sobrenome, idade, calcular_salario.calcular_salario_bruto(),
                                                         pais, estado, cidade, bairro, rua)
        self.graduacao = graduacao
        self.setor = setor

    @property
    def graduacao(self) -> str:
        return self._graduacao

    @graduacao.setter
    def graduacao(self, graduacao: str) -> None:
        self._graduacao = graduacao

    @property
    def setor(self) -> str:
        return self._setor

    @setor.setter
    def setor(self, setor: str) -> None:
        self._setor = setor

    def __str__(self):
        return f"----- Administrador ----- \n" \
               f"Graduação: {self.graduacao} \n" \
               f"Projeto Atual: {self.setor} \n" \
               f"{super().__str__()}"
