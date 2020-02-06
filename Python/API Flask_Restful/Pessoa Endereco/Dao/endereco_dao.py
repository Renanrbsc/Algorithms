import MySQLdb

from Model.endereco_model import EnderecoModel

class EnderecoDao:

    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.padawans.dev',database='padawans16',user='padawans16',passwd="lr2019")
        self.cursor = self.connection.cursor()

    def get_all(self):
        self.cursor.execute("SELECT * FROM ENDERECO")
        many_address = self.cursor.fetchall()
        list_address = []
        for address in many_address:
            address = EnderecoModel(address[1],address[2],address[3],address[4],address[5],address[6],address[0])
            list_address.append(address.__dict__)
        return list_address

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM ENDERECO WHERE ID = {}".format(id))
        address = self.cursor.fetchone()
        ad = EnderecoModel(address[1],address[2],address[3],address[4],address[5],address[6],address[0])
        return ad.__dict__

    def insert(self, address:EnderecoModel):
        self.cursor.execute("""
            INSERT INTO ENDERECO
            (LOGRADOURO, NUMERO, SIGLA, CIDADE, BAIRRO, CEP) 
            VALUES('{}',{},'{}','{}','{}',{})""".format(address.logradouro, address.numero, address.sigla, address.cidade, address.bairro, address.cep))
        self.connection.commit()
        id = self.cursor.lastrowid
        address.id = id
        return address.__dict__

    def update(self, address:EnderecoModel):
        self.cursor.execute("""
            UPDATE ENDERECO 
                SET 
                    LOGRADOURO = '{}',
                    NUMERO = {},
                    SIGLA = '{}',
                    CIDADE = '{}',
                    BAIRRO = '{}',
                    CEP = {}
                WHERE ID = {}
         """.format(address.logradouro, address.numero, address.sigla, address.cidade, address.bairro, address.cep, address.id))
        self.connection.commit()
        return address.__dict__

    def remove(self, id):
        self.cursor.execute("DELETE FROM ENDERECO WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido o endereco de id: {}'.format(id)




    
