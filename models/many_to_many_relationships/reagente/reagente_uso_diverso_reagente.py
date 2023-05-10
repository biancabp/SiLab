from models.database.database import db, Column, Integer, Numeric, ForeignKey

class ReagenteUsoDiversoReagente(db.Model):
    __table__ = "reagente_uso_diverso_reagente"

    id = Column(Integer, primary_key=True)
    reagente = Column(ForeignKey('reagente.id'), nullable=False)
    uso_diverso_reagente = Column(ForeignKey('uso_diverso_reagente.id'), nullable=False)
    massa_utilizada_reagente = Column(Numeric, nullable=False)

    def __init__(self, reagente:int, uso_diverso_reagente:int, massa_utilizada_reagente:float):
        self.reagente = reagente
        self.uso_diverso_reagente = uso_diverso_reagente
        self.massa_utilizada_reagente = massa_utilizada_reagente
    
    def relacionar(self):
        pass

    @staticmethod
    def listar():
        pass

    def editar(self):
        pass

    def deletar(self):
        pass