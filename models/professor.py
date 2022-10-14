from models.database.database import Column, ForeignKey
from models.usuario import Usuario

class Professor(Usuario):
    """
    Representa a entidade ``professor`` no banco de dados. 
    """

    __tablename__ = "professor"
    matricula = Column(ForeignKey("usuario.matricula"), primary_key=True)

    def __init__(self, matricula:int, nome:str, email:str, senha:str):
        super().__init__(matricula, nome, email, senha)

    @staticmethod
    def listar(tipo_filtro:str ,valor_filtro:str) -> list:
        if(tipo_filtro == "nome"):
            lista_professores = Professor.query.filter(Professor.nome.startswith(valor_filtro)).all()

        elif(tipo_filtro == "matricula"):
            lista_professores = Professor.query.filter(Professor.matricula.startswith(valor_filtro)).all()

        else:
            lista_professores = Professor.query.all()
            
        return lista_professores
    
    __mapper_args__ = {
        "polymorphic_identity": "professor",
    }