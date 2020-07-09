print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

nro_secreto = 42

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
        print("Chutou alto!")
    elif(menor):
        print("Chutou Baixo!")

# else if = elif

print("Fim de jogo!")