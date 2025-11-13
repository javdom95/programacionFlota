def seleccionar_dificultad():
        try:
            print("1. Fácil\n2. Media\n3. Difícil")
            dificultad = int(input("Elige una dificultad (1-3): "))
            if dificultad in (1, 2, 3):
                print("Has elegido la dificultad", dificultad)
                
            else:
                print("Opción no válida. Intenta de nuevo.\n")
        except ValueError:
            print("Valor incorrecto intente de nuevo")
        return dificultad

    

import random


def crearTableroJugador(dificultad):
    if dificultad == 3:
        tablero = [
            ["-", "-", "-", "L", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "B", "B", "B", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
            ]
        return tablero

    if dificultad == 2:
        tablero = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "B", "B", "B", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "L", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "P", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "L", "P", "-", "-", "-", "Z", "Z", "Z", "Z"],
            ["-", "-", "P", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "P", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "P", "-", "-", "-", "-", "-", "-", "-"]
            ]
        return tablero

    if dificultad == 1:
        tablero = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "P", "-"],
            ["-", "-", "-", "B", "B", "B", "-", "-", "P", "-"],
            ["-", "-", "-", "-", "-", "-", "L", "-", "P", "-"],
            ["-", "L", "-", "-", "-", "-", "-", "-", "P", "-"],
            ["-", "-", "-", "-", "-", "L", "-", "-", "P", "-"],
            ["B", "B", "B", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "L", "-", "-", "-", "L", "Z", "Z", "Z", "Z"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "B", "B", "B", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
            ]
        return tablero

def crearTableroOrdenador(dificultad):
    return crearTableroJugador(dificultad)

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

def PideCoordenadas(tablero):
    try:
        while True:
            fila = str(input("Introduce una fila a elegir (A-J):"))
            fila.upper()
            col = int(input("Introduce una col a elegir (0-9)"))
            if (fila != "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J") or col > 9 or col < 0:
                print("Coordenadas incorrectas, vuelve a introducir las coordenadas porfavor")
            return fila, col
    except ValueError:
        print("Valor incorrecto, vuelve a intertarlo")

def ComprobarCoordenadas(fila,col,tablero):
    tableroObjetivo = tablero[fila][col]
    return tableroObjetivo

def RealizarDisparo(tableroObjetivo,tablero,fila,col):
    if tableroObjetivo == "P" or "Z" or "B" or "L":
        tablero[fila][col] = "X"
        print("Tocado")
        return True
    else:
        tablero[fila][col] = "A"
        print("Agua")
        return False



tablero = crearTableroVacio()
dificultad = seleccionar_dificultad()
while True:
    crearTableroJugador(dificultad)
    crearTableroOrdenador(dificultad)
    mostrarTablero(tablero)
    fila, col = PideCoordenadas(tablero)
    if fila == "A":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 0
    elif fila == "B":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 1
    elif fila == "C":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 2
    elif fila == "D":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 3
    elif fila == "E":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 4
    elif fila == "F":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 5
    elif fila == "G":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 6
    elif fila == "H":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 7
    elif fila == "I":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 8
    elif fila == "J":
        print(f"Coordenada x = {fila} y = {col}")
        fila = 9
    else:
        print("Coordenada incorrecta")
    tableroObjetivo = ComprobarCoordenadas(fila,col,tablero)
    RealizarDisparo(tableroObjetivo,tablero,fila,col)
    quedanBarcos(tablero)
