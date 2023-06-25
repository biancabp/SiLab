from models.database.database import db, Column, String, Integer, Date, Numeric, ForeignKey
from models.reagente import Reagente

uso_diverso_reagente_reagente = db.Table('uso_diverso_reagente_reagente',
         Column('uso_diverso_reagente_id', Integer, ForeignKey('uso_diverso_reagente.id')),
         Column('reagente_id', Integer, ForeignKey('reagente.id')),
         Column('massa', Numeric)
         )


class UsoDiversoReagente(db.Model):
    __tablename__ = "uso_diverso_reagente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_uso = Column(Date, nullable=False)
    descricao = Column(String(500), nullable=True)
    
    reagentes = db.relationship('Reagente', secondary=uso_diverso_reagente_reagente, lazy='joined')

    def __init__(self, data_uso: object, descricao: str, reagentes: list[Reagente, int]):
        self.data_uso = data_uso
        self.descricao = descricao
        
        for reagente, massa_utilizada in reagentes:
            self.reagentes.append(reagente)
            self.reagentes.uso_diverso_reagente.massa = massa_utilizada
            reagente.massa -= massa_utilizada    
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def listar():
        usos_diversos_reagentes = UsoDiversoReagente.query.all()
        return usos_diversos_reagentes

    def editar(self, nova_data_uso: str, nova_descricao: str):
        self.data_uso = nova_data_uso
        self.descricao = nova_descricao
        
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()
        