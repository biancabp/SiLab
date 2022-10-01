from models.database.database import db, Column, String

class FormulaQuimica(db.Model):
    """
    Representa um registro da tabela 'formula_quimica' no banco de dados.
    """
    __tablename__ = "formula_quimica"

    formula = Column(String(30), primary_key=True)

    def __init__(self, formula:str):
        """
        formula: Uma string que representa uma fórmula química, ex: H2O.
        """
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