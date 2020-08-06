import random


def jogar():
    imprime_msg_abertura()
    palavra_secreta = carrega_palavra_screta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcado = False
    acertou = False
    erros = 0

    while (not enforcado and not acertou):

        chute = pergunta_letra()

        if (chute in palavra_secreta):
            merca_letra_correta(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            # print("Errou! Faltam {} tentativas".format(6 - erros))

        enforcado = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_msg_ganhador()
    else:
        imprime_msg_perdedor(palavra_secreta)
    imprime_msg_termino()


def imprime_msg_ganhador():
    """
    Imprime mensagem caso o jogador ganhe
    """
    # print("Você ganhou! :D")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_msg_perdedor(palavra_secreta):
    """
    Imprime mensagem caso o jogador perca
    """
    # print("Perdeu! D:")
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________         ")
    print("    /               \       ")
    print("   /                 \      ")
    print("/\/                   \/\  ")
    print("\ |   XXXX     XXXX   | /   ")
    print(" \|   XXXX     XXXX   |/     ")
    print("  |   XXX       XXX   |      ")
    print("  |                   |      ")
    print("  \__      XXX      __/     ")
    print("    |\     XXX     /|       ")
    print("    | |           | |        ")
    print("    | I I I I I I I |        ")
    print("    |  I I I I I I  |        ")
    print("    \_             _/       ")
    print("      \_         _/         ")
    print("        \_______/           ")


def imprime_msg_termino():
    """
    Imprime mensagem de termino do jogo
    """
    print("Fim do jogo")


def imprime_msg_abertura():
    """
    Imprime mensagem de inicio do jogo
    """
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


#
def carrega_palavra_screta():
    """
    Esta funcao abre o arquivo palavras.txt, cria uma lista de palavras a partir do arquivo
    e sorteia uma das palavras da lista aleatoriamente.

    Retorna a palavra sorteada.
    """
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    nro = random.randrange(0, len(palavras))
    palavra_secreta = palavras[nro].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    """
    Esta funcao recebe uma certa palavra e retorna uma lista onde cada caractere da
    palavra é substituido por um underline, cifrando a palavra recebida.

    Recebe: palavra a ser cifrada.
    Retorna: list com as letras cifradas.
    """
    return ["_" for letra in palavra]


def pergunta_letra():
    """
    Essa funcao serve para perguntar a letra que o usuario quer chutar
    e fazer as adequacoes para que essa letra seja testada.

    Retorna: letra chutada pelo usuario.
    """
    chute = input("Qual letra?")
    chute = chute.strip().upper()

    return chute


def merca_letra_correta(chute, letras_acertadas, palavra_secreta):
    """
    Essa funcao marca a letra correta no lugar correto.

    Recebe: letra para buscar, letras certas e palavra secreta
    """
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
