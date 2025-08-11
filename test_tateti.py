import unittest
from tateti import Tateti
from jugador import Jugador
from tablero import PosOcupadaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.jugador1 = Jugador("Alice", "X")
        self.jugador2 = Jugador("Bob", "O")
        self.juego = Tateti(self.jugador1, self.jugador2)

    def test_turnos_alternados(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.obtener_turno(), self.jugador2)
        self.juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(self.juego.obtener_turno(), self.jugador1)

    def test_ganador_fila(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 0)  # O
        self.juego.ocupar_una_de_las_casillas(0, 1)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(0, 2)  # X gana
        self.assertEqual(self.juego.obtener_ganador(), self.jugador1)

    def test_ganador_columna(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(0, 1)  # O
        self.juego.ocupar_una_de_las_casillas(1, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(2, 0)  # X gana
        self.assertEqual(self.juego.obtener_ganador(), self.jugador1)

    def test_ganador_diagonal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(0, 1)  # O
        self.juego.ocupar_una_de_las_casillas(1, 1)  # X
        self.juego.ocupar_una_de_las_casillas(0, 2)  # O
        self.juego.ocupar_una_de_las_casillas(2, 2)  # X gana
        self.assertEqual(self.juego.obtener_ganador(), self.jugador1)

    def test_empate(self):
        jugadas = [
            (0, 0), (0, 1),
            (0, 2), (1, 1),
            (1, 0), (1, 2),
            (2, 1), (2, 0),
            (2, 2)
        ]
        for jugada in jugadas:
            self.juego.ocupar_una_de_las_casillas(*jugada)
        self.assertTrue(self.juego.tablero.esta_lleno())
        self.assertIsNone(self.juego.obtener_ganador())

    def test_posicion_ocupada(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    def test_no_permite_jugar_despues_de_ganar(self):
        # X gana en fila superior
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 0)  # O
        self.juego.ocupar_una_de_las_casillas(0, 1)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(0, 2)  # X gana
        ganador = self.juego.obtener_ganador()
        self.assertEqual(ganador, self.jugador1)

        # Intento de seguir jugando
        turno_antes = self.juego.obtener_turno()
        self.juego.ocupar_una_de_las_casillas(2, 2)
        self.assertEqual(self.juego.obtener_turno(), turno_antes)  # No cambia turno

    def test_no_permite_jugar_despues_de_empate(self):
        # Secuencia de empate
        jugadas = [
            (0, 0), (0, 1),
            (0, 2), (1, 1),
            (1, 0), (1, 2),
            (2, 1), (2, 0),
            (2, 2)
        ]
        for jugada in jugadas:
            self.juego.ocupar_una_de_las_casillas(*jugada)

        self.assertTrue(self.juego.tablero.esta_lleno())

        turno_antes = self.juego.obtener_turno()
        self.juego.ocupar_una_de_las_casillas(0, 0)  # Ya estaba ocupado o lleno
        self.assertEqual(self.juego.obtener_turno(), turno_antes)

if __name__ == '__main__':
    unittest.main()
