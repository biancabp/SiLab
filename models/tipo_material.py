from models.database.database import db, Column, String, Integer

class TipoMaterial(db.Model):
    __tablename__ = 'tipo_material'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)

    def __init__(self, id:int, nome:str):
        self.id = id
        self.nome = nome

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def listar():
        lista_tipos_material = TipoMaterial.query.all()
        return lista_tipos_material

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()