print("=================================")
print("=======Rendimento do carro=======")
print("=================================")

tempo = float(input("Insira o tempo gasto na viagem em horas: "))
velocidade = float(input("Insira a velocidade média em km/h: "))
rendimento = float(input("Insira o rendimento do carro em km/l: "))
distancia_perc = tempo * velocidade
litros_usados = distancia_perc / rendimento

print("\nA velocidade média durante a viagem foi {:.2f}km/h".format(velocidade))
print("Teve duração de {:.1f} hora(s)".format(tempo))
print("Onde foram percorrido(s) {:.2f}km".format(distancia_perc))
print("E gastos {:.2f} litro(s) de combustível".format(litros_usados))