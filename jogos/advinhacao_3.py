print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

nro_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    #print("Rodada", rodada, "de", total_de_tentativas)
    print("Rodada {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite seu número: ")
    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    acertou = nro_secreto == chute
    maior = nro_secreto < chute
    menor = nro_secreto > chute

    if(acertou):
        print("Você acertou!!")
    else:
        if(maior):
            print("Chutou alto!!")
        elif(menor):
            print("Chutou Baixo!!")

    rodada = rodada + 1;

print("Fim de jogo!")