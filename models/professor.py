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
    def listar(tipo_filtro:str = None, valor_filtro:str = None) -> list:
        """
        Retorna uma lista de professores do banco de dados.

        ``tipo_filtro``: str | O campo pelo qual a busca será filtrada.
        ``valor_filtro``: str | O valor que será usado como parâmetro no filtro durante a consulta.
        """
        if(tipo_filtro == "nome"):
            lista_professores = Professor.query.filter(Professor.nome.startswith(valor_filtro)).all()

        elif(tipo_filtro == "matricula"):
            lista_professores = Professor.query.filter(Professor.matricula.startswith(valor_filtro)).all()

        else:
            lista_professores = Professor.query.all()
            
        return lista_professores
    
    @staticmethod
    def autorizar_professor(usuario:object) -> bool:
        """
        Realiza a autorização de usuário verificando se o mesmo pertence a tabela
        de ``professores`` no banco de dados.

        ``usuario``: object | Representa um usuário no banco de dados.
        """
        if(Professor.query.get(str(usuario.matricula)) == None):
            return False
        return True
    
    __mapper_args__ = {
        "polymorphic_identity": "professor",
    }