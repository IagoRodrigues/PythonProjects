def calculaMedia(aluno):
    media = (aluno[1] * 0.25 + aluno[2] * 0.25 + aluno[3] * 0.5)

    return media

print("=================================")
print("==========Nome e Notas===========")
print("=================================")

'''
Cada classe é um list com:
0- Aluno 1
1- Aluno 2
2- Aluno 3
'''
classe = []

'''
Cada aluno é um list com:
0 - Nome
1 - Lista
2 - Prova
3 - Prática
4 - Média
'''
for index in range(1, 4):
    aluno = []
    nome_aluno = input("Insira o nome do aluno {}: ".format(index))
    aluno.append(nome_aluno)

    nota_1 = float(input("Lista: "))
    aluno.append(nota_1)

    nota_2 = float(input("Prova: "))
    aluno.append(nota_2)

    nota_3 = float(input("Prática: "))
    aluno.append(nota_3)

    aluno.append(calculaMedia(aluno))

    classe.append(aluno)

[print("Aluno {} Aprovado".format(aluno[0])) for aluno in classe if aluno[4] >= 6]