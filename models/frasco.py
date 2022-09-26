from database.database import * 

class Frasco(db.Model):
    def __init__(self, id:int, volume:float, reagente: object):
        self.id = id
        self.voluma = volume
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