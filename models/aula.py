from database.database import *

class Aula(db.Model):
    """
    Classe Aluno: Esta classe representa um aula no banco de dados. 
    Ela recebe 5 parâmetros em seu construtor que definem: id
    """
    __tablename__ = "aula"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    turma = Column(String(10))
    data = Column(Date)
    descricao = Column(String(500))
    professor = Column(String(100))

    def __init__(self, id:int, turma:object, data:object, descricao:str, professor:object):
        self.id = id
        self.turma = turma.cod
        self.data = data
        self.descricao = descricao
        self.professor = professor.nome
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_aulas = Aula.query.all()
        return lista_aulas

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()