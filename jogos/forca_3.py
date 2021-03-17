def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maca".upper()

    '''
    Para fazer a quantidade de letras se adaptar de acordo com a palavra, eu primeiro
    declarei a lista vazia, depois montei um laço que preenche a lista com "_" para
    cada letra:
    
    letras_acertadas = []
    
    for letra in palavra_secreta:
        letras_acertadas.append("_")
        
    mas o python possui um recurso chamado list comprehensions que permite fazer:
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    ou seja, inicializar a variável com um laço já preenchendo tudo. Incrível! 
    '''

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
