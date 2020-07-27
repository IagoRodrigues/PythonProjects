print("=================================")
print("======Calculadora de carros======")
print("=================================")

preco_de_fab = float(input("Qual o preço de fábrica do carro?"))
perc_lucro_do_dist = float(input("Qual o pencentual de lucro do distribuidor?"))
perc_impostos = float(input("Qual o pencentual de impostos sobre o veículo?"))

lucro_do_dist = preco_de_fab * (perc_lucro_do_dist / 100)
impostos = preco_de_fab * (perc_impostos / 100)
preco_final = preco_de_fab + lucro_do_dist + impostos

print("\nO distribuidor lucra {}% portanto o valor de seu lucro é {:.2f}".format(perc_lucro_do_dist, lucro_do_dist))
print("Os impostos pesam {}% portanto o valor é {:.2f}".format(perc_impostos, impostos))
print("O preço final do veículo será R${:.2f}".format(preco_final))