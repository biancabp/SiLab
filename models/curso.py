from models.database.database import db, Column, String

class Curso(db.Model):
    __tablename__ = "curso"

    nome_curso = Column(String(100), primary_key=True)

    def __init__(self, nome_curso:str):
        self.nome_curso = nome_curso
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def listar():
        lista_cursos = Curso.query.all()
        return lista_cursos
    
    def editar(self, novo_nome_curso:str):
        self.nome_curso = novo_nome_curso
        db.session.add(self)
        db.session.commit()
    
    def deletar(self):
        db.session.delete(self)
        db.session.commit()