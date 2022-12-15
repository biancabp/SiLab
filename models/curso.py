from models.database.database import db, Column, String

class Curso(db.Model):
    """
    Representa a entidade 'curso' no banco de dados.
    """
    __tablename__ = "curso"

    nome_curso = Column(String(100), primary_key=True)

    def __init__(self, nome_curso:str):
        self.nome_curso = nome_curso
    
    def cadastrar(self):
        """
        Registra o curso no banco de dados. 
        """
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def listar(nome_curso:str = None) ->list:
        """
        Retorna uma lista com os cursos registrados no banco de dados
        de acordo com o nome do curso.
        
        caso o argumento ``nome_curso`` seja omitido na chamada da função, 
        ``None`` será atribuido por padrão e o retorno será uma lista com 
        todos os cursos registrados.
        """
        if(nome_curso == None):
            lista_cursos = Curso.query.all()
        else:
            lista_cursos = Curso.query.filter(Curso.nome_curso.startswith(nome_curso)).all()
        return lista_cursos
    
    def editar(self, novo_nome_curso:str):
        """
        Modifica o nome do curso.
        
        caso o argumento ``novo_nome_curso`` corresponda ao nome de um curso
        já registrado no banco de dados, uma exceção de erro de integridade 
        será emitida.
        """
        self.nome_curso = novo_nome_curso
        db.session.add(self)
        db.session.commit()
    
    def deletar(self):
        """
        Remove o registro do curso do banco de dados.
        """
        db.session.delete(self)
        db.session.commit()