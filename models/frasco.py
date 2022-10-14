from models.database.database import db, Column, Integer, Numeric, ForeignKey, Date
from models.reagente import Reagente

class Frasco(db.Model):
    """
    Representa a entidade ``frasco`` no banco de dados.

    Frascos contém um reagente e a massa do reagente vai diminuindo conforme 
    vai sendo usado para criar soluções durante as aulas.
    """
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
    def listar(tipo_filtro:str, valor_filtro:str) -> list:
        """
        Retorna uma lista dos frascos registrados no banco de dados de acordo com o filtro e um valor.

        ``tipo_filtro``: uma string que determina por qual atributo a consulta deve ser filtrada,
        as opções são: massa e data-validade. Caso este parâmetro seja passado com um valor diferente
        dos especificados acima a função retorna uma lista com todos os frascos registrados.

        a busca pelo filtro de 'massa' retorna todos os frascos cujo reagente contido nele tenha
        massa igual ou maior que o específicado na busca.

        a busca pelo filtro de 'data-validade' retorna todos os frascos cujo reagente contido nele tenha
        data de validade menor ou igual a data especificada na busca.

        ``valor_filtro``: uma string com o valor que será usado como argumento para realizar a busca. 
        """
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
    def verificar_disponibilidade_reagentes(reagentes:tuple[int, str, float], qtd_alunos:int) -> bool:
        """
        Verifica se existem reagentes em quantidade suficiente para todos
        os alunos em uma aula. O cálculo é feito através de 2 parâmetros:

        ``reagentes``: uma tupla no formato (int, str, float) onde o primeiro
        item da tupla representa a chave primária da tabela ``reagente`` no banco de dados,
        o segundo item representa o estado da matéria na qual se procura obter o reagente e 
        o terceiro item representa a massa em gramas do reagente que será necessária por aluno.

        ``qtd_alunos``: um número inteiro que representa a quantidade de alunos
        que participam da aula.

        A função retorna ``True`` caso existam reagentes em quantidade suficiente para
        todos os alunos, caso contrário retorna ``False``. 
        """
        for reagente in reagentes:
            massa_minima_reagente = qtd_alunos * reagente[2]
            massa_total_reagente_contido_frasco = 0
            frascos = Frasco.query(Frasco).join(Reagente, Frasco.reagente == Reagente.id).filter(Frasco.reagente == reagente[0]).filter(Reagente.estado_materia == reagente[1]).filter(Frasco.massa_reagente != 0).all()  
            
            for frasco in frascos:
                massa_total_reagente_contido_frasco += frasco.massa_reagente
            if(massa_total_reagente_contido_frasco < massa_minima_reagente):
                return False
        
        return True