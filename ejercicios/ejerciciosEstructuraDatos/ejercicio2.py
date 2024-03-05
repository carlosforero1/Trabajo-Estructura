from builtins import input

class ejercicio2:
    def __init__(self):
        self.lista = []

        valor = True
        print("Primero crea una lista de elementos")
        print("Introduce un numero y cuando desees terminar escribe salir: ")
        while valor:
            numero = input("Número: ")
            if numero.lower() == "salir":
                print("Saliendo del programa")
                valor = False
            else:
                self.lista.append(numero)
                valor = True

        self.menu()

    def menu(self):
        vol = True
        while vol:
            opcion = input("Dime ahora que quieres hacer:\n"
                           "1. Eliminar duplicados\n"
                           "2. Sumar la lista\n"
                           "3. Comparar dos listas\n"
                           "4. Salir del programa\n"
                           "Opción: ")

            if opcion == "1":
                resultado = self.eliminar_duplicados(self.lista)
                print("La lista sin duplicados es: ", resultado)
            elif opcion == "2":
                resultado = self.suma_de_lista(self.lista)
                print("La suma de la lista es:", resultado)
            elif opcion == "3":
                print("Agrega la segunda lista para comparar")
                lista2 = []
                valor = True
                while valor:
                    numero= input("Número: ")
                    if numero.lower() == "salir":
                        print("Saliendo del programa")
                        valor = False
                    else:
                        lista2.append(numero)
                        valor = True
                if self.suma_dos_lista(self.lista, lista2):
                    print("Las listas tienen elementos comunes.")
                else:
                    print("Las listas no tienen elementos comunes.")

            elif opcion == "4":
                print("Saliendo del programa")
                vol = False

    def eliminar_duplicados(self, lista):
        return list(set(lista))

    def suma_de_lista(self, lista):
        suma = 0
        for elemento in lista:
            suma += int(elemento)
        return suma

    def suma_dos_lista(self, lista1, lista2):
        for elemento in lista1:
            if elemento in lista2:
                return True
        return False


objeto_ejercicio = ejercicio2()
