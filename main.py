from funciones import *

dificultad = seleccionar_dificultad()
tableroVisible = crearTableroVacio()
tableroJugador = crearTableroJugador(dificultad)
tableroOrdenador = crearTableroOrdenador(dificultad)
loop = True
ganador = 0
while loop:
    print("########### TU TABLERO ############")
    mostrarTablero(tableroJugador)
    print("####### TABLERO DE DISPAROS #######")
    mostrarTablero(tableroVisible)
    filaOrd, colOrd = pideCoordenadas(tableroVisible)
    realizarDisparo(tableroOrdenador, tableroVisible, filaOrd, colOrd)
    loop = quedanBarcos(tableroOrdenador)
    if loop == False:
        ganador = 1 
        break
    filaJug, colJug = disparoAleatorio(tableroJugador)
    realizarDisparo(tableroJugador, tableroJugador, filaJug, colJug)
    loop = quedanBarcos(tableroJugador)
    if loop == False:
        ganador = 2

if ganador == 1:
    print("¡¡¡HAS GANADO!!!")
if ganador == 2:
    print("¡¡¡HAS PERDIDO!!!")


  