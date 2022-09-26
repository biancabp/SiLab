from usuario import Usuario
from database.database import db

class Tutor(Usuario):
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar():
        lista_tutores = Tutor.query.all()
        return lista_tutores

    def editar(self, nova_matricula, novo_nome):
        self.matricula = nova_matricula
        self.nome = novo_nome
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()
