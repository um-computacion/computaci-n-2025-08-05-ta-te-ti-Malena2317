import sys
import os
sys.path.append("/home/meli/Escritorio/computacion/cimputacion2025/tateti/computaci-n-2025-08-05-ta-te-ti-Malena2317")
import unittest
from unittest.mock import patch
from tateti import Tateti

class TestTateti(unittest.TestCase):

    @patch("builtins.input", side_effect=["Ana", "Pedro"])
    def test_creacion_tateti(self, mock_input):
        juego = Tateti()
        self.assertEqual(juego.jugador1.nombre, "Ana")
        self.assertEqual(juego.jugador1.ficha, "X")
        self.assertEqual(juego.jugador2.nombre, "Pedro")
        self.assertEqual(juego.jugador2.ficha, "0")

    @patch("builtins.input", side_effect=["Ana", "Pedro"])
    def test_turnos_cambian(self, mock_input):
        juego = Tateti()
        self.assertEqual(juego.jugador_actual().nombre, "Ana")
        juego.cambiar_turno()
        self.assertEqual(juego.jugador_actual().nombre, "Pedro")
        juego.cambiar_turno()
        self.assertEqual(juego.jugador_actual().nombre, "Ana")

    @patch("builtins.input", side_effect=["Ana", "Pedro"])
    def test_ocupar_casilla_y_cambiar_turno(self, mock_input):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(juego.tablero.contenedor[0][0], "X")
        self.assertEqual(juego.jugador_actual().nombre, "Pedro")

    @patch("builtins.input", side_effect=["Ana", "Pedro"])
    def test_hay_ganador_en_fila(self, mock_input):
        juego = Tateti()
        juego.tablero.contenedor[0] = ["X", "X", "X"]
        self.assertTrue(juego.hay_ganador())

    @patch("builtins.input", side_effect=["Ana", "Pedro"])
    def test_tablero_lleno(self, mock_input):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "X"]
        ]
        self.assertTrue(juego.esta_lleno())

if __name__ == "__main__":
    unittest.main()
