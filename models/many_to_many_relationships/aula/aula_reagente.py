from models.database.database import db, Column, Numeric, ForeignKey

class AulaReagente:

    aula = Column(ForeignKey('aula.id'), primary_key=True)
    reagente = Column(ForeignKey('reagente.id'), primary_key=True)
    massa = Column(Numeric)

    def __init__(self, aula:int, reagente:int, massa:float):
        self.aula = aula
        self.reagente = reagente
        self.massa = massa
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()
    
    def listar(self):
        pass

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()