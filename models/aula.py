from models.database.database import func, db, Column, String, Integer, Date, ForeignKey, Enum

from models.turma import Turma
from models.experimento import Experimento
from models.usuario import Usuario
from models.reagente import Reagente


class Aula(db.Model):
    __tablename__ = "aula"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data_aula = Column(Date, nullable=False)
    planejada_efetivada = Column(Enum('Planejada', 'Efetivada'), nullable=False)
    turma_cod = Column(ForeignKey("turma.cod"), nullable=False)
    professor_matricula = Column(ForeignKey("usuario.matricula"), nullable=False)
    experimento_id = Column(Integer, ForeignKey("experimento.id"), nullable=False) 
    
    professor = db.relationship('Usuario')
    experimento = db.relationship('Experimento')
    turma = db.relationship('Turma')

    def __init__(self, nome: str, data_aula: str, planejada_efetivada: str, turma: Turma, professor: Usuario, experimento: Experimento):
        if planejada_efetivada != 'Planejada' and planejada_efetivada != 'Efetivada':
            raise ValueError("'planejada_efetivada' não pode ser diferente de 'Planejada' ou 'Efetivada'")

        self.__verificar_tipo_usuario(professor)
        
        self.nome = nome
        self.turma = turma
        self.data_aula = data_aula
        self.professor = professor
        self.experimento = experimento
        self.planejada_efetivada = planejada_efetivada

    def cadastrar(self): 
        db.session.add(self)
        if self.planejada_efetivada == 'planejada':
            db.session.commit()
        else:
            self.efetivar_aula_planejada()
    
    def efetivar_aula_planejada(self, alunos_faltantes: int = 0):
        experimento_concreto = Experimento(self.experimento.nome, self.experimento.path_pdf)
        experimento_concreto.ideal_concreto = "concreto"
        
        for reagente in self.experimento.reagentes:
            experimento_concreto.reagentes.append(reagente)
            if reagente.status == 'planejado':
                novo_reagente = Reagente(reagente.estado_materia, reagente.concentracao, reagente.massa, reagente.volume, reagente.formula_quimica, reagente.local, reagente.data_validade, reagente.data_criacao)
                novo_reagente.cadastrar()
            else:
                experimento_concreto.reagentes[len(experimento_concreto.reagentes) - 1].experimento_reagente.massa = reagente.experimento_reagente.massa
            
            if reagente.status == "planejado":
                reagente.status = None
              
            reagente.massa -= reagente.experimento_reagente.massa
          
        self.planejada_efetivada = "efetivada"
        db.session.add_all([self.experimento, experimento_concreto])
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_aulas = Aula.query.all()
        return lista_aulas

    def editar(self, novo_nome: str, nova_data: str, planejada_efetivada: str, nova_turma: Turma, novo_professor: Usuario, novo_experimento: Experimento):
        self.planejada_efetivada = planejada_efetivada
        self.nome = novo_nome
        self.data_aula = nova_data
        self.planejada_efetivada = planejada_efetivada
        self.turma = nova_turma
        self.professor = novo_professor
        self.experimento = novo_experimento
        
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()
    
    def __verificar_tipo_usuario(self, usuario: object):
        if usuario.tipo_usuario != 'Professor':
            raise ValueError("Somente professores podem registrar uma aula.")
    
    def __somar_massa_reagentes_aula(self) -> dict:
        tipos_reagente = {}
        
        for reagente in self.experimento.reagentes:
            if reagente.formula_quimica in tipos_reagente:
                tipos_reagente[reagente.formula_quimica] += reagente.massa
            else:
                tipos_reagente[reagente.formula_quimica] = reagente.massa
        return tipos_reagente
    
    def __somar_massa_reagentes_aulas_anteriores(self) -> dict:
        # a implementação desta função é feita de modo a incluir apenas reagentes que existam na aula atual
        aulas_anteriores = Aula.query.filter(Aula.data_aula < self.data_aula).all()
        somatorio_massa_tipos_reagente_aulas_anteriores = {}

        for aula_anterior in aulas_anteriores:
            # percorre uma lista que contém todas as aulas anteriores
            for reagente_aula_anterior in aula_anterior.experimento.reagentes:
                # percorre uma lista que contém todos os reagentes da aula anterior
                for reagente_aula_atual in self.experimento.reagentes:
                    # percorre uma lista com todos os reagentes da aula atual
                    if reagente_aula_atual.formula_quimica == reagente_aula_anterior.formula_quimica:
                        # verifica se o reagente da aula anterior que está sendo percorrido também existe na lista de reagentes da aula atual
                        if reagente_aula_anterior.formula_quimica in somatorio_massa_tipos_reagente_aulas_anteriores:
                            somatorio_massa_tipos_reagente_aulas_anteriores[reagente_aula_anterior.formula_quimica] += reagente_aula_anterior.experimento_reagente.massa
                            break
                        else:
                            somatorio_massa_tipos_reagente_aulas_anteriores[reagente_aula_anterior.formula_quimica] = reagente_aula_anterior.experimento_reagente.massa
                            break
        return somatorio_massa_tipos_reagente_aulas_anteriores
    
    def __somatorio_massa_reagentes_sistema(self, lista_reagentes: list) -> dict:
        somatorio_massa_reagentes_sistema = {}
        
        for formula_quimica in lista_reagentes:
            massa_reagentes = db.session.query(func.sum(Reagente.massa)).filter(Reagente.formula_quimica == formula_quimica and Reagente.status != 'deletado' and Reagente.status != 'planejado').scalar()
            somatorio_massa_reagentes_sistema[formula_quimica] = massa_reagentes
        return somatorio_massa_reagentes_sistema
    
    def __verificar_disponibilidade_aula(self) -> bool:
        somatorio_massa_reagentes_aulas_anteriores = self.__somar_massa_reagentes_aulas_anteriores()
        somatorio_massa_tipos_reagente_aula_atual = self.__somar_massa_reagentes_aula()
        lista_reagentes = [formula for formula in somatorio_massa_tipos_reagente_aula_atual]
        somatorio_massa_tipos_reagente_disponiveis_sistema = self.__somatorio_massa_reagentes_sistema(lista_reagentes)
        
        for formula_quimica in somatorio_massa_tipos_reagente_disponiveis_sistema:
            if (somatorio_massa_tipos_reagente_disponiveis_sistema[formula_quimica] - somatorio_massa_reagentes_aulas_anteriores) < somatorio_massa_tipos_reagente_aula_atual[formula_quimica]:
                return False
        return True
        