import random


if __name__ == "__main__":  # -- esse bloco inicia apenas se for o principal
    print("---Buscando valor em lista---")
    tamanho = int(input("Informe o tamanho da lista: "))

    lista = []
    for i in range(tamanho):
        val = random.randint(0, 100)
        lista.append(val)

    print(lista)

    valor = int(input('Informe o valor a ser procurado: '))

    # -- dois indices na enumeracao de lista
    for indice, value in enumerate(lista):
        print(f"Comparando valor {valor} com value {value} no indice {indice}  ="
              f" {'True' if valor == lista[indice] else 'False'}")
