def encontrarElementoMaximo(lista):
    maximo = 0
    for list in lista:
        if maximo > list:
            maximo = maximo
        else:
            maximo = list
    return maximo

if __name__ == '__main__':
    lista = [1, 2, 3, 15, 5, 6, 7, 8, 9, 10]
    print(encontrarElementoMaximo(lista))