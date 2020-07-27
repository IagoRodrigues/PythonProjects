print("=================================")
print("========Conversão do Dólar=======")
print("=================================")

cotacao = float(input("Cotação do dólar hoje: "))
dolar = float(input("Valor em dólares: "))
real = dolar * cotacao

print("US${:.2f} equivalem a R${:.2f}".format(dolar, real))