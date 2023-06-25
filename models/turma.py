from models.database.database import db, Column, String, SmallInteger, Enum


class Turma(db.Model):
    __tablename__ = "turma"

    cod = Column(String(10), primary_key=True)
    ano = Column(String(1), nullable=False)
    turno = Column(Enum('Matutino', 'Vespertino', 'Noturno'), nullable=False) 
    curso = Column(String(100), nullable=False)
    qtd_alunos = Column(SmallInteger(60), nullable=False)

    def __init__(self, cod: str, ano: str, turno: str, curso: str, qtd_alunos: int):
        self.cod = cod
        self.ano = ano
        self.turno = turno
        self.curso = curso
        self.qtd_alunos = qtd_alunos

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_turmas = Turma.query.all()
        return lista_turmas

    def editar(self, novo_cod: str, novo_ano: str, novo_turno: str, novo_curso: str, nova_qtd_alunos: int):
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
        