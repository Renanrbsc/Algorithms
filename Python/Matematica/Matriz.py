import random

N_LINHAS = 8
N_COLUNAS = 8


def crie_matriz(n_linhas, n_colunas):
    """ (int, int, valor) -> matriz (lista de listas)

    Cria e retorna uma matriz com n_linhas linha e n_colunas
    colunas em que cada elemento é aleatorio entre 0.0 e 9.9
    """

    matriz = []  # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = []  # lista vazia
        for j in range(n_colunas):
            valor = float(random.randint(0, 99))/10
            linha.append(valor)
        # coloque linha na matriz
        matriz.append(linha)

    return matriz


# -----------------------

Matriz = crie_matriz(N_LINHAS, N_COLUNAS)
for i in Matriz:
    print(i)
