class PosOcupadaException(Exception):
    pass

# Clase para el tablero
class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def poner_la_ficha(self, fila, col, ficha):
        if self.contenedor[fila][col] == "":
            self.contenedor[fila][col] = ficha
        else:
            raise PosOcupadaException("Ya hay una ficha en esa casilla.")
