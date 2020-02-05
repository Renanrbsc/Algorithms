class PokemonModel:
    def __init__(self, nome,tipo,altura,peso,categoria,habilidade,habilidade2,fraqueza,fraqueza2,descricao, id=0):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso
        self.categoria = categoria
        self.habilidade = habilidade
        self.habilidade2 = habilidade2
        self.fraqueza = fraqueza
        self.fraqueza2 = fraqueza2
        self.descricao = descricao
