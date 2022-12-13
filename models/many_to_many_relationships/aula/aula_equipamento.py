from models.database.database import db, Column, ForeignKey

class AulaEquipamento:

    aula = Column(ForeignKey('aula.id'), primary_key=True)
    equipamento = Column(ForeignKey('equipamento.id'), primary_key=True)

    def __init__(self, aula:int, equipamento:int):
        self.aula = aula
        self.equipamento = equipamento
    
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