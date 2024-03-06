
def invertirArreglo(arr):
    inicio = 0
    fin = len(arr) - 1

    while inicio < fin:
        arr[inicio], arr[fin] = arr[fin], arr[inicio]
        inicio += 1
        fin -= 1

    return arr

if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 5]
    print("Arreglo original:", arreglo)
    arreglo_invertido = invertirArreglo(arreglo)
    print("Arreglo invertido:", arreglo_invertido)