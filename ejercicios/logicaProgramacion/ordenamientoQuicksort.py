def arreglo(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return arreglo(left) + middle + arreglo(right)

if __name__ == "__main__":
    arreglo1 = [3, 6, 8, 10, 1, 2, 1]
    print("Arreglo original:", arreglo1)
    arreglo_ordenado = arreglo(arreglo1)
    print("Arreglo ordenado:", arreglo_ordenado)