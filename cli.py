from tateti import Tateti
def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()

    while not juego.hay_ganador() and not juego.esta_lleno():
        print("Tablero actual:")
        for f in juego.tablero.contenedor:
            print(f)
        jug = juego.jugador_actual()
        print("Turno de", jug.nombre, "(" + jug.ficha + ")")
        try:
            f = int(input("Ingrese fila (0 a 2): "))
            c = int(input("Ingrese columna (0 a 2): "))
            juego.ocupar_una_de_las_casillas(f, c)
        except Exception as err:
            print("Error:", err)

    print("Tablero final:")
    for f in juego.tablero.contenedor:
        print(f)

    if juego.hay_ganador():
        g = juego.jugador_actual()  
        print("Ganó", g.nombre, "(" + g.ficha + ")")
    else:
        print("Empate.")

if __name__ == '__main__':
    main()
