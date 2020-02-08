class ConversorBinario:

    def __init__(self):
        self.binario = ''

    def decimal_para_binario(self, numero):

        while numero != 0:
            self.binario = self.binario + str(numero % 2)
            numero = int(numero / 2)

        return self.binario[::-1]

    def main(self):

        numero = int(input("informe um numero: "))

        print(f'Valor referente em binario: {self.decimal_para_binario(numero)}')

if __name__ == "__main__":
    conversor = ConversorBinario()
    conversor.main()

