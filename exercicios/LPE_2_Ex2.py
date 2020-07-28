print("=================================")
print("=======Soma ou Multiplica========")
print("=================================")

val_a = int(input("Valor a: "))
val_b = int(input("Valor b: "))
val_c = 0
string = ""

if (val_a == val_b):
    string = string + "São iguais! "
    val_c = val_a + val_b
else:
    string = string + "São diferentes! "
    val_c = val_a * val_b

string = string + "Resultado: {}".format(val_c)

print(string)