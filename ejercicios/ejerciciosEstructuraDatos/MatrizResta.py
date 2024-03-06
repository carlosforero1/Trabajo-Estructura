def resta_matriz(matriz):
    total_resta = matriz[0][0]
    filas = len(matriz)
    columnas = len(matriz[0])

    print("Filas: ", filas)
    print("Columnas: ", columnas)

    limite_superior = 0
    limite_inferior = filas - 1
    limite_izquierdo = 0
    limite_derecho = columnas - 1

    print(limite_superior)
    print(limite_inferior)
    print(limite_izquierdo)
    print(limite_derecho)

    while limite_superior <= limite_inferior and limite_izquierdo <= limite_derecho:
        print("rango ↑ ↓:", limite_superior, limite_inferior + 1)
        for i in range(limite_superior, limite_inferior + 1):
            total_resta -= matriz[i][limite_izquierdo]
        limite_izquierdo += 1

        print("rango ← →:", limite_izquierdo, limite_derecho + 1)
        for i in range(limite_izquierdo, limite_derecho + 1):
            total_resta -= matriz[limite_inferior][i]
        limite_inferior -= 1

        if limite_superior <= limite_inferior:
            print("rango ↓ ↑:", limite_superior, limite_inferior)
            for i in range(limite_inferior, limite_superior - 1, -1):
                total_resta -= matriz[i][limite_derecho]
            limite_derecho -= 1

        if limite_izquierdo <= limite_derecho:
            print("rango → ←:", limite_izquierdo, limite_derecho)
            for i in range(limite_derecho, limite_izquierdo - 1, -1):
                total_resta -= matriz[limite_superior][i]
            limite_superior += 1

    return total_resta

if __name__ == "__main__":
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    resultado = resta_matriz(matriz)
    print("La resta de los elementos de la matriz en forma circular es:", resultado)
