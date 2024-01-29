"""
Archivo contenedor de la clase Dni_letter
"""

class Dni_letter:
    """
    Clase Dni_letter hecha para chequear la letra del dni
    """
    def __init__(self):
        self.posible_letters = [
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

    def get_letter_by_dni(self, numero) -> str:
        """
        Devuelve la letra asignada a un numero
        """
        return self.get_letter_by_position(int(numero) % self.__get_largo())

    def does_letter_exists(self, char: str) -> bool:
        """
        Devuelve un booleano si el caracter esta en la lista del objeto
        """
        return char.upper() in self.get_posible_letters()

    def get_posible_letters(self) -> list:
        """
        Devuelve una copia de la lista del objeto
        """
        return self.posible_letters[:]

    def __repr__(self) -> str:
        return str(self.get_posible_letters())

    def get_letter_by_position(self, posicion: int) -> str:
        """
        Devuelve la letra asignada a una posicion
        """
        try:
            return self.posible_letters[posicion]
        except IndexError:
            return "Posicion fuera de rango"

    # -------------------------A PARTIR DE AQUI LOS METODOS SERÍAN PRIVADOS-------------------------

    def __get_largo(self) -> int:
        """
        Devuelve lo largo de la lista del objeto
        """
        return len(self.posible_letters)

if __name__ == "__main__":
    from class_bcolors_enum import Colors

    Letras = Dni_letter()
    print(f"\nLas letras son : {Colors.HEADER}")
    print(Letras)
    print(
        f"{Colors.ENDC}\nLa letra asignada a la posicion 4 es: {Colors.OKGREEN}{Letras.get_letter_by_position(4)}{Colors.ENDC}"
    )
    print(
        f"\nLa letra asignada a la posicion 33 es:  {Colors.BOLD}{Colors.UNDERLINE}{Colors.FAIL}{Letras.get_letter_by_position(33)}{Colors.ENDC}"
    )
    print(
        f"\nLa letra de 77422360 es: {Colors.OKGREEN}{Letras.get_letter_by_dni(77422360)}{Colors.ENDC}"
    )
    print(
        f"\nLa letra l esta en letras:  {Colors.OKBLUE}{str(Letras.does_letter_exists('l'))}{Colors.ENDC}"
    )
    print(
        f"\nLa letra N esta en letras:  {Colors.OKBLUE}{str(Letras.does_letter_exists('N'))}{Colors.ENDC}"
    )
    print(
        f"\nLa letra Ñ esta en letras: {Colors.BOLD}{Colors.UNDERLINE}{Colors.FAIL}{str(Letras.does_letter_exists('ñ'))}{Colors.ENDC}"
    )
