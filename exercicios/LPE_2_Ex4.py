print("=================================")
print("=========Maior e Menor===========")
print("=================================")

numeros = []

for var in range(1, 4):
    numeros.append(int(input("Insira um numero: ")))

print("Maior: {}".format(max(numeros)))
print("Menor: {}".format(min(numeros)))