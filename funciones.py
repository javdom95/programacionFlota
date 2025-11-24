import random
def seleccionar_dificultad():
    print("-----Bienvenido a Hundir la Flota-----")
    while True:
        print("1. Fácil\n2. Media\n3. Difícil")
        opcion = input("Elige una dificultad (1-3): ")
        if opcion in ("1", "2", "3"):
            return int(opcion)
        print("Opción no válida. Intenta de nuevo.\n")

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
                try: 
                    if PosColDireccion == 0: ##Comprobar si hacia la derecha está vacia y escribir hacia la derecha.
                        if tablero[PosFila][PosCol+1] == "-" and tablero[PosFila][PosCol+2] == "-":
                            for i in range(count):
                                tablero[PosFila][PosCol+i] = "B"

                    if PosColDireccion == 1: ##Comprobar si hacia la izquierda está vacia y escribir hacia la izquierda.
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
                try:
                    if PosColDireccion == 0: ##Comprobar si hacia la derecha está vacia y escribir hacia la derecha.
                        if tablero[PosFila][PosCol+1] == "-" and tablero[PosFila][PosCol+2] == "-" and tablero[PosFila][PosCol+3] == "-":
                            for i in range(count):
                                tablero[PosFila][PosCol+i] = "Z"

                    if PosColDireccion == 0: ##Comprobar si hacia la derecha está vacia y escribir hacia la derecha.
                        if tablero[PosFila][PosCol-1] == "-" and tablero[PosFila][PosCol-2] == "-" and tablero[PosFila][PosCol+3] == "-":
                            for i in range(count):
                                tablero[PosFila][PosCol-i] = "Z"
                    loop = False
                except:
                    continue
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
                try:
                    if PosColDireccion == 0: ##Comprobar si hacia la abajo está vacia y escribir hacia la abajo.
                        if tablero[PosFila+1][PosCol] == "-" and tablero[PosFila+2][PosCol] == "-" and tablero[PosFila+3][PosCol] == "-" and tablero[PosFila+4][PosCol] == "-":
                            for i in range(count):
                                tablero[PosFila+i][PosCol] = "P"

                    if PosColDireccion == 1: ##Comprobar si hacia la arriba está vacia y escribir hacia la arriba.
                        if tablero[PosFila-1][PosCol] == "-" and tablero[PosFila-2][PosCol] == "-" and tablero[PosFila-3][PosCol] == "-" and tablero[PosFila-4][PosCol] == "-":
                            for i in range(count):
                                tablero[PosFila-i][PosCol] = "P"
                    loop = False
                except:
                    continue
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
            tableroJugador = escribirB(tableroJugador)
        for i in range(5):
            tableroJugador = escribirL(tableroJugador)
        return tableroJugador
        
def crearTableroOrdenador(dificultad):
    return crearTableroJugador(dificultad)

def pideCoordenadas(tablero):
    while True:
        try:        
            fila = str(input("Introduce una fila a elegir (A-J):")).upper()
            if fila not in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"):
                raise Exception
            col = int(input("Introduce una col a elegir (0-9)"))
            if col > 9 or col < 0:
                print("Coordenadas incorrectas, vuelve a introducir las coordenadas, por favor")
                continue
            
            #Comprobar si la coordenada ya ha sido usada
            #Para pasar las letras a numero convertir usar numero unicode con ord() y restar el valor con el inicio de la fila (en este caso "A")
            indiceFila = ord(fila) - ord("A")
            if tablero[indiceFila][col] in ("X","A"): 
                print("Coordenada ya usada, vuelve a intentarlo.")
                continue
            return indiceFila, col
        except:
            print("Valor no válido, vuelve a intertarlo.")
            continue

def realizarDisparo(tableroObjetivo,tablero,fila,col): 
    if tableroObjetivo[fila][col] in ("P","Z","B","L"):
        tablero[fila][col] = "X"
        tableroObjetivo[fila][col] = "X" ##Es necesario que el tablero que se usa en quedanBarcos se actualice (aunque en el caso de disparo ordenador se actualiza 2 veces)
        print("¡Tocado!")
        return True
    else:
        tablero[fila][col] = "A"
        tableroObjetivo[fila][col] = "A"
        print("¡Agua!")
        return False

def mostrarTablero(tablero):
    print("  " + " ".join(str(num) for num in range(10)))
    columnaLetras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
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

def disparoAleatorio(tablero):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    while True:
        fila = letras[random.randint(0,9)]
        columna = random.randint(0,9)
        ##Añadir comprobar si casilla ya usada
        indiceFila = ord(fila) - ord("A")
        if tablero[indiceFila][columna] in ("X","A"): 
            continue
        print("Disparo del ordenador realizado en coordenada: ",fila+ "-" + str(columna))
        return indiceFila, columna