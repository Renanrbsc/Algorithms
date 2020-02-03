class EnderecoModel:
    def __init__(self, logradouro, numero, sigla, cidade, bairro, cep, id=0):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.sigla = sigla
        self.cidade = cidade
        self.bairro = bairro
        self.cep = cep

