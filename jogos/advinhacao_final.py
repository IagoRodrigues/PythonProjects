import random


def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de advinhação")
    print("*******************************")

    nro_secreto = random.randrange(1, 101)  # de 1 a 100
    pontos = 1000

    print("Qual dificuldade você deseja?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        # print("Rodada", rodada, "de", total_de_tentativas)
        print("Rodada {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        # Python usa and e or
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue
            # Da mesma forma que o break interrompe o laço, o continue
            # interrompe o código e volta para a linha do for, aumentando
            # um valor, ou seja: o continue pula para a próxima iteração

        acertou = nro_secreto == chute
        maior = nro_secreto < chute
        menor = nro_secreto > chute

        if acertou:
            print("Você acertou e fez {} pontos!!!".format(pontos))
            break
        else:
            if maior:
                print("Chutou alto!!")
            elif menor:
                print("Chutou Baixo!!")
            pontos_perdidos = abs(nro_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
