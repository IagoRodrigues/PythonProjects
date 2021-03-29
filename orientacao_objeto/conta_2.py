
class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        # Quando usamos essa notação o python nos avisa que esse atributo
        # não deve ser acessado diretamente, ele não proibe, mas avisa
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo R${:.2f} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfe(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)