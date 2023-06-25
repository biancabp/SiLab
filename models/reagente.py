from models.database.database import db, Column, String, Integer, Numeric, Enum, ForeignKey, Date
from datetime import datetime


class Reagente(db.Model):
    __tablename__ = "reagente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    estado_materia = Column(Enum('Sólido', 'Líquido', 'Gasoso'), nullable=False)
    concentracao = Column(Numeric, nullable=True)
    massa = Column(Numeric, nullable=False)
    volume = Column(Numeric, nullable=False)
    data_validade = Column(Date, nullable=True)
    data_criacao = Column(Date, nullable=True)
    local = Column(String(3), nullable=False)
    formula_quimica = Column(ForeignKey('formula_quimica.formula'), nullable=False)
    status = Column(Enum('deletado', 'planejado'), nullable=True)

    def __init__(self, estado_materia: str, concentracao: float, massa: float, volume: float, formula_quimica: str, local: str, data_validade: object = None, data_criacao: str = None, status: str = None):
        self.estado_materia = estado_materia
        self.concentracao = concentracao
        self.massa = massa
        self.volume = volume
        
        if data_validade is not None:
            self.data_validade = datetime.strptime(data_validade, '%Y-%m-%d').date()
        if data_criacao is not None:
            self.data_criacao = datetime.strptime(data_criacao, "%Y-%m-%d").date()
        
        self.formula_quimica = formula_quimica
        self.local = local
        self.status = status
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_reagentes = Reagente.query.filter(Reagente.status is None).all()
        return lista_reagentes

    def editar(self, novo_estado_materia: str, nova_concentracao: float, nova_massa: float, novo_volume: float, nova_formula_quimica: str, novo_local: str, nova_data_validade: str = None, nova_data_criacao: str = None, novo_status: str = None):
        self.estado_materia = novo_estado_materia
        self.concentracao = nova_concentracao
        self.massa = nova_massa
        self.volume = novo_volume
        self.formula_quimica = nova_formula_quimica
        self.local = novo_local
        
        if nova_data_validade is not None:
            self.data_validade = datetime.strptime(nova_data_validade, '%Y-%m-%d').date()
        if nova_data_criacao is not None:
            self.data_criacao = datetime.strptime(nova_data_criacao, "%Y-%m-%d").date()
        
        self.status = novo_status

        db.session.add(self)
        db.session.commit()

    def deletar(self):
        self.status = "deletado"
        db.session.add(self)
        db.session.commit()
            