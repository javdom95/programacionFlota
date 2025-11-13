from ..javi.py import *
import random

def MenuDificultad():
    while True:
        print() 

def PideCoordenadas(tablero):
    CoordenadaX = 0


'''
L = 1 casilla
B = 3 casillas horizontales
Z = 4 casillas horizontales consecutivas
P = 5 verticules
nivel 1 10 barcos 5L, 3B, 1Z, 1P.
nivel 2 5 barcos 2L, 1B, 1Z, 1P.
nivel 3 2 barcos 1L, 1B
''' [3][3]
def crearTableroJugador():
    if dificultad == 3:
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
'''
        tablero = []
        for i in range(10):
            tablero.([])
            for j in range(10):
                tablero[i][j] = ""
        return tablero
'''

array = crearTableroJugador(3)
mostrarTablero(array)