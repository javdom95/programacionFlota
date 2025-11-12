def PideCoordenadas(tablero):
    try:
        fila = str(input("Introduce una fila a elegir (A-J):"))
        fila.lower()
        columna = int(input("Introduce una columna a elegir (0-9)"))
        if (fila != "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j") or columna > 9 or columna < 0:
            print("Coordenadas incorrectas, vuelve a introducir las coordenadas porfavor")
        else:
            print(f"Coordenada x = {fila} y = {columna}")
            return fila, columna
    except ValueError:
        print("Valor incorrecto, vuelve a intertarlo")

#def ComprobarCoordenadas(fila,columna,tablero):
    #Coordenada = tablero[fila][columna]