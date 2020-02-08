import random


class Fila:

    def __init__(self):
        self.fila = []

    def adicionar_valor_final_da_fila(self, valor):
        self.fila.append(valor)

    def retirar_primeiro_valor_da_fila(self):
        return self.fila.pop(0)

    def imprimir_na_tela(self):
        return f"Fila: {self.fila}"

    def direcao_da_fila(self):
        return f"      <---<---<---<---<---<---<---<---<---<---\n"

    def main(self):

        for i in range(0, 10):
            self.adicionar_valor_final_da_fila(random.randint(10, 99))
        print(f"---Fila Inicial---")
        self.imprimir_na_tela()

        for i in range(1, 11):
            print(f"---Fila {i}---")
            self.retirar_primeiro_valor_da_fila()
            self.adicionar_valor_final_da_fila(random.randint(10, 99))
            self.imprimir_na_tela()
            self.direcao_da_fila()


if __name__ == "__main__":
    fila = Fila()
    fila.main()
