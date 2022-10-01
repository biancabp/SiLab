from models.database.database import db, Column, String, Integer
from models.exceptions.exceptions import AbstractClassError

class Usuario(db.Model):
    """
    Classe abstrata 'Usuario'

    Representa a entidade 'usuario' no banco de dados, ela é a classe base
    para a especialização das entidades 'professor' e 'tutor', portanto esta classe
    não deve ser instânciada em nenhum momento durante a aplicação.

    Caso tente instânciar esta classe uma exceção do tipo AbstractClassError será emitida.
    """
    __tablename__ = "usuario"

    matricula = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String(50), nullable=False)
    senha = Column(String(64), nullable=False)

    def __init__(self, matricula:int, nome:str, senha:str):
        if(str(type(self)) == "<class '"+__name__+".Usuario'>"):
            raise AbstractClassError("'Usuario' é uma classe abstrata e não pode ser instânciada")
        
        self.matricula = matricula
        self.nome = nome
        self.senha = senha    

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    def listar(self):
        pass
    
    def editar(self, nova_matricula:int, novo_nome:str, nova_senha:str):
        self.matricula = nova_matricula
        self.nome = novo_nome
        self.senha = nova_senha
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()