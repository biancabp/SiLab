from models.database.database import db, Column, String, Integer, Date, Numeric, ForeignKey
from models.reagente import Reagente

class UsoDiversoReagente(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_uso = Column(Date, nullable=False)
    massa = Column(Numeric, nullalbe=False)
    descricao = Column(String(200), nullable=True)
    reagente = Column(ForeignKey('reagente.id'), nullable=False)

    def __init__(self, data_uso:object, massa:float, descricao:str, reagente:object):
        self.data_uso = data_uso
        self.massa = massa
        self.descricao = descricao
        self.reagente = reagente.id
    
    def cadastrar(self):
        db.session.add()
        Reagente.debitar_massa_reagente(db, [(self.reagente, self.massa)])
        db.session.commit()
    
    @staticmethod
    def listar():
        usos_diversos_reagentes = UsoDiversoReagente.query.all()
        return usos_diversos_reagentes

    def editar(self, nova_data_uso, nova_massa, nova_descricao, novo_reagente):
        self.data_uso = nova_data_uso
        self.massa = nova_massa
        self.descricao = nova_descricao
        self.reagente = novo_reagente
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()