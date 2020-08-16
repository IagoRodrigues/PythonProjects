
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    """
    Com essa sintaxe definimos que o método nome é o getter do atributo __nome
    
    Quando fizermos:
    >>>cliente.nome
    
    Por baixo dos panos o Python vai chamar esse método
    """
    @property
    def nome(self):
        return self.__nome.title()

    """
    Com essa sintaxe definimos o metodo nome como setter do atributo __nome
    
    Quando fizermos:
    >>>cliente.nome = "marco"
    
    Por baixo dos panos o Python vai chamar esse método
    """
    @nome.setter
    def nome(self, nome):
        self.__nome = nome