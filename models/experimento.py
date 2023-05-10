from models.database.database import db, Column, String, Integer, SmallInteger, ForeignKey, Boolean

class Experimento(db.Model):
    __table__ = "experimento"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    

    def __init__(self):
        pass

    def cadastrar(self):
        pass

    @staticmethod
    def listar():
        pass

    def editar(self):
        pass

    def deletar(self):
        pass