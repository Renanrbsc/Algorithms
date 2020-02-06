import MySQLdb


class ProdutoDao:
    def __init__(self, table='PRODUTO'):
        host = ''
        database = ''
        user = database
        passwd = ''
        self.table = table
        self.connection = MySQLdb.connect(host=host, database=database, user=user, passwd=passwd)
        self.cursor = self.connection.cursor()

    def get_all(self):
        self.cursor.execute(f"""SELECT * FROM {self.table}""")

    def get_by_id(self, id):
        self.cursor.execute(f"""SELECT * FROM {self.table} where ID = {id}""")
