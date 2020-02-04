import MySQLdb

from Model.treinador_model import TreinadorModel

class TreinadorDao:
    # --- Inicialização da conecção com o servidor local
    # --- Inicialização do cursor para manter conecção
    def __init__(self):
        self.connection = MySQLdb.connect(host='127.0.0.1',database='PadawanHBSIS',user='root')
        self.cursor = self.connection.cursor()

    # --- Metodo para buscar todos os registro de uma tabela local
    # --- Retorna uma lista de tuplas e cada tupla convertida em dicionario de classe Model
    # --- Adicionado cada dicionario na lista que retorna
    def get_all(self):
        self.cursor.execute("SELECT * FROM TREINADOR")
        treinador_all = self.cursor.fetchall()
        list_treinador = []
        for treinador in treinador_all:
            treinador = TreinadorModel(treinador[1],treinador[2],treinador[3],treinador[4],treinador[5],treinador[6],treinador[7],treinador[0])
            list_treinador.append(treinador.__dict__)
        return list_treinador
    
    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM TREINADOR WHERE ID = {}".format(id))
        treinador = self.cursor.fetchone()
        train = TreinadorModel(treinador[1],treinador[2],treinador[3],treinador[4],treinador[5],treinador[6],treinador[7],treinador[0])
        return train.__dict__
    
    def insert(self, treinador : TreinadorModel):
        self.cursor.execute("""
            INSERT INTO TREINADOR 
            (NOME, SOBRENOME, IDADE, CIDADE, ID_POKEMON1, ID_POKEMON2, ID_POKEMON3) 
            VALUES('{}','{}',{},'{}',{},{},{})""".format(treinador.nome, treinador.sobrenome, treinador.idade, treinador.cidade, treinador.id_pokemon1, treinador.id_pokemon2, treinador.id_pokemon3))
        self.connection.commit()
        id = self.cursor.lastrowid
        treinador.id = id
        return treinador.__dict__
    
    def update(self, treinador : TreinadorModel):
        self.cursor.execute("""
            UPDATE TREINADOR 
                SET 
                    NOME = '{}',
                    SOBRENOME = '{}',
                    IDADE = {},
                    CIDADE = '{}',
                    ID_POKEMON1 = {},
                    ID_POKEMON2 = {},
                    ID_POKEMON3 = {}
                WHERE id = {}
         """.format(treinador.nome, treinador.sobrenome, treinador.idade, treinador.cidade, treinador.id_pokemon1, treinador.id_pokemon2, treinador.id_pokemon3, treinador.id))
        self.connection.commit()
        return treinador.__dict__
    
    def remove(self, id):
        self.cursor.execute("DELETE FROM TREINADOR WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido o treinador de id: {}'.format(id)
    
    
    
    