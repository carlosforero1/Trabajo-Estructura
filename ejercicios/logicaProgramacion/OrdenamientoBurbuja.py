
def ordenaiento_burbuja_optima(arreglo):
    n = len(arreglo)

    for i in range(n - 1):
        intercambio = False

        for j in range(n - 1 - i):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                intercambio = True

        if intercambio == False:
            break

if __name__ == "__main__":
    num = [2, 3, 4, 5, 7, 6, 8]
    ordenaiento_burbuja_optima(num)
    print(num)