from clasesObjetos.clasesYObejtos.Persona import Persona


class Empleado(Persona):
    def __init__(self, salario, puesto,  nombre, edad, genero):
        super().__init__(nombre, edad, genero)
        self.salario = salario
        self.puesto = puesto

    def saludar(self):
        print("Hola desde empleado")

    def calcularSalarios(self):
        total = 0
        if self.salario != 0:
            total += self.salario
        else:
            print("El salario es menor a cero")
        return total


