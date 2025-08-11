class PosOcupadaException(Exception):
    pass


class Tablero:
    def __init__(self):
        self.contenedor = [["", "", ""], ["", "", ""], ["", "", ""]]

    def poner_la_ficha(self, fil, col, ficha):
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("¡Posición ocupada!")

    def hay_ganador(self, ficha):
        # Revisar filas
        for fila in self.contenedor:
            if all(celda == ficha for celda in fila):
                return True
        # Revisar columnas
        for col in range(3):
            if all(self.contenedor[fila][col] == ficha for fila in range(3)):
                return True
        # Revisar diagonales
        if all(self.contenedor[i][i] == ficha for i in range(3)) or \
           all(self.contenedor[i][2-i] == ficha for i in range(3)):
            return True
        return False

    def esta_lleno(self):
        return all(celda != "" for fila in self.contenedor for celda in fila)
