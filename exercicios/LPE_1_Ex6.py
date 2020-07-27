import math

print("==================================")
print("========Volume do cilindro========")
print("==================================")

raio = float(input("Raio do cilindro em cm: "))
altura = float(input("Altura do cilindro em cm: "))
volume = math.pi * math.pow(raio, 2) * altura

print("Este cilindro possui {:.2f}cm³".format(volume))