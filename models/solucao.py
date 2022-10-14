from models.database.database import db, Column, String, Integer, Numeric, Enum, ForeignKey
from models.aula import Aula

class Solucao(db.Model):
    """Representa a entidade ``solução`` no banco de dados."""
    __tablename__ = "solucao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    autor = Column(String(100))
    aula = Column(ForeignKey("aula.id"))
    formula_quimica = Column(ForeignKey('formula_quimica.formula'))
    estado_materia = Column(Enum)
    densidade = Column(Numeric)
    concentracao = Column(Numeric)

    def __init__(self, id:int, nome:str, autor:str, aula:object, formula_quimica:object, estado_materia:str, densidade:float, concentracao:float, reagentes:list):
        self.id = id
        self.nome = nome
        self.autor = autor
        self.aula = aula.id
        self.formula_quimica = formula_quimica
        self.estado_materia = estado_materia
        self.densidade = densidade
        self.concentracao = concentracao
        self.reagentes = reagentes
    
    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar(tipo_filtro:str, valor_filtro:str):
        if(tipo_filtro == "nome"):
            lista_solucoes = Solucao.query.filter(Solucao.nome.startswith(valor_filtro)).all()
        
        elif(tipo_filtro == "estado-materia"):
            lista_solucoes = Solucao.query.filter_by(estado_materia=valor_filtro).all()
            
        elif(tipo_filtro == "ate-data"):
            lista_solucoes = Solucao.query.join(Aula, Aula.id == Solucao.id).filter(Aula.data <= valor_filtro).all()
        elif(tipo_filtro == "apos-data"):
            lista_solucoes = Solucao.query.join(Aula, Aula.id == Solucao.id).filter(Aula.data >= valor_filtro).all()
        else:
            lista_solucoes = Solucao.query.all()
        return lista_solucoes

    def editar(self, novo_id:int, novo_nome:str, novo_autor:str, nova_formula_quimica:object, novo_estado_materia:str, nova_densidade:float, nova_concentracao:float, novos_reagentes:list):
        self.id = novo_id
        self.nome = novo_nome
        self.autor = novo_autor
        self.formula_quimica = nova_formula_quimica
        self.estado_materia = novo_estado_materia
        self.densidade = nova_densidade
        self.concentracao = nova_concentracao
        self.reagentes = novos_reagentes
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()
