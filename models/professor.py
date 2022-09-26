from usuario import Usuario
from database.database import db

class Professor(Usuario):
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_professores = Professor.query.all()
        return lista_professores

    def editar(self, nova_matricula:int, novo_nome:str):
        self.matricula = nova_matricula
        self.nome = novo_nome
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()