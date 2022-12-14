from models.database.database import db, Column, ForeignKey

class AulaEquipamento:

    aula = Column(ForeignKey('aula.id'), primary_key=True)
    equipamento = Column(ForeignKey('equipamento.id'), primary_key=True)

    def __init__(self, aula:int, equipamento:int):
        self.aula = aula
        self.equipamento = equipamento
        return self
    
    def relacionar(self, db:object):
        db.session.add(self)
    
    @staticmethod
    def listar(aula:int) -> list:
        """
        Lista todos os equipamentos utilizados em uma aula
        """
        lista_equipamentos = AulaEquipamento.query.filter(aula=aula).all()
        return lista_equipamentos
        
    def deletar(self):
        db.session.delete(self)
        db.session.commit()