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
        # Nome, ano e likes estao na superclasse
        # logo, posso chamar o super passando essas coisas
        # chamo o inicializador(init) da classe mae (super)
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


'''
    Estou com a ideia de transformar tudo em uma playlist de likes, com filmes e series.
'''
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
# print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao}: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
# print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas}: {atlanta.likes}')

'''
    O filme e um programa
    A serie e um programa

    logo, posso fazer uma lista de programa que contem filmes e series. O python nao e apegado a tipos,
    entao e mais facil de colocar objetos diferentes em uma lista, mas a preocupacao com os tipos deve ser
    mantido, para nao termos erros
'''
# Crio a lista com meus programas
meus_programas = [vingadores, atlanta]

# Escrevo nome duracao e quantidade de likes
# for programa in meus_programas:
#    print(f'{programa.nome}, - {programa.temporadas}: {programa.likes}')

'''
    O Codigo a cima gera um erro, afinal quando o objeto for atlanta programa.temporadas vai retornar a quantidade
    de temporadas. Mas quando o objeto for vingadores não vai existir programa.temporadas, porque vingadores e
    um filme, ele tem duracao e nao temporadas.
    
    Vou fazer um novo if usando a funcao hasattr que recebe um obj, o nome de um atributo e confere se esse obj tem
    ou nao esse atributo
    
    tambem usarei um if ternario:
'''

for programa in meus_programas:
    # Duracao = programa.duracao se o objeto tiver duracao, senao ele recebe programa.temporadas
    descricao = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas

    print(f'{programa.nome}, duracao de {descricao} e tem {programa.likes} likes')
