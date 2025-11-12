def PideCoordenadas(tablero):
    try:
        fila = str(input("Introduce una fila a elegir (A-J):"))
        fila.upper()
        columna = int(input("Introduce una columna a elegir (0-9)"))
        if (fila != "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J") or columna > 9 or columna < 0:
            print("Coordenadas incorrectas, vuelve a introducir las coordenadas porfavor")
        elif fila == "A":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 0
        elif fila == "B":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 1
        elif fila == "C":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 2
        elif fila == "D":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 3
        elif fila == "E":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 4
        elif fila == "F":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 5
        elif fila == "G":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 6
        elif fila == "H":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 7
        elif fila == "I":
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 8
        else:
            print(f"Coordenada x = {fila} y = {columna}")
            fila = 9
        return fila, columna
    except ValueError:
        print("Valor incorrecto, vuelve a intertarlo")

#def ComprobarCoordenadas(fila,columna,tablero):
    #tableroObjetivo = tablero[fila][columna]
    #return tableroObjetivo
