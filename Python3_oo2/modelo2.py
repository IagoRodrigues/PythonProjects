class Programa:
    def __init__(self, nome, ano):
        # Atributos que usam dois underline no inicio do nome
        # sao privados. Como o __nome por exemplo.
        # Esse atributo nao pode ser herdado, visto que ele
        # e privado.
        # Deixar dessa forma vai dar um erro, dizendo que Filme
        # nao tem o atributo _Programa__likes.
        #
        # Uma saida seria colocar _Programa__likes ou
        # _Programa__nome, dizendo para o python qual atributo buscar na
        # classe mae, mas isso seria complicado, teria que ser feito para todos
        # os atributos privados, logo, surge uma convencao:
        # usar somente um underline.
        #
        # Isso quebra a validacao do python e mostra para os outros programadores
        # que o atributo eh privado. Ficaremos com _nome e _likes, dando a ideia de
        # protegido mas nao privado, entao:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Posso criar getters usando uma função com o mesmo nome do atributo
    # e adicionar a notação @property
    # assim quando fizer objeto.atributo ele chama o getter, não o atributo de fato
    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome:  {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome:  {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
