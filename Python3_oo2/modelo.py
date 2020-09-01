class Filme:
    def __init__(self, nome, ano, duracao):
        """Atributos privados são marcados usando __ no inicio do nome"""
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    """
        Posso criar getters usando uma função com o mesmo nome do atributo
        e adicionar a notação @property
        
        assim quando fizer objeto.atributo ele chama o getter, não o atributo de fato
    """

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome


class Serie:
    """
    Se tivermos um atributo de classe devemos fazer:

    tamanho_dos_ep = 40
    """
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    """
    Na hora de usar:
    
    __class__.tamanho_dos_ep
    """


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome:  {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome:  {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
