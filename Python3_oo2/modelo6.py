"""
    Para mais detalhes e comentarios:
    ver modelo 5
"""


# Definicao da classe Mae de todos----------------------------------------------------------------------------------


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

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

    def __str__(self):
        return f'{self.nome} - {self.ano}: {self.likes}'


# Definicao das classes filhas------------------------------------------------------------------------------------------


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} dura {self.duracao} minutos e tem {self.likes} likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} dura {self.temporadas} temporadas e tem {self.likes} likes'


# Outras Classes--------------------------------------------------------------------------------------------------------


class Playlist:
    '''
        Representa minha playlist de programas.
        Essa classe possui nome, list de programas e tamanho (tamanho do list de programas)

    '''
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

# Contato com o usuario-------------------------------------------------------------------------------------------------


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

pr = Filme('Pacific Rim', 2016, 120)
pr.dar_like()
pr.dar_like()
pr.dar_like()

tmoc = Serie('Todo mundo odeia o Cris', 1986, 4)
tmoc.dar_like()
tmoc.dar_like()
tmoc.dar_like()

rambo = Filme('Rambo', 1996, 90)
rambo.dar_like()
rambo.dar_like()
rambo.dar_like()

pkb = Serie('Peaky Blinders', 2020, 4)
pkb.dar_like()
pkb.dar_like()
pkb.dar_like()

# Adiciono meu programas na lista
meus_programas = [vingadores, atlanta, pr, tmoc, rambo, pkb]

# Crio minha playlist
playlist_do_iago = Playlist("Minha Play", meus_programas)

# Percorro minha playlist
# O codigo abaixo nao funciona, eu obtenho: TypeError: 'Playlist' object is not iterable
# Isso acontece pq playlist_do_iago nao eh uma lista (nao eh um iteravel) e sim um obj que
# possui um iteravel dentro. Uma maneira de corrigir eh usando:
# for programa in playlist_do_iago.programas
# mas isso nao eh bom, visto que eu tenho que conhecer a classe e conhecer a estrutura interna dela para
# poder fazer funcionar
for programa in playlist_do_iago:
    print(programa)
