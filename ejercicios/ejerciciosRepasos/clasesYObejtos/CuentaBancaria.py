class CuentaBancaria:
    def __init__(self, saldo = 0):
     self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("El valor del dinero depositado es: $ ", self.__saldo)
        else:
            print("la cantidad de dinero es menor a cero")

    def transferir(self, valor):
        if self.__saldo >= valor:
            print("acabas de transferir: $ ", valor)
            self.__saldo -= valor
            print("saldo de la cuenta: $", self.__saldo)

    def saldoActual(self):
        return print("el saldo actual es: $", self.__saldo)
