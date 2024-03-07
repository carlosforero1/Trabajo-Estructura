
def buscar_subcadena(cadena, subcadena):
    if subcadena in cadena:
        return cadena.index(subcadena)
    else:
        return -1

if __name__ == "__main__":
    cadena_principal = "Hola mundo, este es un ejemplo"
    subcadena = "mundo"
    posicion = buscar_subcadena(cadena_principal, subcadena)
    if posicion != -1:
        print(f"La subcadena '{subcadena}' esta en la posicion ", posicion)
    else:
        print(f"La subcadena '{subcadena}' no se encuentra en la cadena principal o -1")