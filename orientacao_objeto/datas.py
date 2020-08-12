
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada_br(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))

    def formatada_eua(self):
        print("{}/{}/{}".format(self.ano, self.mes, self.dia))