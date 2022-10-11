from models.database.database import db, Column, Integer, Numeric, ForeignKey, Date

class Frasco(db.Model):
    __tablename__ = "frasco"

    id = db.Column(Integer, primary_key=True)
    volume = Column(Numeric, nullable=False)
    reagente = Column(ForeignKey('reagente.id'))
    data_validade_reagente = Column(Date)
    massa_reagente = Column(Numeric)

    def __init__(self, id:int, volume:float, reagente:object, data_validade_reagente:object, massa_reagente:float):
        self.id = id
        self.volume = volume
        self.reagente = reagente.id
        self.data_validade_reagente = data_validade_reagente
        self.massa_reagente = massa_reagente

    def cadastrar(self):
        """
        Realiza a inserção do frasco no banco de dados.
        """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar(tipo_filtro:str, valor_filtro:str):
        if(tipo_filtro == "massa"):
            valor_filtro = float(valor_filtro)
            lista_frascos = Frasco.query.filter(Frasco.massa_reagente >= valor_filtro).all()
        
        elif(tipo_filtro == "data-validade"):
            lista_frascos = Frasco.query.filter(Frasco.data_validade <= valor_filtro).all()
        
        else:    
            lista_frascos = Frasco.query.all()
        
        return lista_frascos

    def editar(self, novo_id:int, novo_volume:float, novo_reagente:object, nova_data_validade_reagente:object, nova_massa_reagente:float):
        """
        Modifica os atributos do objeto frasco e reflete as alterações no banco de dados.
        """
        self.id = novo_id
        self.volume = novo_volume
        self.reagente = novo_reagente
        self.data_validade_reagente = nova_data_validade_reagente
        self.massa_reagente = nova_massa_reagente
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        """
        Remove o registro do frasco do banco de dados.
        """
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def verificar_disponibilidade_reagentes(frascos_reagentes:dict, qtd_alunos:int) -> bool:
        pass
        """for massa in frascos_reagentes:
            frasco = """