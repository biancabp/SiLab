from models.database.database import db, Column, Integer, Numeric, ForeignKey, Date

class Frasco(db.Model):
    __tablename__ = "frasco"

    id = db.Column(Integer, primary_key=True)
    volume = Column(Numeric, nullable=False)
    reagente = Column(ForeignKey('reagente.id'))
    data_validade_reagente = Column(Date)
    massa_reagente = Column(Numeric)

    def __init__(self, id:int, volume:float, reagente: object):
        self.id = id
        self.volume = volume
        self.reagente = reagente

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar():
        lista_frascos = Frasco.query.all()
        return lista_frascos

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def verificar_disponibilidade_reagentes() -> bool:
        pass