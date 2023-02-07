from models.database.database import db, Column, String

class TipoEquipamento(db.Model):
    __tablename__ = "tipo_equipamento"

    nome = Column(String(100), primary_key=True)

    def __init__(self, nome:str):
        """
        ``nome``: str | nome do tipo de material.
        """
        self.nome = nome

    def cadastrar(self):
        """
        Faz o registro do novo tipo de equipamento no banco de dados.
        """
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def listar():
        """
        Retorna uma lista contendo todos os tipos de equipamento registrados no banco de dados.
        """
        lista_tipos_material = TipoEquipamento.query.all()
        return lista_tipos_material

    def editar(self, novo_nome:str):
        """
        Modifica o nome do item no banco de dados.
        """
        self.nome = novo_nome
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        """
        Deleta o registro do item no banco de dados.
        """
        db.session.delete(self)
        db.session.commit()