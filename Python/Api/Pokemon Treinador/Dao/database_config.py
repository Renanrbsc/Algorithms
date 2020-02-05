import MySQLdb

class DatabaseConfig:
    def __init__(self,table):
        #self.connection = MySQLdb.connect(host='127.0.0.1',database='PadawanHBSIS',user='root')
        self.host = 'mysql.padawans.dev'
        self.database = 'padawans16'
        self.user = self.database
        self.passwd = 'lr2019'
        self.table = table
        self.connection = MySQLdb.connect(host=self.host,database=self.database,user=self.user,passwd=self.passwd)
        self.cursor = self.connection.cursor()