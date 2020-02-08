def Fatorial(num):
    aux = 1
    for i in range(2, num + 1):
        aux = aux * i
    return aux


print(f'Exemplo: A Fatoração de {5} é: {Fatorial(5)}')

valor = int(input("Informe o valor: "))
print(f'A Fatoração de {valor} é: {Fatorial(valor)}')


