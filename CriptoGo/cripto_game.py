# Imports----------------------------------------
import string
import random

# Globais----------------------------------------
# Quantidade de letras do alfabeto
quant_letras_alfbto = 26

# quantidade de linhas criptografadas
linhas_criptografia = 3

# Caractere de partida tabela ascii
min_ascii = 33

# Caractere final tabela ascii
max_ascii = 127


# Principal--------------------------------------
def play():
    chave = cria_matriz_inicial()
    menu(chave)


# Criacao da matriz------------------------------
def cria_matriz_inicial():
    """
        A ideia aqui e criar uma lista de listas para ser nossa matriz
        a primeira linha eh composta por letras do alfabeto, as outras
        duas sao compostas pelos simbulos. O tipo de objeto e char.
    """
    # Crio a lista de chars escolhidos
    chars_escolhidos = []

    # Crio a matriz chave
    chave = []

    # Crio uma lista contendo o alfabeto
    alfabeto = list(string.ascii_uppercase)

    # Jogo a lista contendo o alfabeto para a chave
    # isto e, para a primeira linha da matriz
    chave.append(alfabeto)

    # Agora crio as outras tres linhas contendo chars aleatorios
    for i in range(linhas_criptografia):
        # crio a linha vazia
        linha = []

        for j in range(quant_letras_alfbto):
            # preencho 26 espacos, cada espaco com um char sorteado
            linha.append(chr(sorteia_char(chars_escolhidos)))

        # Coloco minha linha na matriz
        chave.append(linha)

    return chave


def sorteia_char(chars_escolhidos):
    """
        Essa funcao sorteia um char para preencher uma posicao
        na lista de chars sorteados. Cada char nessa lista
        precisa ser unico.
    """
    achei_repetido = False

    # gero um aleatorio entre 33 e 254
    char_secreto = random.randrange(min_ascii, max_ascii)

    # confiro se ele já foi escolhido
    # isto e, se esta na lista de escolhidos
    if char_secreto in chars_escolhidos:
        # se algum item da lista for igual o char_secreto
        # achei repetido se torna verdadeiro
        achei_repetido = True

    # Se achei algum repetido, sorteio de novo
    # senão coloco na lista de chars que ja escolhi
    # e retorno ele para fazer parte da matriz
    if achei_repetido:
        return sorteia_char(chars_escolhidos)
    else:
        chars_escolhidos.append(char_secreto)
        return char_secreto


def escreve_matriz(chave):
    """
        Essa funcao escreve a matriz criptografia na tela
    """
    count = 0
    for y in chave:
        print(y)
        count += 1

        # conto os elementos de 0 a 26, quando chegar a 26
        # zero o contador e quebro a linha
        if count == quant_letras_alfbto:
            count = 0
            print('\n')


# Cria o menu
def menu(chave):
    """
        Essa funcao cria o menu com suas opcoes
    """
    sair = False
    opt = 0

    while not sair:
        print('\n')
        print('------------------------------')
        print('---------- CriptaGo ----------')
        print('------------------------------')
        print('------ 1-Criptografar --------')
        print('------ 2-Descriptografar -----')
        print('---------- 3-Matriz ----------')
        print('-----------  4-Sair ----------')
        print('------------------------------')

        try:
            opt = int(input())
        except:
            opt = 0

        if opt == 1:
            criptografar(chave)
        elif opt == 2:
            descriptografar(chave)
        elif opt == 3:
            escreve_matriz(chave)
        elif opt == 4:
            sair = True
            print('Saindo...')
        else:
            print('Opção inválida!')


def criptografar(chave):
    """
        Essa funcao recebe a chave e criptografa a mensagem
        usando ela
    """
    msg = input('Insira sua mensagem: ')
    msg = msg.upper()

    # Crio uma lista vazia que conterá cada letra da msg
    letras_msg = []

    # Coloco as letras da msg na lista
    letras_msg[:0] = msg

    # Crio a lista para receber as letras apos a criptografia
    cripto_msg = []

    # Para cada letra da msg
    for letra in letras_msg:
        achou = False
        m = 0
        # Vou procurando qual sua posicao no alfabeto (linha 0 da matriz)
        while not achou:
            if letra == chave[0][m]:
                # Quando achar salvo sua posicao
                # sorteio um valor de 1 a 3 correspondedo a quantidade de
                # linhas com simbulos
                # adiciono o simbulo sorteado na lista critografada
                coluna = m
                linha = random.randrange(1, linhas_criptografia)
                cripto_msg.append(chave[linha][coluna])
                achou = True

            # Se nao achei busco o proximo elemento
            m += 1

            # Se a letra encontrada for um espaco
            # adiciono o espaco na posicao
            if letra == ' ':
                cripto_msg.append(' ')
                achou = True

    # Escrevo a msg criptografada
    print('Mensagem criptografada:')
    print(''.join(cripto_msg))


def descriptografar(chave):
    """
        Descriptografa a mensagem informada de acordo com a
        chave recebida
    """
    msg = input('Insira sua mensagem: ')

    # Crio uma lista vazia que conterá cada char da msg
    char_msg = []

    # Coloco os chars da msg na lista
    char_msg[:0] = msg

    # Crio a lista para receber as letras apos a descriptografia
    descripto_msg = []

    # Para cada letra da mensagem
    for char in char_msg:
        achou = False

        # Ignoro a linha 0 da chave, visto que e o alfabeto
        linha = 1

        # Comeco da coluna 0 para frente
        coluna = 0

        # Enquanto nao achou
        while not achou:

            # Se a coluna for 26, tenho que ir para a linha de baixo
            # e recomeçar a contagem coluna por coluna
            if coluna == quant_letras_alfbto:
                linha += 1
                coluna = 0

            # Se o char que procuro for igual o char da chave
            if char == chave[linha][coluna]:
                # acrescento o elemento que pertence a mesma coluna do char, mas da linha 0
                # que e a letra do alfabeto que corresponde ao caractere selecionado
                descripto_msg.append(chave[0][coluna])
                achou = True

            # Se a letra encontrada for um espaco
            # adiciono o espaco na posicao
            if char == ' ':
                descripto_msg.append(' ')
                achou = True

            # Senão busco no proximo elemento
            coluna += 1

    # Escrevo a msg criptografada
    print('Mensagem descriptografada:')
    print(''.join(descripto_msg))


# Inicia o app-----------------------------------
if __name__ == "__main__":
    play()
