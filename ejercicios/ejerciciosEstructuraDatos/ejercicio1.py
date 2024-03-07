import np

class ClasePrueba:
    def agregar_numero(lista):
            lista.append(lista)
            return lista

    def elimina_duplicados(lista):
        return np.unique(lista)

    def suma_de_lista(self, lista):
        valor = 0
        for list in lista:
            valor += list
        return valor

    def comun_entre_lista(self, lista1, lista2):
        valor = False
        for variable in lista1:
            if variable in lista2:
                valor = True
            else:
                valor =  False
            return valor
