from models.database.database import db, Column, Numeric, ForeignKey
from sqlalchemy.ext import IntegrityError

class SolucaoUsaReagente(db.Model):
    """
    Representa o relacionamento de cardinalidade muitos-para-muitos entre
    a tabela ``solucao`` e ``reagente`` no banco de dados.
    """
    __tablename__ = "solucao_usa_reagente"

    solucao = Column(ForeignKey("solucao.id"), primary_key=True)
    reagente = Column(ForeignKey("reagente.id"), primary_key=True)
    massa = Column(Numeric)

    def __init__(self, solucao:object, reagente:object, massa:float):
        """
        ``solucao``: object | solução que está se relacionando com o reagente.
        ``reagente``: object | reagente que compõe a solução.
        ``massa``: float | massa dada em gramas(g) que foi usada do reagente.
        """
        self.solucao = solucao.id
        self.reagente = reagente.id
        self.massa = massa
    
    def relacionar(self, db:object):
        """
        ``db``: object | objeto passado por referência que permite a construção de transações no banco de dados.
        """
        try:
            db.session.add(self)
            return True
        except IntegrityError:
            return False