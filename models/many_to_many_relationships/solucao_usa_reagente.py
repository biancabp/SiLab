from models.database.database import db, Column, Numeric, ForeignKey
from sqlalchemy.ext import IntegrityError

class SolucaoUsaReagente(db.Model):
    __tablename__ = "solucao_usa_reagente"

    solucao = Column(ForeignKey("solucao.id"), primary_key=True)
    reagente = Column(ForeignKey("reagente.id"), primary_key=True)
    qtd = Column(Numeric)

    def __init__(self, solucao:object, reagente:object, qtd:float):
        self.solucao = solucao.id
        self.reagente = reagente.id
        self.qtd = qtd
    
    def relacionar(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except IntegrityError:
            return False