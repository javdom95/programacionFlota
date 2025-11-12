from funciones import *
from javi import *

crearTableroVacio()

nivelDif = 0
while nivelDif < 1 or nivelDif > 3:
    try:
        nivelDif = int(input("Por favor, seleccione el nivel de dificultad: "))
        if nivelDif < 1 or nivelDif > 3:
            print("Por favor, introduce un valor válido: 1, 2 ó 3.")
    except Exception as error:
        print("Por favor, introduce un valor válido: 1, 2 ó 3.")
        nivelDif = 0
    tableroJugador = [[]]
    
crearTableroJugador(nivelDif)