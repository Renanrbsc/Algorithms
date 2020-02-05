import MySQLdb

from Model.pokemon_model import PokemonModel
from Dao.database_config import DatabaseConfig

class PokemonDao(DatabaseConfig):

    def __init__(self):
        super().__init__('POKEMON')

    def get_all(self):
        self.cursor.execute(f"SELECT * FROM {self.table}")
        pokemon_all = self.cursor.fetchall()
        list_pokemon = []
        for pokemon in pokemon_all:
            pokemon = PokemonModel(pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[0])
            list_pokemon.append(pokemon.__dict__)
        return list_pokemon

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE ID = {id}")
        pokemon = self.cursor.fetchone()
        poke = PokemonModel(pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[0])
        return poke.__dict__

    def insert(self, pokemon:PokemonModel):
        self.cursor.execute(f"""
            INSERT INTO {self.table}
                (nome,tipo,altura,peso,categoria,habilidade,habilidade2,fraqueza,fraqueza2,descricao) 
            VALUES
                ('{pokemon.nome}','{pokemon.tipo}',{pokemon.altura},{pokemon.peso},'{pokemon.categoria}','{pokemon.habilidade}','{pokemon.habilidade2}','{pokemon.fraqueza}','{pokemon.fraqueza2}','{pokemon.descricao}')
        """)
        self.connection.commit()
        id = self.cursor.lastrowid
        pokemon.id = id
        return pokemon.__dict__

    def update(self, pokemon:PokemonModel):
        self.cursor.execute(f"""
            UPDATE {self.table} 
                SET 
                    NOME = '{pokemon.nome}',
                    TIPO = '{pokemon.tipo}',
                    ALTURA = {pokemon.altura},
                    PESO = {pokemon.peso},
                    CATEGORIA = '{pokemon.categoria}',
                    HABILIDADE = '{pokemon.habilidade}',
                    HABILIDADE2 = '{pokemon.habilidade2}',
                    FRAQUEZA = '{pokemon.fraqueza}',
                    FRAQUEZA2 = '{pokemon.fraqueza2}',
                    DESCRICAO = '{pokemon.descricao}'
                WHERE ID = {pokemon.id}
        """)
        self.connection.commit()
        return pokemon.__dict__

    def remove(self, id):
        self.cursor.execute(f"DELETE FROM {self.table} WHERE ID = {id}")
        self.connection.commit()
        return f'Removido o pokemon de id: {id}'




    
