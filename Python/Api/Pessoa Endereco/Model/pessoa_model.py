# --- Classe Model para recebimento de dados do Database
# --- Inicia com recebimento no parametros e salva dados em selfs de resultado
# --- Usada para converter em dict

class PessoaModel:
    def __init__(self, nome, sobrenome, idade, genero, email, telefone, codigo=0):
        self.codigo = codigo
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.genero = genero
        self.email = email
        self.telefone = telefone
   