from models.database.database import db, Column, String, Integer, SmallInteger, ForeignKey

class Material(db.Model):
    __tablename__ = "material"

    id = db.Column(Integer, primary_key=True)
    localizacao = Column(String(100), nullable=False)
    qtd = db.Column(SmallInteger, nullable=False)
    volume = Column(SmallInteger, nullable=False)
    material = Column(String(100), nullable=False)
    tamanho = Column(SmallInteger, nullable=False)
    tipo_material = Column(ForeignKey('tipo_material.id'), nullable=False)
    lugar = Column(String(100), nullable=False)

    def __init__(self, id:int, localizacao:str, qtd:int, volume:float, material:str, tamanho:float, tipo_material:object, lugar:str):
        self.id = id
        self.localizacao = localizacao
        self.qtd = qtd
        self.volume = volume
        self.material = material
        self.tamanho = tamanho
        self.tipo_material = tipo_material
        self.lugar = lugar

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_materiais = Material.query.all()
        return lista_materiais

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()