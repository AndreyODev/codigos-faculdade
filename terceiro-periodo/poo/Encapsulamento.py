class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Deposito: {self.__saldo}")

    def sacar(self, titular, valor):
        self.__saldo -= valor
        self.__titular = titular
        print(f"O {self.__titular} sacou: {valor}")

    def get_saldo(self):
        print(f"Saldo atual: {self.__saldo}")
        
c = ContaBancaria("Andrey")

c.depositar(1000)

c.sacar("Andrey", 459)

c.get_saldo()
