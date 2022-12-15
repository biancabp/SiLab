from models.database.database import db, Column, Numeric, ForeignKey

class AulaReagente:

    aula = Column(ForeignKey('aula.id'), primary_key=True)
    reagente = Column(ForeignKey('reagente.id'), primary_key=True)
    massa = Column(Numeric)

    def __init__(self, aula:int, reagente:int, massa:float):
        self.aula = aula
        self.reagente = reagente
        self.massa = massa
        return self
    
    def relacionar(self, db:object):
        db.session.add(self)
    
    @staticmethod
    def listar(aula:int):
        lista_reagentes = AulaReagente.query.filter(aula=aula).all()
        return lista_reagentes

    def deletar(self):
        db.session.delete(self)
        db.session.commit()