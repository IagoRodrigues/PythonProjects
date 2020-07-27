print("=================================")
print("========Nascimento números=======")
print("=================================")

ano_nasc = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano de atual: "))

anos = ano_atual - ano_nasc
meses = anos * 12
dias = meses * 30

print("Viveu {} anos, {} meses e {} dias".format(anos, meses, dias))