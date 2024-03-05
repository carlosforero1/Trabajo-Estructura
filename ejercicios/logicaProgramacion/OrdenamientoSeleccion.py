
def ordenamientoSeleccion(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(i+1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

if __name__ == '__main__':
    lista = [1, 3, 2, 4, 8, 7, 5, 6]
    lista_ordenada = ordenamientoSeleccion(lista)
    print(lista_ordenada)
