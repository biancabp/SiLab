from models.database.database import db, Column, String, Boolean


class FormulaQuimica(db.Model):
    __tablename__ = "formula_quimica"

    formula = Column(String(30), primary_key=True)
    nome = Column(String(100), nullable=False)
    deletado = Column(Boolean, nullable=False)

    def __init__(self, formula: str, nome: str):
        self.formula = formula
        self.nome = nome
        self.deletado = False
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_formulas = FormulaQuimica.query.filter(FormulaQuimica.deletado == False).all()
        return lista_formulas
        
    def editar(self, nova_formula: str, novo_nome: str):
        self.formula = nova_formula
        self.nome = novo_nome
        
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        self.deletado = True
        db.session.add(self)
        db.session.commit()
        