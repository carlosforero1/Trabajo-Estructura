
def eliminarDuplicados(arr):
    arreglo_sin_duplicados = []
    for elemento in arr:
        if elemento not in arreglo_sin_duplicados:
            arreglo_sin_duplicados.append(elemento)
    return arreglo_sin_duplicados


if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 5, 1, 2, 3]
    arreglo_sin_duplicados = eliminarDuplicados(arreglo)
    print("Arreglo original:", arreglo)
    print("Arreglo sin duplicados:", arreglo_sin_duplicados)