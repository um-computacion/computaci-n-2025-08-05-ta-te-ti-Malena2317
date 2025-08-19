import sys
import os
sys.path.append("/home/meli/Escritorio/computacion/cimputacion2025/tateti/computaci-n-2025-08-05-ta-te-ti-Malena2317")
import unittest
from tablero import Tablero, PosOcupadaException


class TestTablero(unittest.TestCase):

    def test_poner_ficha_vacia(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        self.assertEqual(t.contenedor[0][0], "X")

    def test_poner_dos_fichas_distintas_posiciones(self):
        t = Tablero()
        t.poner_la_ficha(1, 1, "O")
        t.poner_la_ficha(2, 2, "X")
        self.assertEqual(t.contenedor[1][1], "O")
        self.assertEqual(t.contenedor[2][2], "X")

    def test_no_deja_poner_dos_veces_en_el_mismo_lugar(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            t.poner_la_ficha(0, 0, "O")

    def test_tablero_empieza_vacio(self):
        t = Tablero()
        self.assertEqual(t.contenedor[0][0], "")
        self.assertEqual(t.contenedor[1][1], "")
        self.assertEqual(t.contenedor[2][2], "")

if __name__ == '__main__':
    unittest.main()
