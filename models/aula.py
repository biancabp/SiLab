from models.database.database import db, Column, String, Integer, Date, ForeignKey, Enum, Boolean
from models.usuario import Usuario
from models.reagente import Reagente
from models.solucao import Solucao

from models.many_to_many_relationships.aula.aula_equipamento import AulaEquipamento
from models.many_to_many_relationships.aula.aula_reagente import AulaReagente
from models.many_to_many_relationships.aula.aula_solucao import AulaSolucao
from models.many_to_many_relationships.solucao.solucao_usa_reagente import SolucaoUsaReagente

class Aula(db.Model):
    """
    Representa a entidade ``aula`` no banco de dados. 
    """
    __tablename__ = "aula"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    turma = Column(ForeignKey("turma.cod"))
    data_aula = Column(Date)
    roteiro = Column(String(500))
    professor = Column(ForeignKey("usuario.matricula"))
    planejada_efetivada = Column(Enum('Planejada', 'Efetivada'))
    deletada = Column(Boolean)

    def __init__(self, turma:object, data:object, roteiro:str, professor:object, planejada_efetivada:str, equipamentos:list = None, reagentes:list = None, solucoes:list = None):
        """
           ``id``: int | Atributo numérico identificador 
            
           ``turma``: object | Objeto da classe 'Turma' que está relacionado com a aula 

           ``data``: object | Data em que a aula foi registrada
           
           ``roteiro``: object | Um texto que descreve as atividades realizadas na aula 

           ``professor``: object | Objeto da classe 'Usuario' que representa o professor que ministrou a aula.

           ``planejada_efetivada``: string | Informa se a aula se encontra em estágio de planejamento ou se foi executada.
        """
        if(planejada_efetivada != 'Planejada' and planejada_efetivada != 'Efetivada'):
            raise ValueError("'planejada_efetivada' não pode ser diferente de 'Planejada' ou 'Efetivada'")

        self.__verificar_tipo_usuario(professor)
        
        self.turma = turma.cod
        self.data_aula = str(data)
        self.roteiro = roteiro
        self.professor = professor.matricula
        self.planejada_efetivada = planejada_efetivada

    def cadastrar_aula(self, equipamentos:list = None, reagentes:list = None, solucoes_criadas:list = None, solucoes_utilizadas:list = None, solucoes_criadas_utilizadas:list = None):
        """
        Realiza a inserção da aula no banco de dados.
        """
        try:
            db.session.add(self)
            db.session.commit()
            id_aula = [row[0] for row in db.session.execute("select LAST_INSERT_ID()")]
            
            for equipamento in equipamentos:
                AulaEquipamento(id_aula[0], equipamento.id).relacionar(db)
            
            for reagente in reagentes:
                AulaReagente(id_aula[0], reagente.id, reagente.massa).relacionar(db)
            
            for solucao, reagentes in solucoes_criadas:
                nova_solucao = Solucao(solucao.nome, solucao.autor, solucao.formula_quimica, solucao.estado_materia, solucao.densidade, solucao.massa, solucao.concentracao, solucao.deleta_planejado)
                id_nova_solucao = nova_solucao.cadastrar(reagentes, id_aula)
                AulaSolucao(id_aula[0], id_nova_solucao, 'Criada', solucao.massa).relacionar(db)
            
            for solucao, massa in solucoes_utilizadas:
                AulaSolucao(id_aula[0], solucao, 'Utilizada', massa).relacionar(db)

            for solucao, reagentes in solucoes_criadas_utilizadas:
                nova_solucao = Solucao(solucao[0].nome, solucao[0].autor, solucao[0].formula_quimica, solucao[0].estado_materia, solucao[0].densidade, solucao[0].massa, solucao[0].concentracao, solucao[0].deleta_planejado)
                id_nova_solucao = nova_solucao.cadastrar(reagentes, id_aula)
                AulaSolucao(id_aula[0], id_nova_solucao, 'Ambos', solucao.massa).relacionar(db)


            if self.planejada_efetivada == "Efetivada":
                Reagente.debitar_massa_reagente(db, reagentes)
                Solucao.debitar_massa_solucoes(db, solucoes_utilizadas)

                for solucao, reagentes in solucoes_utilizadas:
                    Solucao.debitar_massa_solucoes(db, solucoes_criadas_utilizadas)
                Solucao.debitar_massa_solucoes(db, solucoes_criadas_utilizadas)
           
            db.session.commit()

        except:
            db.session.rollback()
            db.session.delete(Aula.query.get(id_aula[0]))
            db.session.commit()
    
    def efetivar_aula_planejada(self):
        try:
            if self.planejada_efetivada == 'Planejada':
                self.planejada_efetivada = 'Efetivada'
                db.session.add(self)
                reagentes_utilizados_aula = db.session.query(Reagente, AulaReagente.massa).join(AulaReagente).filter(AulaReagente.aula == self.id).all()
                solucoes_utilizadas_aula = db.session.query(Solucao, AulaSolucao.massa).join(AulaSolucao).filter(AulaSolucao.aula == self.id).all()
                reagentes_solucoes = db.session.query(Reagente, SolucaoUsaReagente.massa).join(SolucaoUsaReagente).join(AulaSolucao).filter(AulaSolucao.aula == self.id).filter(AulaSolucao.criada_utilizada == 'Criada' or AulaSolucao.criada_utilizada == 'Ambos').all()

                Reagente.debitar_massa_reagente(db, reagentes_utilizados_aula)
                Reagente.debitar_massa_reagente(db, reagentes_solucoes)
                Solucao.debitar_massa_solucoes(db, solucoes_utilizadas_aula)

                solucoes = db.session.query(Solucao).join(AulaSolucao).filter(AulaSolucao.aula == self.id).filter(Solucao.deletado_planejado == 'Planejado').all()
                for solucao in solucoes:
                    solucao.deletado_planejado == None
                    db.session.add(solucao)
                db.session.commit()
       
        except Exception:
            db.session.rollback()
            raise ValueError("O campo 'planejada_efetivada' deve ser igual a 'Efetivada'")

    @staticmethod
    def listar(tipo_filtro:str = None, valor_filtro:str = None) -> list:
        """
        Realiza uma consulta no banco de dados que retorna as aulas registradas com base em um filtro.
        Caso o nada seja passado para o parâmetro ``tipo_filtro`` a função retorna uma lista com todas as aulas.
        """
        if(tipo_filtro == "turma"):
            lista_aulas = db.session.query(Aula, Usuario.nome).join(Usuario, Aula.professor == Usuario.matricula).filter_by(turma=valor_filtro).all()
        elif(tipo_filtro == "professor"):
            lista_aulas = db.session.query(Aula, Usuario.nome).join(Usuario, Aula.professor == Usuario.matricula).filter_by(professor=valor_filtro).all()
        else:
            lista_aulas = db.session.query(Aula, Usuario.nome).join(Usuario, Aula.professor == Usuario.matricula).all()
        return lista_aulas

    def editar(self, nova_turma:object, nova_data:object, novo_roteiro:str, novo_professor:object, planejada_efetivada:str):
        """
        Edita os atributos da aula no banco de dados.
        """
        self.turma = nova_turma.cod
        self.data_aula = str(nova_data)
        self.roteiro = novo_roteiro
        self.professor = novo_professor.matricula
        self.planejada_efetivada = planejada_efetivada
        db.session.add(self)
        db.session.commit()

    def deletar(self):
        """
        Remove o registro da aula do banco de dados.
        """
        try:
            self.deletada = True
            db.session.add(self)
            db.session.commit()
        except:
            pass
    
    def __verificar_tipo_usuario(self, usuario:object):
        if(usuario.tipo_usuario != 'Professor'):
            raise ValueError("Somente professores podem registrar uma aula.")
    
    #def __efetivar_aula()