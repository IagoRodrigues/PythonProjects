import random


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")  # Abro o arquivo palavras para leitura
    palavras = []  # Crio uma lista de palavras

    for linha in arquivo:
        linha = linha.strip()  # Recebo uma linha e tiro espaços e \n
        palavras.append(linha)  # Jogo a palavra para a lista de palavras

    arquivo.close()  # Fecho o arquivo

    nro = random.randrange(0, len(palavras))  # Sorteio um numero aleatório

    palavra_secreta = palavras[nro].upper()  # Pego a palavra selecionada aleatoriamente
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcado = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcado and not acertou:

        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Errou! Faltam {} tentativas".format(6 - erros))

        enforcado = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou! :D")
    else:
        print("Perdeu! D:")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
