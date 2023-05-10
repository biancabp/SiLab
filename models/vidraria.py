from models.database.database import db, Column, String, Integer,Numeric,SmallInteger, Enum

class Vidraria(db.Model):
    __table__ = "vidraria"

    id = Column(Integer, primary_key=True)
    volume = Column(Numeric, nullable=False)
    material = Column(String(100), nullable=False)
    local = Column(String(3), nullable=False)

    def __init__(self, volume:float, material:str, local:str):
        self.volume = volume
        self.material = material
        self.local = local

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar():
        vidrarias = Vidraria.query.all()
        return vidrarias

    def editar(self, novo_volume:float, novo_material:str, novo_local:str):
        self.volume = novo_volume
        self.material = novo_material
        self.local = novo_local
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        pass