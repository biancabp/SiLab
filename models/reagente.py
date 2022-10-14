from models.database.database import db, Column, String, Integer, Numeric, Enum, ForeignKey

class Reagente(db.Model):
    """
    Representa a entidade ``regaente`` no banco de dados.
    """
    __tablename__ = "reagente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    estado_materia = Column(Enum, nullable=False)
    densidade = Column(Numeric, nullable=False)
    formula_quimica = Column(ForeignKey('formula_quimica.formula'), nullable=False)

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
    def listar(tipo_filtro:str, valor_filtro:str) -> list:
        if(tipo_filtro == "estado-materia"):
            lista_reagentes = Reagente.query.filter_by(estado_materia=valor_filtro).all()
        elif(tipo_filtro == "nome"):
            lista_reagentes = Reagente.query.filter(Reagente.nome.startswith(valor_filtro)).all()
        else:
            lista_reagentes = Reagente.query.all()
        return lista_reagentes

    def editar(self, novo_id:int, novo_nome:str, novo_estado_materia:str, nova_densidade:float, nova_formula_quimica:object):
        self.id = novo_id
        self.nome = novo_nome
        self.estado_materia = novo_estado_materia
        self.densidade = nova_densidade
        self.formula_quimica = nova_formula_quimica.formula
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()