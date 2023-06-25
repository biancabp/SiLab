from models.database.database import db, Column, String, Integer, Date, ForeignKey, Enum

from models.turma import Turma
from models.experimento import Experimento
from models.usuario import Usuario


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
    
    def efetivar_aula_planejada(self):
        experimento_concreto = Experimento(self.experimento.nome, self.experimento.path_pdf)
        experimento_concreto.ideal_concreto = "concreto"
        
        for reagente in self.experimento.reagentes:
            experimento_concreto.reagentes.append(reagente)
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
    