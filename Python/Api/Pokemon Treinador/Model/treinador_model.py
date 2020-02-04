# --- Classe Model para recebimento de dados do Database
# --- Inicia com recebimento no parametros e salva dados em selfs de resultado
# --- Usada para converter em dict

class TreinadorModel:
    def __init__(self, nome, sobrenome, idade, cidade, id=0, id_pokemon=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
        self.id_pokemon = id_pokemon

        


   