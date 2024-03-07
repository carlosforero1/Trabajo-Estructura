def multiplicar_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

if __name__ == "__main__":
    matriz1 = [[1, 2, 3],
                [4, 5, 6]]
    matriz2 = [[7, 8],
               [9, 10],
               [11, 12]]
    resultado = multiplicar_matrices(matriz1, matriz2)
    if resultado:
        print("Resultado de la multiplicación:")
        for fila in resultado:
            print(fila)
    else:
        print("Las dimensiones de las matrices no son adecuadas para la multiplicación.")