from models.database.database import db, Column, String, Integer, Numeric, Enum, ForeignKey
from models.aula import Aula
from models.reagente import Reagente
from models.many_to_many_relationships.solucao_usa_reagente import SolucaoUsaReagente
from sqlalchemy.ext import IntegrityError

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

    def __init__(self, id:int, nome:str, autor:str, aula:object, formula_quimica:object, estado_materia:str, densidade:float, frascos:tuple[object, float]):
        """
        ``id``: int | representa o identificador númerico da solução.
        ``nome``: string | representa o nome dado a solução.
        ``autor``: string | representa o nome do autor da solução.
        ``aula``: objeto da classe ``Aula`` | indica a aula na qual a solução foi criada/registrada.
        ``formula_quimica``: objeto da classe ``FormulaQuimica`` | indica a fórmula química da solução.
        ``estado_materia``: string | representa o estado da matéria da solução.
        ```densidade``: float | representa a densidade da solução, a unidade de medida é kg/m³ (quilograma por metro cúbico).
        ``reagentes``: tuple | contém objetos da classe ``Frasco`` que representam os regentes usados para formar a solução.
        """
        self.id = id
        self.nome = nome
        self.autor = autor
        self.aula = aula.id
        self.formula_quimica = formula_quimica
        self.estado_materia = estado_materia
        self.densidade = densidade
        self.frascos = frascos
    
    def cadastrar(self):
        try:
            db.session.add(self)
            for frasco_reagente, massa_reagente in self.frascos:
                frasco_reagente.massa_reagente -= massa_reagente

                if(frasco_reagente.massa_reagente < 0):
                    db.session.rollback()
                    raise ValueError("Os frascos devem conter massa de reagentes suficiente")

                db.session.add(frasco_reagente)
                reagente = Reagente.query.filter(id = frasco_reagente.reagente).all()                
                relacionar_solucao_reagente = SolucaoUsaReagente(self, reagente, massa_reagente)
                relacionar_solucao_reagente.relacionar()
                
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise IntegrityError("Erro de integridade")

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
        self.reagentes = novos_reagentes
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()