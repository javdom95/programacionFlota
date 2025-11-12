def crearTableroVacio():
    tablero = []
    columnaLetras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in range(10):
        tablero.append([columnaLetras[i]])
        for j in range(10):
            tablero[i].append("-")

    filaNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
    print("  " + " ".join(str(num) for num in range(10)))
    for linea in tablero:
        print(*linea)   
