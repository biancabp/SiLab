from models.database.database import db, Column, String, Integer, ForeignKey

class Roteiro(db.Model):
    id = Column(Integer, autoincrement=True)
    descricao = Column(String(200))
    usuario = Column(ForeignKey('usuario.matricula'))
    turma = Column(ForeignKey('turma.cod'))

    def __init__(self, descricao:str, usuario:int, turma:str):
        self.descricao = descricao

    def cadastrar(self):
        pass

    @staticmethod
    def listar(self):
        pass

    def editar(self):
        pass

    def deletar(self):
        pass