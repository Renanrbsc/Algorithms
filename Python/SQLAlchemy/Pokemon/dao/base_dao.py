# -- Importando Biblioteca SQLAlchemy
import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


# -- Criando classe que representa a nossa conexão e sessão, (acessa o nosso banco de dados)
class BaseDao:
    # -- Criando método construtor que define as configuração de conexao
    def __init__(self):
        # -- criando engine e passando a configuração de acesso
        # -- formato de string (SGBD+conector://user:passwd@url:port/database)
        conexao = db.create_engine("mysql+mysqlconnector://padawans16:lr2019@mysql.padawans.dev:3306/padawans16")
        # -- Criando variável com o tipo de sessao do DataBase
        criar_sessao = db.orm.sessionmaker()
        # -- Configurando a nossa conexao na sessao
        criar_sessao.configure(bind=conexao)
        # -- definindo objeto de acesso a classe
        self.sessao = criar_sessao()

    def get(self, Model, id=None)-> list:
        if id:
            return self.sessao.query(Model).filter(Model.id == id).one()
        return self.sessao.query(Model).all()

    def insert(self, Model)-> str:
        self.sessao.add(Model)
        self.sessao.commit()
        self.sessao.close()
        return 'Adicionado com sucesso!'

    def update(self, new_update, id)-> str:
        self.sessao.merge(new_update)
        self.sessao.commit()
        self.sessao.close()
        return f'Atualizado ID {id} da tabela'

    def remove(self, search, id)-> str:
        self.sessao.delete(search)
        self.sessao.commit()
        self.sessao.close()
        return f'Removido a ID {id} da tabela'
