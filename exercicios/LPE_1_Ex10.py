def preenche_lista(notas, pesos):
    for index in range(1, 4): #ATENÇÃO: estou preenchendo de 1 a 3, o ultimo número fica fora, ou seja, joguei 3 valores no list
        notas.append(float(input("Insira a nota da prova {}: ".format(index))))
        pesos.append(float(input("Insira o peso da prova {}: ".format(index))))

def calcula_media(notas, pesos):
    soma_notas = 0
    soma_pesos = 0

    for index in range(0, 3): #ATENÇÃO: estou lendo 3 valores: 0, 1, 2 mas devo colocar "até 3" uma vez que ele fica fora
        soma_notas = soma_notas + (notas[index] * pesos[index])
        soma_pesos += pesos[index]


    return soma_notas/soma_pesos

print("=================================")
print("=========Média Ponderada=========")
print("=================================")

notas = []
pesos = []

preenche_lista(notas, pesos)
media = calcula_media(notas, pesos)

print("A média do aluno foi {:.2f}".format(media))