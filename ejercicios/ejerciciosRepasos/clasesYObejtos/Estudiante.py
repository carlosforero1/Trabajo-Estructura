from clasesObjetos.clasesYObejtos.Persona import Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad , genero, grado, escuela):
        super().__init__(nombre, edad, genero)
        self.__grado = grado
        self.__escuela = escuela

    def saludar(self):
        print("Hola desde estudiante")
