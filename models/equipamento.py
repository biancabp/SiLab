from models.database.database import db, Column, String, Boolean


class Equipamento(db.Model):
    __tablename__ = "equipamento"

    tombo = db.Column(String(10), primary_key=True)
    tipo_equipamento = Column(String(50), nullable=False)
    descricao = Column(String(400), nullable=False)
    local = Column(String(45), nullable=False)
    deletado = Column(Boolean, nullable=False)

    def __init__(self, tombo: str, tipo_equipamento: str, descricao: str, local: str):
        self.tombo = tombo
        self.tipo_equipamento = tipo_equipamento
        self.descricao = descricao
        self.local = local
        self.deletado = False

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_equipamentos = Equipamento.query.filter(Equipamento.deletado == False).all()
        return lista_equipamentos

    def editar(self, novo_tombo: str, novo_tipo_equipamento: str, nova_descricao: str, novo_local: str):
        self.tombo = novo_tombo
        self.tipo_equipamento = novo_tipo_equipamento
        self.descricao = nova_descricao
        self.local = novo_local
        
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        self.deletado = True
        db.session.add(self)
        db.session.commit()
        