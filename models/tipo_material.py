from models.database.database import db, Column, String, Integer

class TipoMaterial:
    __tablename__ = 'tipo_material'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

    def __init__(self, id:int, nome:str):
        self.id = id
        self.nome = nome

    def cadastrar(self):
        pass
    
    @staticmethod
    def listar():
        pass

    def editar(self):
        pass

    def deletar(self):
        pass
