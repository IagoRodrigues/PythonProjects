class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo R${:.2f} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    """
    Pode Sacar fica sendo um método privado com essa notacao
    """
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite

        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

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
        Quando todos os objetos de uma mesma classe compartilham um mesmo metodo ou atributo,
        eh interessante colocar esse metodo/atributo como sendo estatico, ou seja, eh um
        metodo/atributo de classe.

        para isso samos a sintaxe abaixo:
    """
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    """
        Já no caso de atributos podemos simplesmente declarar:
        
        Atributo = valor
        
        logo abaixo do nome da classe, sem o uso de self e fora do __init__
        isso faz com que o atributo seja estático (atributo de classe), por exemplo:
        
        class Circulo:

            PI = 3.14
            
        e na hora de usar:
        
        >>>Circulo.PI
        3.14
    """

    """
        Python segue uma convencao para metodos e atributos privados:
        Dentro da classe conta:
        
        a)o atributo __saldo se torna _Conta__saldo.
        b)o método __pode_sacar() se torna _Conta__pode_sacar().
    """