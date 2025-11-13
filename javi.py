from Alexis import * 

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

def quedanBarcos(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != "-" and tablero[i][j] != "X" and tablero[i][j] != "A":
                return True
    return False


tablero = crearTableroVacio()
mostrarTablero(tablero)
print(quedanBarcos(tablero))

tableroJugador = crearTableroJugador(3)
print(quedanBarcos(tableroJugador))