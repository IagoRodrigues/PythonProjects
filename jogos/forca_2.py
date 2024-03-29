def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcado = False
    acertou = False

    print(letras_acertadas)

    while not enforcado and not acertou:

        chute = input("Qual letra?")

        index = 0
        # Para cada variavel letra dentro de palavra_secreta faça:
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                # print("Encontrei a letra {} na posição {}".format(chute, index+1))
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
