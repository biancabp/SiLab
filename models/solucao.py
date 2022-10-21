from models.database.database import db, Column, String, Integer, Numeric, Enum, ForeignKey
from models.aula import Aula
from models.frasco import Frasco
from sqlalchemy.exc import IntegrityError

class Solucao(db.Model):
    """Representa a entidade ``solução`` no banco de dados."""
    __tablename__ = "solucao"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    autor = Column(String(100))
    aula = Column(ForeignKey("aula.id"))
    formula_quimica = Column(ForeignKey('formula_quimica.formula'))
    estado_materia = Column(Enum)
    massa = Column(Numeric)
    densidade = Column(Numeric)

    def __init__(self, id:int, nome:str, autor:str, aula:object, formula_quimica:object, estado_materia:str, densidade:float, frascos:tuple[object, float], massa:float = None):
        """
        ``id``: int | representa o identificador númerico da solução.
        
        ``nome``: string | representa o nome dado a solução.
        
        ``autor``: string | representa o nome do autor da solução.
        
        ``aula``: objeto da classe ``Aula`` | indica a aula na qual a solução foi criada/registrada.
        
        ``formula_quimica``: objeto da classe ``FormulaQuimica`` | indica a fórmula química da solução.
        
        ``estado_materia``: string | representa o estado da matéria da solução.
        
        ``densidade``: float | representa a densidade da solução, a unidade de medida é kg/m³ (quilograma por metro cúbico).
        
        ``frascos``: tuple | contém objetos da classe ``Frasco`` que representam os regentes usados para formar a solução e a massa de reagente que foi usada.
        
        ``massa``: float | representa a massa total da solução.

        obs: ``massa`` é um parâmetro opcional que é inicializado com ``None`` por padrão.
        
        Caso este parâmetro seja omitido então o cálculo da massa da solução será realizado 
        somando a massa dos reagentes usados para compor a solução. Caso ele seja especificado
        então a massa da solução será correspondente ao valor especificado.
        """
        self.id = id
        self.nome = nome
        self.autor = autor
        self.aula = aula.id
        self.formula_quimica = formula_quimica
        self.estado_materia = estado_materia
        self.densidade = densidade
        self.frascos = frascos
        
        if(massa == None):
            self.massa = self.__calcular_massa_total_solucao(self.frascos)
        else:
            self.massa = massa
    
    def cadastrar(self):
        """
        Realiza o registro da solução no banco de dados e seus relacionamentos com a tabela ``reagente``.
        """
        try:
            db.session.add(self)
            Frasco.debitar_massa_reagente_frasco(db, self, self.frascos)
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

    def editar(self, novo_id:int, novo_nome:str, novo_autor:str, nova_formula_quimica:object, novo_estado_materia:str, nova_massa:float, nova_densidade:float, novos_reagentes:list):
        self.id = novo_id
        self.nome = novo_nome
        self.autor = novo_autor
        self.formula_quimica = nova_formula_quimica
        self.estado_materia = novo_estado_materia
        self.massa = nova_massa
        self.densidade = nova_densidade
        self.reagentes = novos_reagentes
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        """
        Remove o registro da solução e de seus relacionamentos do banco de dados.
        """
        db.session.delete(self)
        db.session.commit()
    
    def __calcular_massa_total_solucao(self, frascos:tuple[object, float]):
        """
        Realiza o cálculo da massa total da solução somando a massa de todos os reagentes
        que compõem a ela.
        """
        massa_total_solucao = 0.0
        
        for frasco, massa in frascos:
            massa_total_solucao += massa
        
        return massa_total_solucao