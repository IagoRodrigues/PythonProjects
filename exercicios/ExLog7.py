print("=================================")
print("=======Inversor de números=======")
print("=================================")

numero = input("Insira o numero a ser invertido: ")
inverso = ''.join(list(reversed(numero)))
print(type(inverso))

'''
A função reversed retorna um interator que pode ser usado para percorrer uma lista de forma reversa,
logo se fizermos:

>>>inverso = reversed(numero)

Temos como tipo:
>>>print(type(inverso))
O tipo reversed

E se mandarmos escrever ficamos com:
>>>print("Inverso: {}".format(inverso))
Inverso: <reversed object at 0x0029AF10

Por isso pego o reversed e jogo para uma lista:
>>>inverso = list(reversed(numero))

Agora o tipo que tenho é:
>>>print(type(inverso))
Tipo list

E se mandar escrever a saída é:
>>>print("Inverso: {}".format(inverso))
Inverso: ['3', '2', '1']

Agora posso juntar todos os elementos da lista usando uma string como separador e join:
vou usar um espaço vazio como separador, afinal não quero nada entre os itens da lista:

>>>inverso = ''.join(list(reversed(numero)))

>>>print(type(inverso))
tipo str

>>>print("Inverso: {}".format(inverso))
escreve: Inverso: 321
'''
soma = int(numero) + int(inverso)

print("\nNúmero: {}".format(numero))
print("Inverso: {}".format(inverso))
print("Soma: {}".format(soma))