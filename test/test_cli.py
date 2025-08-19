import sys
import os
sys.path.append("/home/meli/Escritorio/computacion/cimputacion2025/tateti/computaci-n-2025-08-05-ta-te-ti-Malena2317")
import unittest
from unittest.mock import patch
import tateti

class TestTatetiSimple(unittest.TestCase):

    # Simula los nombres de los jugadores
    @patch("builtins.input", side_effect=["Ana", "Pedro"])
    def test_crear_juego(self, mock_input):
        juego = tateti.Tateti()
        # Compruebo que los nombres y fichas se asignaron
        self.assertEqual(juego.jugador1.nombre, "Ana")
        self.assertEqual(juego.jugador1.ficha, "X")
        self.assertEqual(juego.jugador2.nombre, "Pedro")
        self.assertEqual(juego.jugador2.ficha, "0")
        # Compruebo que empieza el turno del jugador1
        self.assertEqual(juego.jugador_actual().nombre, "Ana")

    # Prueba simple de cambiar el turno
    @patch("builtins.input", side_effect=["Ana", "Pedro"])
    def test_cambiar_turno(self, mock_input):
        juego = tateti.Tateti()
        juego.cambiar_turno()
        self.assertEqual(juego.jugador_actual().nombre, "Pedro")
        juego.cambiar_turno()
        self.assertEqual(juego.jugador_actual().nombre, "Ana")

if __name__ == "__main__":
    unittest.main()
