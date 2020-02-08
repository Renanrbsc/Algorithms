
def Exponenciacao(base, expoente):
    result = base
    for i in range(0, expoente-1):
        result *= base
    return result


print(f'Exemplo: A base {5} elevada em {5} é : {Exponenciacao(5, 5)}')

base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))

print(f'A base {base} elevada em {expoente} é: {Exponenciacao(base, expoente)}')
