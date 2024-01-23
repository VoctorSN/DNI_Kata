from class_bcolors_enum import Colors


class Letra:
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

    def get_Letras(self) -> list:
        return self.letras

    def print_Letras(self):
        print(self.get_Letras())

    def get_Letra_by_Position(self, posicion: int) -> str:
        try:
            return self.letras[posicion]
        except IndexError:
            return "Posicion fuera de rango"

    def get_Largo(self) -> int:
        return len(self.letras)

    def get_Letra_by_DNI(self, numero) -> str:
        return self.letras[int(numero) % self.get_Largo()]

    def is_Letra_in_Tabla(self, char: str) -> bool:
        return char.upper() in self.letras


if __name__ == "__main__":
    Letras = Letra()
    print(f"\nLas letras son : {Colors.HEADER}")
    Letras.print_Letras()
    print(
        f"{Colors.ENDC}\nLa letra asignada a la posicion 4 es: {Colors.OKGREEN}"
        + Letras.get_Letra_by_Position(4) + Colors.ENDC
    )
    print(
        f"\nLa letra asignada a la posicion 33 es:  {Colors.BOLD}{Colors.UNDERLINE}{Colors.FAIL}{Letras.get_Letra_by_Position(33)}{Colors.ENDC}"
    )
    print(
        f"\nLa letra de 34343434 es: {Colors.OKGREEN}{Letras.get_Letra_by_DNI(34343434)}{Colors.ENDC}"
    )
    print(
        "\nLa letra L esta en letras:  {}{}{}".format(
            Colors.OKBLUE, str(Letras.is_Letra_in_Tabla("l")), Colors.ENDC
        )
    )
    print(
        "\nLa letra Ñ esta en letras: {}{}{}{}{}".format(
            Colors.BOLD,
            Colors.UNDERLINE,
            Colors.FAIL,
            str(Letras.is_Letra_in_Tabla("ñ")),
            Colors.ENDC,
        )
    )