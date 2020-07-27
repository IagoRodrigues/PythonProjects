print("=================================")
print("=====Salário por funcionário=====")
print("=================================")

horas_trabalhadas = int(input("Quantidade de horas trabalhadas: "))

salario_bruto = 10 * horas_trabalhadas
inss = (8/100) * salario_bruto
salario_liquido = salario_bruto - inss

print("Salário bruto: R${:.2f}".format(salario_bruto))
print("Desconto INSS: R${:.2f}".format(inss))
print("Salário líquido: R${:.2f}".format(salario_liquido))