import random


class BuscarValorSequencial:
    """Recebe uma lista e um valor, roda um loop de verificação nos indices
    retorna o indice caso seja encontrado valor
    retorna false caso não encontre"""
    def busca_valor_sequencial(self, valor, lista):

        for i in range(0, len(lista)):
            if lista[i] == valor:
                return i

        return -1

    def main(self):
        print("---Buscando valor em lista---")
        tamanho = int(input("Informe o tamanho da lista: "))
        lista = []

        for i in range(tamanho):
            valores = random.randint(0, 100)
            lista.append(valores)
        print(lista)

        valor = int(input('Informe o valor a ser procurado: '))
        index = self.busca_valor_sequencial(valor, lista)

        if index >= 0:
            print(f"Encontrado valor {valor} na posição {index}.")
        else:
            print(f"Não foi encontrado o valor {valor}.")


# -- esse bloco da run apenas se for o principal
if __name__ == "__main__":
    busca = BuscarValorSequencial()
    busca.main()