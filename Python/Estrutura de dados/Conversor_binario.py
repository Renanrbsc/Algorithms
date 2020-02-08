def decimal_para_binario(numero):
    decimal = ''

    while numero != 0:
        decimal = decimal + str(numero % 2)
        numero = int(numero / 2)

    return b[::-1]


numero = int(input("informe um numero: "))

print(f'Valor referente em binario: {decimal_para_binario(numero)}')
