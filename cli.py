from tateti import Tateti
from jugador import Jugador
from tablero import PosOcupadaException

def main():
    print("Bienvenidos al Tateti")

    nombre1 = input("Ingrese el nombre del Jugador 1 (ficha X): ")
    nombre2 = input("Ingrese el nombre del Jugador 2 (ficha O): ")

    jugador1 = Jugador(nombre1, "X")
    jugador2 = Jugador(nombre2, "O")

    juego = Tateti(jugador1, jugador2)

    while True:
        print("\nTablero: ")
        for fila in juego.tablero.contenedor:
            print(fila)

        if juego.obtener_ganador():
            print(f"¡Ganó {juego.obtener_ganador().obtener_nombre()}!")
            break

        if juego.tablero.esta_lleno():
            print("¡Empate!")
            break

        turno_actual = juego.obtener_turno()
        print(f"Turno de: {turno_actual.obtener_nombre()} ({turno_actual.obtener_ficha()})")

        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese col (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
        except PosOcupadaException as e:
            print(e)
        except ValueError:
            print("Entrada inválida, ingrese números entre 0 y 2.")

if __name__ == '__main__':
    main()
