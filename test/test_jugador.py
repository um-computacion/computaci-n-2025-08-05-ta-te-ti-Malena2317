import sys
import os
sys.path.append("/home/meli/Escritorio/computacion/cimputacion2025/tateti/computaci-n-2025-08-05-ta-te-ti-Malena2317")
import unittest
from jugador import Jugador   # acá importa desde jugador.py

class TestJugador(unittest.TestCase):

    def test_crear_jugador_nombre(self):
        j = Jugador("Ana", "X")
        self.assertEqual(j.nombre, "Ana")

    def test_crear_jugador_ficha(self):
        j = Jugador("Pedro", "O")
        self.assertEqual(j.ficha, "O")

    def test_jugador_nombre_y_ficha(self):
        j = Jugador("Meli", "X")
        self.assertEqual(j.nombre, "Meli")
        self.assertEqual(j.ficha, "X")

    def test_dos_jugadores_diferentes(self):
        j1 = Jugador("Juan", "X")
        j2 = Jugador("Laura", "O")
        self.assertNotEqual(j1.nombre, j2.nombre)
        self.assertNotEqual(j1.ficha, j2.ficha)

if __name__ == '__main__':
    unittest.main()
