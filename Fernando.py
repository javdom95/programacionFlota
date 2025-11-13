def PideCoordenadas(array):
    try:
        while True:
            fila = str(input("Introduce una fila a elegir (A-J):"))
            fila.upper()
            col = int(input("Introduce una col a elegir (0-9)"))
            if (fila != "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J") or col > 9 or col < 0:
                print("Coordenadas incorrectas, vuelve a introducir las coordenadas porfavor")
            elif fila == "A":
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
            else:
                print(f"Coordenada x = {fila} y = {col}")
                fila = 9
            return fila, col
    except ValueError:
        print("Valor incorrecto, vuelve a intertarlo")

def ComprobarCoordenadas(fila,col,arrayOrdenador):
    arrayObjetivo = arrayOrdenador[fila][col]
    return arrayObjetivo

def RealizarDisparo(arrayObjetivo,arrayOrdenador,fila,col):
    if arrayObjetivo == "P" or "Z" or "B" or "L":
        arrayOrdenador[fila][col] = "X"
        print("Tocado")
        return True
    else:
        arrayOrdenador[fila][col] = "A"
        print("Agua")
        return False
