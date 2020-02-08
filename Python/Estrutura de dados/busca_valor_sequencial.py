import random


def busca_valor_sequencial(valor, lista):
    """Recebe uma lista e um valor, roda um loop de verificação nos indices
        retorna o indice caso seja encontrado valor
        retorna false caso não encontre"""
    for i in range(0, len(lista)):
        if lista[i] == valor:
            return i
    return -1


if __name__ == "__main__":  # -- esse bloco da run apenas se for o principal
    print("---Buscando valor em lista---")
    tamanho = int(input("Informe o tamanho da lista: "))

    lista = []
    for i in range(tamanho):
        val = random.randint(0, 100)
        lista.append(val)

    print(lista)

    valor = int(input('Informe o valor a ser procurado: '))
    index = busca_valor_sequencial(valor, lista)

    if index >= 0:
        print(f"Encontrado valor {valor} na posição {index}.")
    else:
        print(f"Não foi encontrado o valor {valor}.")
