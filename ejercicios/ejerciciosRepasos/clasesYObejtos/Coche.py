class Coche:
    def __init__(self, velocidad):
        self.__velocidad = velocidad


    def acelerar(self, incremeto):
        if  incremeto > 0:
            print("el auto aumento su velocidad")
        else:
            print("el auto no aumento su velocidad")

    def frenar(self, frenada):
        if frenada == self.__velocidad or frenada > self.__velocidad:
            print("el auto se detuvo")
        elif frenada < self.__velocidad:
            print("el auto bajo su velocidad a: " + self.__velocidad + "KM/H")
        else:
            print("opcion invalida")

