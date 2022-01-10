class Funcionario:
    """
        Classe pai
        Cria os metodos registra_horas e mostrar_tarefas
    """

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    """
        Classe filho
        Herda da classe pai (Caelum eh um Funcionario)
        Cria o metodo busca_cursos_do_mes e sobreescreve o mostrar_tarefas
    """

    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    """
        Classe filho
        Herda da classe pai (Alura eh um Funcionario)
        Cria o metodo busca_perguntas_sem_resposta e sobreescreve o mostrar_tarefas
    """

    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Junior(Alura):
    """
        Classe filho
        Herda da classe pai (Junior eh um Alura)
    """
    pass


class Pleno(Alura, Caelum):
    """
        Classe filho
        Herda das duas classes pais (Junior eh um Alura e é um Caelum)
    """
    pass


# Crio os objetos:

func_junior = Junior()
func_pleno = Pleno()

'''
func_junior tem os metodos:

registra_horas -> de Funcionario
mostrar_tarefas -> de Funcionario
mostrar_tarefas -> de Alura
busca_perguntas_sem_resposta -> de Alura

Ele tem duas imprementacoes do metodo mostrar_tarefas, uma vinda de funcionario(vo) e uma vinda de alura(pai)
ele busca a implementacao mais proxima de si na arvore, logo, usa a do pai:
func_junior.mostrar_tarefas() retorna "Fez muita coisa, Alurete!"

func_pleno tem os metodos:

registra_horas -> de funcionario
mostrar_tarefas -> de Funcionario
busca_cursos_do_mes -> de Caelum
mostrar_tarefas -> de Caelum
mostrar_tarefas -> de Alura
busca_perguntas_sem_resposta -> de Alura

Ele tem tres imprementacoes do metodo mostrar_tarefas, uma vinda de funcionario(vo), uma vinda de alura(pai) e uma
vinda de caelum(pai)
ele busca a implementacao mais proxima de si na arvore, logo, usa a de um dos pais:

func_pleno.mostrar_tarefas() retorna "Fez muita coisa, Alurete!" ou "Fez muita coisa, Caelumer"

O python usa o MRO (method resolution order), ele vai da esquerda para direita verificando as classes citadas como maes 
e sempre que ele puxa uma classe mae, ele puxa os antepassados dessa classe junto, ou seja:

Busca o metodo em pleno > se não achar puxa a classe mae mais a esquerda > puxa Alura > Como puxou Alura, puxa a classe
mae de alura tambem > puxa Funcionario > se nao achar até agora puxa a outra classe mae, da esquerda para a direita > 
puxa Caelum > Como puxou Caelum, puxa a classe mae de Caelum tambem > puxa Funcionario e assim vai

Só que o MRO busca repetir o minimo possivel as classes a serem chamadas, para melhorar a busca, logo, a classe 
funcionario (que se repete) deve ser chamada uma vez so. Para isso o MRO consulta a hierarquia de classes para chamar
cada uma somente uma vez
'''
func_pleno.mostrar_tarefas()