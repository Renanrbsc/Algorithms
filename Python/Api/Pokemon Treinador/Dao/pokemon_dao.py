import MySQLdb

from Model.pokemon_model import PokemonModel

class PokemonDao:

    def __init__(self):
        self.connection = MySQLdb.connect(host='127.0.0.1',database='PadawanHBSIS',user='root')
        self.cursor = self.connection.cursor()

    def get_all(self):
        self.cursor.execute("SELECT * FROM POKEMON")
        pokemon_all = self.cursor.fetchall()
        list_pokemon = []
        for pokemon in pokemon_all:
            pokemon = PokemonModel(pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[0])
            list_pokemon.append(pokemon.__dict__)
        return list_pokemon

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM POKEMON WHERE ID = {}".format(id))
        pokemon = self.cursor.fetchone()
        poke = PokemonModel(pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[0])
        return poke.__dict__

    def insert(self, pokemon:PokemonModel):
        self.cursor.execute("""
            INSERT INTO POKEMON
            (nome,altura,peso,categoria,habilidade,habilidade2,tipo,fraqueza,fraqueza2,descricao) 
            VALUES('{}',{},{},'{}','{}','{}','{}','{}','{}','{}')""".format(pokemon.nome, pokemon.altura, pokemon.peso, pokemon.categoria, pokemon.habilidade, pokemon.habilidade2, pokemon.tipo, pokemon.fraqueza, pokemon.fraqueza2, pokemon.descricao))
        self.connection.commit()
        id = self.cursor.lastrowid
        pokemon.id = id
        return pokemon.__dict__

    def update(self, pokemon:PokemonModel):
        self.cursor.execute("""
            UPDATE POKEMON 
                SET 
                    NOME = '{}',
                    ALTURA = {},
                    PESO = {},
                    CATEGORIA = '{}',
                    HABILIDADE = '{}',
                    HABILIDADE2 = '{}',
                    TIPO = '{}',
                    FRAQUEZA = '{}',
                    FRAQUEZA2 = '{}',
                    DESCRICAO = '{}'
                WHERE ID = {}
         """.format(pokemon.nome, pokemon.altura, pokemon.peso, pokemon.categoria, pokemon.habilidade, pokemon.habilidade2, pokemon.tipo, pokemon.fraqueza, pokemon.fraqueza2, pokemon.descricao, pokemon.id))
        self.connection.commit()
        return pokemon.__dict__

    def remove(self, id):
        self.cursor.execute("DELETE FROM POKEMON WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido o pokemon de id: {}'.format(id)




    
