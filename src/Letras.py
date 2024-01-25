"""
Archivo contenedor de la clase letra
"""

class Letra:
    """
    Clase letra hecha para chequear la letra del dni
    """
    def __init__(self):
        self.letras = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]

    def get_letras(self) -> list:
        """
        Devuelve una copia de la lista del objeto
        """
        return self.letras[:]

    def __repr__(self) -> str:
        return str(self.get_letras())

    def get_letra_by_position(self, posicion: int) -> str:
        """
        Devuelve la letra asignada a una posicion
        """
        try:
            return self.letras[posicion]
        except IndexError:
            return "Posicion fuera de rango"

    def get_largo(self) -> int:
        """
        Devuelve lo largo de la lista del objeto
        """
        return len(self.letras)

    def get_letra_by_dni(self, numero) -> str:
        """
        Devuelve la letra asignada a un numero
        """
        return self.letras[int(numero) % self.get_largo()]

    def is_letra_in_tabla(self, char: str) -> bool:
        """
        Devuelve un booleano si el caracter esta en la lista del objeto
        """
        return char.upper() in self.letras


if __name__ == "__main__":
    from class_bcolors_enum import Colors

    Letras = Letra()
    print(f"\nLas letras son : {Colors.HEADER}")
    print(Letras)
    print(
        f"{Colors.ENDC}\nLa letra asignada a la posicion 4 es: {Colors.OKGREEN}{Letras.get_letra_by_position(4)}{Colors.ENDC}"
    )
    print(
        f"\nLa letra asignada a la posicion 33 es:  {Colors.BOLD}{Colors.UNDERLINE}{Colors.FAIL}{Letras.get_letra_by_position(33)}{Colors.ENDC}"
    )
    print(
        f"\nLa letra de 77422360 es: {Colors.OKGREEN}{Letras.get_letra_by_dni(77422360)}{Colors.ENDC}"
    )
    print(
        f"\nLa letra l esta en letras:  {Colors.OKBLUE}{str(Letras.is_letra_in_tabla('l'))}{Colors.ENDC}"
    )
    print(
        f"\nLa letra N esta en letras:  {Colors.OKBLUE}{str(Letras.is_letra_in_tabla('N'))}{Colors.ENDC}"
    )
    print(
        f"\nLa letra Ñ esta en letras: {Colors.BOLD}{Colors.UNDERLINE}{Colors.FAIL}{str(Letras.is_letra_in_tabla('ñ'))}{Colors.ENDC}"
    )
