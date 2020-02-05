import MySQLdb

from Model.treinador_model import TreinadorModel
from Dao.database_config import DatabaseConfig

class TreinadorDao(DatabaseConfig):
    # --- Inicialização da conecção com o servidor local
    # --- Inicialização do cursor para manter conecção
    def __init__(self):
        super().__init__('TREINADOR')# Metodo para chamar a classe de herança

    # --- Metodo para buscar todos os registro de uma tabela local
    # --- Retorna uma lista de tuplas e cada tupla convertida em dicionario de classe Model
    # --- Adicionado cada dicionario na lista que retorna
    def get_all(self):
        treinador_all = super().get_all()
        list_treinador = []
        for treinador in treinador_all:
            treinador = TreinadorModel(treinador[1],treinador[2],treinador[3],treinador[4],treinador[5],treinador[0])
            list_treinador.append(treinador.__dict__)
        return list_treinador
    
    def get_by_id(self, id):
        treinador = super().get_by_id(id)
        train = TreinadorModel(treinador[1],treinador[2],treinador[3],treinador[4],treinador[5],treinador[0])
        return train.__dict__
    
    def insert(self, treinador : TreinadorModel):
        command_sql = (f"""
            INSERT INTO {self.table} 
                (NOME, SOBRENOME, IDADE, CIDADE, ID_POKEMON) 
            VALUES
                ('{treinador.nome}','{treinador.sobrenome}',{treinador.idade},'{treinador.cidade}',{treinador.id_pokemon})
        """)
        treinador.id = super().insert(command_sql)
        return treinador.__dict__
    
    def update(self, treinador : TreinadorModel):
        command_sql = (f"""
            UPDATE {self.table} 
                SET 
                    NOME = '{treinador.nome}',
                    SOBRENOME = '{treinador.sobrenome}',
                    IDADE = {treinador.idade},
                    CIDADE = '{treinador.cidade}',
                    ID_POKEMON = {treinador.id_pokemon}
                WHERE id = {treinador.id}
         """)
        super().update(command_sql)
        return treinador.__dict__
    
    def remove(self, id):
        return super().remove(id)
    