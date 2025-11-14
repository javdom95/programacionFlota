import random

def mostrarTablero(tablero):
    print("  " + " ".join(str(num) for num in range(10)))
    columnaLetras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J"]
    letra = 0
    for linea in tablero:
        print(columnaLetras[letra], *linea)
        letra += 1   

def crearTableroVacio():
    tablero = []
    for i in range(10):
        tablero.append([])
        for j in range(10):
            tablero[i].append("-")
    return tablero

def escribirL(tablero):
    loop = True
    PosFila = -1
    PosCol = -1
    while loop:
        PosFila = random.randint(0,9)
        PosCol = random.randint(0,9)
        if tablero[PosFila][PosCol] == "-":
            tablero[PosFila][PosCol] = "L"
            loop = False
    return tablero
        #B

def escribirB(tablero):
        loop = True
        PosFila = -1
        PosCol = -1
        count = 3
        while loop:
            PosFila = random.randint(0,9)
            PosCol = random.randint(0,9)
            PosColDireccion = random.randint(0,1)
            #Comprobar que no se pase del maximo de rango
            if PosColDireccion == 0: #Derecha
                if PosCol+1 > len(tablero[PosFila]) or PosCol+2 > len(tablero[PosFila]):
                    continue

            if PosColDireccion == 1: #izquierda
                if PosCol-1 < 0 or PosCol-2 < 0:
                    continue

            ##Comprobar que no están llenos
            if tablero[PosFila][PosCol] == "-":
                if PosColDireccion == 0: ##Comprobar si hacia la derecha está vacia y escribir hacia la derecha.
                    try: 
                        if tablero[PosFila][PosCol+1] == "-" and tablero[PosFila][PosCol+2] == "-":
                            for i in range(count):
                                tablero[PosFila][PosCol+i] = "B"
                                loop = False
                    except Exception as error:
                        continue
                if PosColDireccion == 1: ##Comprobar si hacia la izquierda está vacia y escribir hacia la izquierda.
                    try:
                        if tablero[PosFila][PosCol-1] == "-" and tablero[PosFila][PosCol-2] == "-":
                            for i in range(count):
                                tablero[PosFila][PosCol-i] = "B"
                                loop = False
                    except Exception as error:
                        continue
        return tablero

def escribirZ(tablero):
        loop = True
        PosFila = -1
        PosCol = -1
        count = 4
        while loop:
            PosFila = random.randint(0,9)
            PosCol = random.randint(0,9)
            PosColDireccion = random.randint(0,1)
            #Comprobar que no se pase del maximo de rango
            if PosColDireccion == 0: #Derecha
                if PosCol+1 > len(tablero[PosFila]) or PosCol+2 > len(tablero[PosFila]) or PosCol+3 > len(tablero[PosFila]):
                    continue

            if PosColDireccion == 1: #izquierda
                if PosCol-1 < 0 or PosCol-2 < 0 or PosCol-3 < 0:
                    continue

            ##Comprobar que no están llenos
            if tablero[PosFila][PosCol] == "-":
                if PosColDireccion == 0: ##Comprobar si hacia la derecha está vacia y escribir hacia la derecha.
                    if tablero[PosFila][PosCol+1] == "-" and tablero[PosFila][PosCol+2] == "-" and tablero[PosFila][PosCol+3] == "-":
                        for i in range(count):
                            tablero[PosFila][PosCol+i] = "Z"
                            loop = False

                if PosColDireccion == 0: ##Comprobar si hacia la derecha está vacia y escribir hacia la derecha.
                    if tablero[PosFila][PosCol-1] == "-" and tablero[PosFila][PosCol-2] == "-" and tablero[PosFila][PosCol+3] == "-":
                        for i in range(count):
                            tablero[PosFila][PosCol-i] = "Z"
                            loop = False
        return tablero

def escribirP(tablero):
        loop = True
        PosFila = -1
        PosCol = -1
        count = 5
        while loop:
            PosFila = random.randint(0,9)
            PosCol = random.randint(0,9)
            PosColDireccion = random.randint(0,1)
            #Comprobar que no se pase del maximo de rango
            if PosColDireccion == 0: #Abajo
                if PosFila+1 > len(tablero) or PosFila+2 > len(tablero) or PosFila+3 > len(tablero) or PosFila+4 > len(tablero):
                    continue

            if PosColDireccion == 1: #Arriba
                if PosFila-1 < 0 or PosFila-2 < 0 or PosFila-3 < 0 or PosFila-4 < 0:
                    continue

            ##Comprobar que no están llenos
            if tablero[PosFila][PosCol] == "-":
                if PosColDireccion == 0: ##Comprobar si hacia la abajo está vacia y escribir hacia la abajo.
                    if tablero[PosFila+1][PosCol] == "-" and tablero[PosFila+2][PosCol] == "-" and tablero[PosFila+3][PosCol] == "-" and tablero[PosFila+4][PosCol] == "-":
                        for i in range(count):
                            tablero[PosFila+i][PosCol] = "P"
                            loop = False

                if PosColDireccion == 0: ##Comprobar si hacia la arriba está vacia y escribir hacia la arriba.
                    if tablero[PosFila-1][PosCol] == "-" and tablero[PosFila-2][PosCol] == "-" and tablero[PosFila-3][PosCol] == "-" and tablero[PosFila-4][PosCol] == "-":
                        for i in range(count):
                            tablero[PosFila-i][PosCol] = "P"
                            loop = False
        return tablero


def crearTableroJugador(dificultad):
    tableroJugador = crearTableroVacio()
    if dificultad == 3:
        tableroJugador = escribirB(tableroJugador)
        tableroJugador = escribirL(tableroJugador)
        return tableroJugador
    if dificultad == 2:
        tableroJugador = escribirP(tableroJugador)
        tableroJugador = escribirZ(tableroJugador)
        tableroJugador = escribirB(tableroJugador)
        for i in range(2):
            tableroJugador = escribirL(tableroJugador)
        return tableroJugador
    if dificultad == 1:
        tableroJugador = escribirP(tableroJugador)
        tableroJugador = escribirZ(tableroJugador)
        for i in range(2):
            tableroJugador = escribirb(tableroJugador)
        for i in range(5):
            tableroJugador = escribirL(tableroJugador)
        return tableroJugador
    
        
    
                

def crearTableroOrdenador(dificultad):
    return crearTableroJugador(dificultad)


'''
        arrayDificil = [
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
        return arrayDificil

    if dificultad == 2:
        arrayNormal = [
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
        return arrayNormal

    if dificultad == 1:
        arrayFacil = [
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
        return arrayFacil
        '''