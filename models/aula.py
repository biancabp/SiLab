from models.database.database import db, Column, String, Integer, Date, ForeignKey
from models.usuario import Usuario

class Aula(db.Model):
    """
    Representa a entidade ``aula`` no banco de dados. 
    """
    __tablename__ = "aula"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    turma = Column(ForeignKey("turma.cod"))
    data_aula = Column(Date)
    descricao = Column(String(500))
    professor = Column(ForeignKey("usuario.matricula"))
    roteiro = Column(ForeignKey("roteiro.id"))

    def __init__(self, id:int, turma:object, data:object, descricao:str, professor:object):
        """
           ``id``: int | Atributo numérico identificador 
            
           ``turma``: object | Objeto da classe 'Turma' que está relacionado com a aula 

           ``data``: object | Data em que a aula foi registrada
           
           ``descricao``: object | Um texto que descreve as atividades realizadas na aula 

           ``professor``: object | Objeto da classe 'Usuario' que representa o professor que ministrou a aula.
        """
        self.id = id
        self.turma = turma.cod
        self.data_aula = str(data)
        self.descricao = descricao
        self.professor = professor.matricula
    
    def cadastrar(self):
        """
        Realiza a inserção da aula no banco de dados.
        """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar(tipo_filtro:str = None, valor_filtro:str = None) -> list:
        """
        Realiza uma consulta no banco de dados que retorna as aulas registradas com base em um filtro.
        Caso o nada seja passado para o parâmetro ``tipo_filtro`` a função retorna uma lista com todas as aulas.
        """
        if(tipo_filtro == "turma"):
            lista_aulas = db.session.query(Aula, Usuario.nome).join(Usuario, Aula.professor == Usuario.matricula).filter_by(turma=valor_filtro).all()
        elif(tipo_filtro == "professor"):
            lista_aulas = db.session.query(Aula, Usuario.nome).join(Usuario, Aula.professor == Usuario.matricula).filter_by(professor=valor_filtro).all()
        else:
            lista_aulas = db.session.query(Aula, Usuario.nome).join(Usuario, Aula.professor == Usuario.matricula).all()
        return lista_aulas

    def editar(self, nova_turma:object, nova_data:object, nova_descricao:str, novo_professor:object):
        """
        Edita os atributos da aula no banco de dados.
        """
        self.turma = nova_turma.cod
        self.data_aula = str(nova_data)
        self.descricao = nova_descricao
        self.professor = novo_professor.matricula
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        """
        Remove o registro da aula do banco de dados.
        """
        db.session.delete(self)
        db.session.commit()