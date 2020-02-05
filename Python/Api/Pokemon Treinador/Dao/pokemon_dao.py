import MySQLdb

from Model.pokemon_model import PokemonModel
from Dao.database_config import DatabaseConfig

class PokemonDao(DatabaseConfig):

    def __init__(self):
        super().__init__('POKEMON')

    def get_all(self):
        pokemon_all = super().get_all()
        list_pokemon = []
        for pokemon in pokemon_all:
            pokemon = PokemonModel(pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],
                                   pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[0])
            list_pokemon.append(pokemon.__dict__)
        return list_pokemon

    def get_by_id(self, id):
        pokemon = super().get_by_id(id)
        poke = PokemonModel(pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],
                            pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[0])
        return poke.__dict__

    def insert(self, pokemon:PokemonModel):
        command_sql = (f"""
            INSERT INTO {self.table}
                (nome,tipo,altura,peso,categoria,habilidade,habilidade2,fraqueza,fraqueza2,descricao) 
            VALUES
                ('{pokemon.nome}','{pokemon.tipo}',{pokemon.altura},{pokemon.peso},'{pokemon.categoria}','{pokemon.habilidade}','{pokemon.habilidade2}','{pokemon.fraqueza}','{pokemon.fraqueza2}','{pokemon.descricao}')
        """)
        pokemon.id = super().insert(command_sql)
        return pokemon.__dict__

    def update(self, pokemon:PokemonModel):
        command_sql = (f"""
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
        super().update(command_sql)
        return pokemon.__dict__

    def remove(self, id):
        return super().remove(id)





    
