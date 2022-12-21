from models.database.database import db, Column,  Numeric, Enum, ForeignKey

class AulaSolucao:

    aula = Column(ForeignKey('aula.id'), primary_key=True)
    solucao = Column(ForeignKey('solucao.id'), primary_key=True)
    massa = Column(Numeric)
    criada_utilizada = Column(Enum('Criada', 'Utilizada'))

    def __init__(self, aula:int, solucao:int, massa:float, criada_utilizada:str):
        self.aula = aula
        self.solucao = solucao
        self.massa = massa
        self.criada_utilizada = criada_utilizada
        return self
    
    def relacionar(self, db:object):
        db.session.add(self)

    @staticmethod
    def listar(aula:int) -> list:
        lista_solucoes = AulaSolucao.query.filter(aula=aula).all()
        return lista_solucoes

    def deletar(self):
        db.session.delete(self)
        db.session.commit()