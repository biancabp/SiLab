from flask_login import UserMixin
from models.database.database import db, Column, String, Integer, Enum

class Usuario(db.Model, UserMixin):
    """
    Representa a entidade ``usuario`` no banco de dados

    ``matricula``: int | chave primária da tabela
    """
    __tablename__ = "usuario"

    matricula = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String(50), nullable=False)
    email = Column(String(300), nullable=False)
    senha = Column(String(64), nullable=False)
    tipo_usuario = Column(Enum('Professor', 'Tutor'), nullable=False)

    def __init__(self, matricula:int, nome:str, email:str, senha:str, tipo_usuario:str):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.senha = senha    
        self.tipo_usuario = tipo_usuario

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar(tipo_filtro:str ,valor_filtro:str, tipo_usuario:str) -> list:
        if(tipo_filtro == "nome"):
            lista_usuarios = Usuario.query.filter(Usuario.nome.startswith(valor_filtro)).filter(Usuario.tipo_usuario == tipo_usuario).all()

        elif(tipo_filtro == "matricula"):
            lista_usuarios = Usuario.query.filter(Usuario.matricula.startswith(valor_filtro)).filter(Usuario.tipo_usuario == tipo_usuario).all()

        else:
            lista_usuarios = Usuario.query.all()
            
        return lista_usuarios
    
    def editar(self, nova_matricula:int, novo_nome:str, novo_email:str, nova_senha:str):
        self.matricula = nova_matricula
        self.nome = novo_nome
        self.email = novo_email
        self.senha = nova_senha
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def autorizar_professor(usuario:object) -> bool:
        """
        Realiza a autorização de usuário verificando se o mesmo é do tipo ``professor`` no banco de dados.

        ``usuario``: object | Representa um usuário no banco de dados.
        """
        if(Usuario.query.get(str(usuario.matricula)).tipo_usuario != 'Professor'):
            return False
        return True
    
    def get_id(self):
        return self.matricula