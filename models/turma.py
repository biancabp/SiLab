from models.database.database import db, Column, String, SmallInteger, Enum, ForeignKey

class Turma(db.Model):
    __tablename__ = "turma"

    cod = Column(String(10), primary_key=True)
    ano = Column(SmallInteger)
    turno = Column(Enum) 
    curso = Column(ForeignKey("curso.nome_curso"))
    qtd_alunos = Column(SmallInteger)

    def __init__(self, cod:str, ano:int, turno:str, curso:str, qtd_alunos:int):
        self.cod = cod
        self.ano = ano
        self.turno = turno
        self.curso = curso
        self.qtd_alunos = qtd_alunos

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar(tipo_filtro:str, valor_filtro:str) -> list:
        if(tipo_filtro == "curso"):
            lista_turmas = Turma.query.filter_by(curso=valor_filtro).all()
        
        elif(tipo_filtro == "turno"):
            lista_turmas = Turma.query.filter_by(turno=valor_filtro).all()
        
        elif(tipo_filtro == "ano"):
            lista_turmas = Turma.query.filter_by(ano=valor_filtro).all()
        
        elif(tipo_filtro == "cod"):
            lista_turmas = Turma.query.filter_by(cod=valor_filtro).all()

        else:
            lista_turmas = Turma.query.all()
        
        return lista_turmas

    def editar(self, novo_cod:str, novo_ano:int, novo_turno:str, novo_curso:str, nova_qtd_alunos:int):
        self.cod = novo_cod
        self.ano = novo_ano
        self.turno = novo_turno
        self.curso = novo_curso
        self.qtd_alunos = nova_qtd_alunos
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()