class PokemonModel:
    def __init__(self, nome,altura,peso,categoria,habilidade,habilidade2,tipo,fraqueza,fraqueza2,descricao, id=0):
        self.id = id
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.categoria = categoria
        self.habilidade = habilidade
        self.habilidade2 = habilidade2
        self.tipo = tipo
        self.fraqueza = fraqueza
        self.fraqueza2 = fraqueza2
        self.descricao = descricao

