print("==================================")
print("========Cálculo de salário========")
print("==================================")

base = float(input("Insira o salário base: "))
gratificacao = (base * (5/100))
imposto = (base * (7/100))

salario = base + gratificacao - imposto

print("O funcionário deve receber R${:.2f} de salário base".format(base))
print("Somados R${:.2f} em gratificação".format(gratificacao))
print("Descontados R${:.2f} em impostos".format(imposto))
print("Totalizando R${:.2f} de salário líquido".format(salario))