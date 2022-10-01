class AbstractClassError(Exception):
    """
    Define uma exceção de classe abstrata.

    Ao tentar instânciar um objeto a partir de uma classe abstrata um erro será emitido.
    
    Esta exceção foi criada para resolver um conflito de meta-classes que impediu a definição
    de classes abstratas através da classe nativa do Python 'ABC' e o uso da ORM 'flask-sqlAlchemy' em uma mesma classe.
    """
    pass