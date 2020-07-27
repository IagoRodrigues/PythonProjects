print("================================")
print("===Calculadora de temperatura===")
print("================================")

celsius = float(input("Qual a temperatura em Celsius no momento?"))

fahrenheit = ((celsius * 9/5) + 32)

print("A temperatura é {:.2f}ºF".format(fahrenheit))