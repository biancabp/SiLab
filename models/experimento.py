from models.database.database import db, Column, String, Integer, Enum

from models.equipamento import Equipamento
from models.vidraria import Vidraria
from models.reagente import Reagente

experimento_equipamento = db.Table('experimento_equipamento',
         Column('experimento_id', Integer, db.ForeignKey('experimento.id')),
         Column('equipamento_tombo', String(10), db.ForeignKey('equipamento.tombo'))
         )

experimento_vidraria = db.Table('experimento_vidraria',
         Column('experimento_id', Integer, db.ForeignKey('experimento.id')),
         Column('vidraria_id', Integer, db.ForeignKey('vidraria.id'))
         )

experimento_reagente = db.Table('experimento_reagente',
         Column('experimento_id', Integer, db.ForeignKey('experimento.id')),
         Column('reagente_id', Integer, db.ForeignKey('reagente.id')),
         Column('massa', Integer)
         )


class Experimento(db.Model):
    __tablename__ = "experimento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    path_pdf = Column(String(100), nullable=True)
    ideal_concreto = Column(Enum('ideal', 'concreto'), nullable=False)
    
    equipamentos = db.relationship('Equipamento', secondary=experimento_equipamento)
    vidrarias = db.relationship('Vidraria', secondary=experimento_vidraria)
    reagentes = db.relationship('Reagente', secondary=experimento_reagente, lazy="joined")
    
    def __init__(self, nome: str, path_pdf: str = '', equipamentos: list[Equipamento] = [], vidrarias: list[Vidraria] = [], reagentes: list[Reagente, int] = [], reagentes_planejados: list[dict] = {}):
        for reagente_planejado in reagentes_planejados:
            estado_materia, concentracao = reagente_planejado['estado-materia'], reagente_planejado['concentracao']
            massa, volume = reagente_planejado['massa'], reagente_planejado['volume']
            formula_quimica, local = reagente_planejado['formula_quimica'], reagente_planejado['local']
            data_validade, data_criacao = reagente_planejado['data-validade'], reagente_planejado['data-criacao']
            status = reagente_planejado['status']
            
            novo_reagente_planejado = Reagente(estado_materia, concentracao, massa, volume, formula_quimica, data_validade, data_criacao, status)
            db.session.add(novo_reagente_planejado)
            db.session.commit()
            self.reagentes.append(novo_reagente_planejado)
            
        self.nome = nome
        self.path_pdf = path_pdf
        self.ideal_concreto = "ideal"
        
        for equipamento in equipamentos:
            self.equipamentos.append(equipamento)
        
        for vidraria in vidrarias:
            self.vidrarias.append(vidraria)
          
        for reagente, massa_utilizada in reagentes:
            self.reagentes.append(reagente)
            self.reagentes[len(self.reagentes) - 1].experimentp_reagente.massa = massa_utilizada

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar():
        lista_experimentos = Experimento.query.filter(Experimento.ideal_concreto == 'ideal').all()
        return lista_experimentos

    def editar(self, novo_nome: str, path_pdf: str = None, novos_equipamentos: list[Equipamento] = [], novas_vidrarias: list[Vidraria] = [], novos_reagentes: list[Reagente, int] = []):
        self.nome = novo_nome
        self.path_pdf = path_pdf
        
        self.reagentes = []
        self.equipamentos = []
        self.vidrarias = []
        
        for equipamento in novos_equipamentos:
            self.equipamentos.append(equipamento)

        for vidraria in novas_vidrarias:
            self.vidrarias.append(vidraria)

        for reagente, massa_utilizada in novos_reagentes:
            self.reagentes.append(reagente)
            self.reagentes[len(self.reagentes) - 1].experimentp_reagente.massa = massa_utilizada
        
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        if self.ideal_concreto == 'ideal':
            db.session.delete(self)
            db.session.commit()
