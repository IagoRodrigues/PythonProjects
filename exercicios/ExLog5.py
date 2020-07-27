print("=================================")
print("=======Calculadora de luz========")
print("=================================")

lado_1 = float(input("Primeira medida do cômodo (em metros): "))
lado_2 = float(input("Segundaa medida do cômodo (em metros): "))

area = lado_1 * lado_2
luz = area * 18

print("\nA área do cômodo é {:.2f}m² e deve receber uma iluminação com {}w de potência".format(area, luz))