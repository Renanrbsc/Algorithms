import random


class InsertionSort:

    def __init__(self):
        self.lista = []

    def ordenacao_por_insercao(self, lista):
        """ é um algoritmo de ordenação que recebe uma lista e
            ordena os valores do menor para o maior por ordem de chegada,
            fazendo uma inserção por vez."""

        for indice in range(1, len(lista)):
            valor = lista[indice]
            aux = indice - 1
            while aux >= 0 and lista[aux] > valor:
                lista[aux + 1] = lista[aux]
                aux -= 1
            lista[aux + 1] = valor
            print(lista)


    def main(self):
        tamanho = int(input("Informe o tamanho da lista: "))

        for i in range(tamanho):
            self.lista.append(random.randint(0, 99))
        print(f"---Lista Criada---\n"
              f"{self.lista}\n"
              f"-----------------")

        self.ordenacao_por_insercao(self.lista)


insertion_sort = InsertionSort()
insertion_sort.main()
