from models.database.database import db, Column, String, Integer, SmallInteger, ForeignKey, Boolean

class Equipamento(db.Model):
    """
    Representa a entidade ``equipamento`` no banco de dados.
    """
    __tablename__ = "equipamento"

    id = db.Column(Integer, primary_key=True)
    qtd = db.Column(SmallInteger, nullable=False)
    tipo_equipamento = Column(ForeignKey('tipo_equipamento.nome'), nullable=False)
    lugar = Column(String(100), nullable=False)
    danificado = Column(Boolean)

    def __init__(self, qtd:int, tipo_equipamento:object, lugar:str, danificado:bool):
        self.qtd = qtd
        self.tipo_equipamento = tipo_equipamento.id
        self.lugar = lugar
        self.danificado = danificado

    def cadastrar(self):
        """
        Faz a inserção do equipamento no banco de dados.
        """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar(valor_filtro:object = None) -> list:
        """
        Retorna uma lista contendo os equipamentos registrados no banco de dados.
        
        A busca pode ser feita usando um filtro de ``tipo de equipamento``, caso
        a busca seja realizada sem filtros então a função retorna uma lista com
        todos os equipamentos registrados no banco de dados.
        """
        if(valor_filtro == None):
            lista_equipamentos = Equipamento.query.all()
        else:    
            lista_equipamentos = Equipamento.query.filter(Equipamento.tipo_equipamento == valor_filtro.id).all()
        return lista_equipamentos

    def editar(self, nova_qtd:int, novo_tipo_equipamento:object, novo_lugar:str, danificado:bool):
        """
        Modifica o valor das propriedades do item no banco de dados.
        """
        self.qtd = nova_qtd
        self.tipo_equipamento = novo_tipo_equipamento.nome
        self.lugar = novo_lugar
        self.danificado = danificado
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        """
        Deleta o registro do equipamento do banco de dados.
        """
        db.session.delete(self)
        db.session.commit()