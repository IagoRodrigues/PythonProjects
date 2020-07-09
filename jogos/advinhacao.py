print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

nro_secreto = 42

# A função input recebe um texto pra exibir e traz a resposta inserida pelo usuário COMO STRING
chute_str = input("Digite seu número: ")
print("Você digitou: ", chute_str)

# chute_str é string, nro_secreto é int: preciso converter todos para int
# para fazer a conversão
chute = int(chute_str)

if(chute == nro_secreto):
    print("Você acertou!!")
else:
    print("ERRoooU!")

'''
    Python só soma valores numéricos e só concatena strings.
    O código:
    
    numero1 = 10 ---> int
    numero2 = "20" ---> str
    soma = numero1 + numero2 (int + str = erro)
    
    Retorna:
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    
    O código:
    numero1 = "ia" ---> str
    numero2 = "go" ---> str
    soma = numero1 + numero2 (str + str = concatenação)
    
    Retorna:
    iago
    
    MAS PYTHON POSSUI SYNTAX SUGAR:
    O código:
    
    numero1 = 10
    numero2 = "20"
    produto = numero1 * numero2
    print(produto)
    
    Retorna:
    20202020202020202020
    
    Ao invés de escrever dez vezes o número 20, podemos simplificar e escrever 10 * "20"
'''