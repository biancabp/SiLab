from flask_login import UserMixin
from models.database.database import db, Column, String, Enum


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuario"

    matricula = Column(String(10), primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(60), nullable=False)
    senha = Column(String(64), nullable=False)
    tipo_usuario = Column(Enum('Professor', 'Tutor'), nullable=False)

    def __init__(self, matricula: str, nome: str, email: str, senha: str, tipo_usuario: str):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.senha = senha    
        self.tipo_usuario = tipo_usuario

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_usuarios = Usuario.query.all()
        return lista_usuarios
    
    def editar(self, nova_matricula: int, novo_nome: str, novo_email: str, nova_senha: str, tipo_usuario: str):
        self.matricula = nova_matricula
        self.nome = novo_nome
        self.email = novo_email
        self.senha = nova_senha
        self.tipo_usuario = tipo_usuario

        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def autorizar_professor(matricula: str) -> bool:
        """
        Realiza a autorização de usuário verificando se o mesmo é do tipo ``professor`` no banco de dados.
        """
        if Usuario.query.get({"matricula": matricula}).tipo_usuario != 'Professor':
            return False
        return True
    
    def get_id(self):
        return self.matricula
    