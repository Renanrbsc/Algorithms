import MySQLdb

from Model.pessoa_model import PessoaModel

class PessoaDao:
    # --- Inicialização da conecção com o servidor local
    # --- Inicialização do cursor para manter conecção
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.padawans.dev',database='padawans16',user='padawans16',passwd="lr2019")
        self.cursor = self.connection.cursor()

    # --- Metodo para buscar todos os registro de uma tabela local
    # --- Retorna uma lista de tuplas e cada tupla convertida em dicionario de classe Model
    # --- Adicionado cada dicionario na lista que retorna
    def get_all(self):
        self.cursor.execute("SELECT * FROM CLIENTE")
        many_people = self.cursor.fetchall()
        list_people = []
        for people in many_people:
            people = PessoaModel(people[1],people[2],people[3],people[4],people[5],people[6],people[0])
            list_people.append(people.__dict__)
        return list_people
    
    def get_by_id(self, codigo):
        self.cursor.execute("SELECT * FROM CLIENTE WHERE CODIGO = {}".format(codigo))
        people = self.cursor.fetchone()
        p = PessoaModel(people[1],people[2],people[3],people[4],people[5],people[6],people[0])
        return p.__dict__
    
    def insert(self, pessoa : PessoaModel):
        self.cursor.execute("""
            INSERT INTO CLIENTE 
            (NOME, SOBRENOME, IDADE, GENERO, EMAIL, TELEFONE) 
            VALUES('{}','{}',{},'{}','{}','{}')""".format(pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.genero, pessoa.email, pessoa.telefone))
        self.connection.commit()
        codigo = self.cursor.lastrowid
        pessoa.codigo = codigo
        return pessoa.__dict__
    
    def update(self, pessoa : PessoaModel):
        self.cursor.execute("""
            UPDATE CLIENTE 
                SET 
                    NOME = '{}',
                    SOBRENOME = '{}',
                    IDADE = {},
                    GENERO = '{}',
                    EMAIL = '{}',
                    TELEFONE = '{}'
                WHERE CODIGO = {}
         """.format(pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.genero, pessoa.email, pessoa.telefone, pessoa.codigo))
        self.connection.commit()
        return pessoa.__dict__
    
    def remove(self, codigo):
        self.cursor.execute("DELETE FROM CLIENTE WHERE CODIGO = {}".format(codigo))
        self.connection.commit()
        return 'Removido a pessoa de id: {}'.format(codigo)
    
    
    
    