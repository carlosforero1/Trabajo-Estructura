def contarOcurriencias(arr):
    contador = {}
    for elemento in arr:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 2, 3, 1, 2, 4, 5, 9]
    ocurrencias = contarOcurriencias(arreglo)
    print("Ocurrencias de cada elemento:")
    for elemento, cantidad in ocurrencias.items():
        print(f"{elemento}: {cantidad}")