def calcular_pi(numero):
    denominador = 1.0
    operador = 1.0
    pi = 0.0
    for i in range(numero):
        pi += operador * (4.0 / denominador)
        print(f'PI ({i}): {pi}')
        denominador += 2.0
        operador *= -1.0
    return pi


valores_precisao = [10, 100, 1000, 10000, 100000]
for numero in valores_precisao:
    print(f"Calculo do PI em Precisão de {numero}")
    calcular_pi(numero)
    print(f'------------------------------------')
