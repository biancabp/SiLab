from models.database.database import Column, ForeignKey
from models.usuario import Usuario

class Professor(Usuario):
    """
    Representa a entidade 'professor' no banco de dados.
    """

    __tablename__ = "professor"
    matricula = Column(ForeignKey("usuario.matricula"), primary_key=True)

    def __init__(self, matricula:int, nome:str, email:str, senha:str):
        super().__init__(matricula, nome, email, senha)

    @staticmethod
    def listar() -> list:
        lista_professores = Professor.query.all()
        return lista_professores
    
    __mapper_args__ = {
        "polymorphic_identity": "professor",
    }