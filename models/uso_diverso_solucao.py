from models.database.database import db, Column, String, Integer, Date, Numeric, ForeignKey
from models.solucao import Solucao

class UsoDiversoSolucao(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_uso = Column(Date)
    massa = Column(Numeric)
    descricao = Column(String(200))
    solucao = Column(ForeignKey('solucao.id'))

    def __init__(self, data_uso:object, massa:float, descricao:str, solucao:object):
        self.data_uso = data_uso
        self.massa = massa
        self.descricao = descricao
        self.solucao = solucao.id
    
    def cadastrar(self):
        db.session.add()
        Solucao.debitar_massa_solucoes(db, [(self.solucao, self.massa)])
        db.session.commit()
    
    @staticmethod
    def listar(solucao:int = None) -> list:
        if solucao != None:
            lista_uso_diveros_solucao = UsoDiversoSolucao.query.filter(UsoDiversoSolucao.solucao == solucao)
            return lista_uso_diveros_solucao

        lista_uso_diveros_solucao = UsoDiversoSolucao.query.all()
        return lista_uso_diveros_solucao

    def editar(self, nova_data_uso, nova_massa:float, nova_descricao:str, nova_solucao:int):
        self.data_uso = nova_data_uso
        self.massa = nova_massa
        self.descricao = nova_descricao
        self.solucao = nova_solucao
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()