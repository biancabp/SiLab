from models.database.database import db, Column, String, Integer, Numeric, Enum, ForeignKey, Date, Boolean
from datetime import datetime

class Reagente(db.Model):
    """
    Representa a entidade ``regaente`` no banco de dados.
    """
    __tablename__ = "reagente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    estado_materia = Column(Enum('Sólido', 'Líquido', 'Gasoso'), nullable=False)
    densidade = Column(Numeric, nullable=False)
    concentracao = Column(Numeric)
    massa = Column(Numeric, nullable=False)
    volume = Column(Numeric, nullalbe=False)
    data_validade = Column(Date, nullable=True)
    data_criacao = Column(Date, nullalbe=True)
    local = Column(String(3), nullable=False)
    formula_quimica = Column(ForeignKey('formula_quimica.formula'), nullable=False)
    deletado = Column(Boolean, nullable=False)

    def __init__(self, estado_materia:str, densidade:float, massa:float, volume:float, data_validade:object, formula_quimica:object, local:str, deletado:bool = False):
        self.estado_materia = estado_materia
        self.densidade = float(densidade)
        self.massa = float(massa)
        self.volume = float(volume)
        self.data_validade = datetime.strptime(data_validade, '%Y-%m-%d').date()
        self.formula_quimica = formula_quimica
        self.local = local
        self.deletado = deletado
    
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

    def editar(self, novo_estado_materia:str, nova_densidade:float, nova_massa:float, novo_volume:float, nova_data_validade:str, nova_formula_quimica:str, novo_local:str):
        self.estado_materia = novo_estado_materia
        self.densidade = nova_densidade
        self.massa = nova_massa
        self.volume = novo_volume
        self.data_validade = datetime.strptime(nova_data_validade, '%Y-%m-%d').date()
        self.formula_quimica = nova_formula_quimica
        self.local = novo_local
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        self.deletado = True
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def debitar_massa_reagente(db:object, reagentes:list):
        for reagente, massa_utilizada in reagentes:
            reagente.massa -= massa_utilizada
            db.session.add(reagente)