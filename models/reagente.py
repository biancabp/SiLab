from database.database import *

class Reagente(db.Model):
    def __init__(self, id:int, nome:str, estado_materia:str, densidade:float, formula_quimica:object):
        self.id = id
        self.nome = nome
        self.estado_materia = estado_materia
        self.densidade = densidade
        self.formula_quimica = formula_quimica
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_reagentes = Reagente.query.all()
        return lista_reagentes

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()