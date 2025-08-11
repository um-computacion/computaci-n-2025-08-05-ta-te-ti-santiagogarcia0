class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def obtener_nombre(self):
        return self.nombre

    def obtener_ficha(self):
        return self.ficha
