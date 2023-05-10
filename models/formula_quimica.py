from models.database.database import db, Column, String

class FormulaQuimica(db.Model):
    """
    Representa um registro da entidade ``formula_quimica`` no banco de dados.
    """
    __tablename__ = "formula_quimica"

    formula = Column(String(30), primary_key=True)
    nome = Column(String(50), nullable=False)

    def __init__(self, formula:str, nome:str):
        """
        ``formula``: Uma string que representa uma fórmula química, ex: H2O.
        """
        self.formula = formula
        self.nome = nome
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_formulas = FormulaQuimica.query.all()
        return lista_formulas
        
    def editar(self, nova_formula:str, novo_nome:str):
        self.formula = nova_formula
        self.nome = novo_nome
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()