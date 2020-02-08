import random

class BuscaSequencialEnumerate:

    def __init__(self):
        self.valor = None

    def sequencial_enumerate(self, lista):

        # -- dois indices na enumeracao de lista
        for indice, value in enumerate(lista):
            print(f"Comparando valor {self.valor} com value {value} no indice {indice}  ="
                  f" {'True' if self.valor == lista[indice] else 'False'}")

    def main(self):

        print("---Buscando valor em lista---")
        tamanho = int(input("Informe o tamanho da lista: "))

        lista = []
        for i in range(tamanho):
            val = random.randint(0, 100)
            lista.append(val)

        print(lista)

        self.valor = int(input('Informe o valor a ser procurado: '))
        self.sequencial_enumerate(lista)


if __name__ == "__main__":  # -- esse bloco inicia apenas se for o principal
    busca_sequencial = BuscaSequencialEnumerate()
    busca_sequencial.main()
