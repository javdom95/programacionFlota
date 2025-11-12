print("-----Bienvenido a Hundir la Flota-----")

def MenuDificultad():
    while True:
        print()

def PideCoordenadas(tablero):
    CoordenadaX = 0


def seleccionar_dificultad():
    while True:
        opcion = input("Elige una dificultad (1-3): ")
        print("1. Fácil\n2. Media\n3. Difícil")
        if opcion in ("1", "2", "3"):
            return int(opcion)
        print("Opción no válida. Intenta de nuevo.\n")


nivel = seleccionar_dificultad()
print("Has elegido la dificultad", nivel)