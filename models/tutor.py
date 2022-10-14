from models.database.database import Column, ForeignKey
from models.usuario import Usuario

class Tutor(Usuario):
    """
    Representa a entidade ``tutor`` no banco de dados.
    """
    __tablename__ = "tutor"

    matricula = Column(ForeignKey("usuario.matricula"), primary_key=True)

    def __init__(self, matricula:str, nome:str, senha:str):
        super().__init__(matricula, nome, senha)

    @staticmethod
    def listar(tipo_filtro:str ,valor_filtro:str) -> list:
        if(tipo_filtro == "nome"):
            lista_tutores = Tutor.query.filter(Tutor.nome.startswith(valor_filtro)).all()

        elif(tipo_filtro == "matricula"):
            lista_tutores = Tutor.query.filter(Tutor.matricula.startswith(valor_filtro)).all()

        else:
            lista_tutores = Tutor.query.all()
            
        return lista_tutores

    __mapper_args__ = {
        "polymorphic_identity": "tutor",
    }