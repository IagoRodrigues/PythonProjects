print("================================")
print("=====Calculadora de Teatros=====")
print("================================")

valor_espet = float(input("Valor do espetáculo: "))
valor_ingresso = float(input("Valor do ingresso: "))

necessarios = valor_espet / valor_ingresso;

print("Será necessário vender {:.1f} ingresso(s) para pagar este espetáculo!".format(necessarios))