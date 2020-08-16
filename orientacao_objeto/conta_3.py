class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        """
            Quando usamos essa notação o python nos avisa que esse atributo
            não deve ser acessado diretamente, ele não proibe, mas avisa
        """
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

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    """
    # Só o limite é atualizavel, pq não tem sentido mudar o saldo sem depósito
    def set_limite(self, limite):
        self.__limite = limite
    """