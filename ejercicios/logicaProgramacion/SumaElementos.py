def sumaElementos(lista):
    total = 0
    for listar in lista:
        total += listar
    return total

if __name__ == "__main__":
    num = [2, 3, 4, 5, 6, 7, 8]
    resultado = sumaElementos(num)
    print(resultado)

