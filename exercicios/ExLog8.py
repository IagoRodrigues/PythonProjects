print("==================================")
print("========Gerador de números========")
print("==================================")

nro_original = list(input("Número original: "))

'''
Recebendo o numero inserido como list os algarismos já vem separados!

exemplo: input é 123

list(input) é ['1', '2', '3']

MAS

nesse caso todos os elementos da lista são string! Devemos converte-los pra int!
'''

lista_int = list(map(int, nro_original))

'''
A função map recebe dois parametros: o primeiro é a operação a ser feita em toda a lista, o segundo
é a lista em si. 

Agora se mandarmos escrever a lista_int teremos:
[1, 2, 3]

não é mais string!
'''

temp = ((lista_int[0]) + (lista_int[1] * 3) + (lista_int[2] * 5))

quarto_alg = temp % 7

lista_int.append(quarto_alg)
#No comando acima adiciono o quarto algarismo na lista de int

'''
Se fizermos

print("Número formado: {}".format(''.join(lista_int)))

receberemos:

TypeError: sequence item 0: expected str instance, int found

Uma vez que o join sperava receber str e recebeu int.
Como resolver? De duas formas:

1) Usando map novamente:
print("Número formado: {}".format(''.join(map(str, lista_int))))

2) Usando List Comprehension:
print("Número formado: {}".format(''.join(str(i) for i in lista_int)))
'''
print("Número formado: {}".format(''.join(str(i) for i in lista_int)))

#treinamos map e list comprehension e um ex só!