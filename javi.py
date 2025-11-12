def crearTableroVacio():
    tablero = []
    for i in range(10):
        tablero.append([])
        for j in range(10):
            tablero[i].append("-")
    return tablero

def mostrarTablero(tablero):
    print("  " + " ".join(str(num) for num in range(10)))
    columnaLetras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J"]
    letra = 0
    for linea in tablero:
        print(columnaLetras[letra], *linea)
        letra += 1   

    
tablero = crearTableroVacio()
mostrarTablero(tablero)