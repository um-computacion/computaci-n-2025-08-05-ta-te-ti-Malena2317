from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self):
        self.tablero = Tablero()
        nom1 = input("Nombre del jugador X: ")
        nom2 = input("Nombre del jugador 0: ")
        self.jugador1 = Jugador(nom1, "X")
        self.jugador2 = Jugador(nom2, "0")
        self.turno = self.jugador1

    def ocupar_una_de_las_casillas(self, fila, col):
        self.tablero.poner_la_ficha(fila, col, self.turno.ficha)
        if not self.hay_ganador():
            self.cambiar_turno()

    def cambiar_turno(self):
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1

    def jugador_actual(self):
        return self.turno

    def jugador_anterior(self):
        if self.turno == self.jugador1:
            return self.jugador2
        else:
            return self.jugador1

    def hay_ganador(self):
        t = self.tablero.contenedor

        # Reviso las filas
        if t[0][0] == t[0][1] and t[0][1] == t[0][2] and t[0][0] != "":
            return True
        if t[1][0] == t[1][1] and t[1][1] == t[1][2] and t[1][0] != "":
            return True
        if t[2][0] == t[2][1] and t[2][1] == t[2][2] and t[2][0] != "":
            return True

        # Reviso las columnas
        if t[0][0] == t[1][0] and t[1][0] == t[2][0] and t[0][0] != "":
            return True
        if t[0][1] == t[1][1] and t[1][1] == t[2][1] and t[0][1] != "":
            return True
        if t[0][2] == t[1][2] and t[1][2] == t[2][2] and t[0][2] != "":
            return True

        # Reviso las diagonales
        if t[0][0] == t[1][1] and t[1][1] == t[2][2] and t[0][0] != "":
            return True
        if t[0][2] == t[1][1] and t[1][1] == t[2][0] and t[0][2] != "":
            return True

        return False

    def esta_lleno(self):
        
        tablero_lleno = True
        for fila in self.tablero.contenedor:
            for casilla in fila:
                if casilla == "":
                    tablero_lleno = False
                    # Cuando encuentro uno, salgo de la función.
                    return False
        # Solo llego aquí si recorrí todo el tablero y no encontré un vacío.
        return tablero_lleno
