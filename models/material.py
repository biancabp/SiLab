from database.database import *

class Material(db.Model):
    def __init__(self, id:int, localizacao:str, qtd:int, volume:float, material:str, tamanho:float, tipo_material:object, lugar:str):
        self.id = id
        self.localizacao = localizacao
        self.qtd = qtd
        self.volume = volume
        self.material = material
        self.tamanho = tamanho
        self.tipo_material = tipo_material
        self.lugar = lugar

    def cadastrar(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def listar() -> list:
        lista_materiais = Material.query.all()
        return lista_materiais

    def editar(self):
        pass

    def deletar(self):
        db.session.delete(self)
        db.session.commit()