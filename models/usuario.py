from abc import ABC, abstractmethod
from database.database import *

class Usuario(ABC, db.Model):
    matricula = Column(Integer, primary_key=True, autoincrement=False)
    nome = Column(String(50))

    def __init__(self, matricula:int, nome:str):
        self.matricula = matricula
        self.nome = nome

    @abstractmethod
    def cadastrar(self):
        pass

    @abstractmethod
    def listar(self):
        pass
    
    @abstractmethod
    def editar(self):
        pass

    @abstractmethod
    def deletar(self):
        pass