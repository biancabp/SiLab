from database.database import *

class FormulaQuimica(db.Model):
    formula = Column(String(50), primary_key=True)

    def __init__(self, formula:str):
        self.formula = formula
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_formulas = FormulaQuimica.query.all()
        return lista_formulas
        
    def editar(self, nova_formula:str):
        self.formula = nova_formula
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()