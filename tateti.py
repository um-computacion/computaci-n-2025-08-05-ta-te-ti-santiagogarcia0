from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = jugador1  
        self.tablero = Tablero()
        self.ganador = None

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.turno.obtener_ficha())

        
        if self.tablero.hay_ganador(self.turno.obtener_ficha()):
            self.ganador = self.turno
            return

        if self.tablero.esta_lleno():
            return

        self.turno = self.jugador1 if self.turno == self.jugador2 else self.jugador2

    def obtener_turno(self):
        return self.turno

    def obtener_ganador(self):
        return self.ganador
