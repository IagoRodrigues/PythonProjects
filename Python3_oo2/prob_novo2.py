class Funcionario:
    """
    Vou criar um mixin

    Mixins sao classes extremamente especificas que sao herdadas para agregar um funcionamento para as classes
    que as herdarem.

    No caso vou criar um mixin para escrever o nome do funcionario:

    1) Defino que meus funcionarios tem o atributo nome
    """

    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class MostraNome:
    """
    2) Crio o mixin (classe mega especifica) com um unico metodo escrevendo nome
    """

    def __str__(self):
        return f'Meu nome eh {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, MostraNome):
    """
    Herdo o mixin onde quero utilizar
    """
    pass


jose = Junior('José')
jose.busca_perguntas_sem_resposta()
jose.mostrar_tarefas()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()
print(luan)