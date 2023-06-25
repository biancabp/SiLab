from models.database.database import db, Column, String, Integer, Numeric, Boolean


class Vidraria(db.Model):
    __tablename__ = "vidraria"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), nullable=False)
    material = Column(String(45), nullable=False)
    volume = Column(Numeric, nullable=False)
    local = Column(String(3), nullable=False)
    deletado = Column(Boolean, nullable=False)

    def __init__(self, nome: str, material: str, volume: float, local: str):
        self.nome = nome
        self.material = material
        self.volume = volume
        self.local = local
        self.deletado = False

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        vidrarias = Vidraria.query.all()
        return vidrarias

    def editar(self, novo_nome: str, novo_material: str, novo_volume: float, novo_local: str, deletado: bool):
        self.nome = novo_nome
        self.material = novo_material
        self.volume = novo_volume
        self.local = novo_local
        self.deletado = deletado

        db.session.add(self)
        db.session.commit()

    def deletar(self):
        self.deletado = True
        db.session.add(self)
        db.session.commit()
        