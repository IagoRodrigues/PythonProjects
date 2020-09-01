comp_pista = int(input("Comprimento da pista: "))
nro_voltas = int(input("Numero de voltas do GP: "))
reabast_desej = int(input("Reabastecimentos desejados: "))
consumo_do_carro = int(input("Consumo do carro: "))

tamanho_corrida = nro_voltas * comp_pista;

tamanho_em_km = tamanho_corrida / 1000;

consumo_total = tamanho_em_km / consumo_do_carro;

litros_ate_abastecer = consumo_total / reabast_desej;

print("Será necessário abastecer o carro com no minimo {:.2f} litros por reabastecimento".format(litros_ate_abastecer))