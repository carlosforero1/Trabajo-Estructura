def buscar_elemento(arreglo, objetivo):
    return objetivo in arreglo

if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 5]
    objetivo = 3
    if buscar_elemento(arreglo, objetivo):
        print(f"{objetivo} está presente en el arreglo.")
    else:
        print(f"{objetivo} no está presente en el arreglo.")