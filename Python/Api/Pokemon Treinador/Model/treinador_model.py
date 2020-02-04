# --- Classe Model para recebimento de dados do Database
# --- Inicia com recebimento no parametros e salva dados em selfs de resultado
# --- Usada para converter em dict

class TreinadorModel:
    def __init__(self, nome, sobrenome, idade, cidade, id_pokemon1=None, id_pokemon2=None,id_pokemon3=None, id=0):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
        self.id_pokemon1 = id_pokemon1
        self.id_pokemon2 = id_pokemon2
        self.id_pokemon3 = id_pokemon3
        


   