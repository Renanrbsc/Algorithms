class ProdutoModel:
    def __init__(self, nome, tipo, marca, quantidade, valor, id=0, validade=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.marca = marca
        self.quantidade = quantidade
        self.valor = valor
        self.validade = validade