from models.database.database import db, Column, String, Integer, Date, Numeric, ForeignKey

class UsoDiversoReagente:

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_uso = Column(Date)
    massa = Column(Numeric)
    descricao = Column(String(200))
    reagente = Column(ForeignKey('reagente.id'))

    def __init__(self, data_uso:object, massa:float, descricao:str, reagente:int):
        self.data_uso = data_uso
        self.massa = massa
        self.descricao = descricao
        self.reagente = reagente
    
    def cadastrar(self):
        db.session.add()
        db.session.commit()
    
    def listar(self):
        pass

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()