from database.database import *

class Turma(db.Model):
    cod = Column(String(10), primary_key=True, autoincrement=False)
    ano = Column(Integer)
    turno = Column(String()) # pesquisar pelo tipo ENUM
    curso = Column(String(50))

    def __init__(self, cod:str, ano:int, turno:str, curso:str):
        self.cod = cod
        self.ano = ano
        self.turno = turno
        self.curso = curso

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar():
        lista_turmas = Turma.query.all()
        return lista_turmas

    def editar(self, novo_cod:str, novo_ano:int, novo_turno:str, novo_curso:str):
        self.cod = novo_cod
        self.ano = novo_ano
        self.turno = novo_turno
        self.curso = novo_curso
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()