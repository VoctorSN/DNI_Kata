
if __name__ == '__main__':
    from letras import Dni_letter
else:
    from src.letras import Dni_letter

class Dni:
    """Clase dni, almacena las constantes y las funciones/metodos
    necesarios para chekear si un dni puede existir o no"""
    NUMBER_LENGHT=8

    def __init__(self,dni:str) -> None:
        self.dni = dni

    def is_a_correct_dni(self) -> bool:
        """
        Devuelve si el dni es correcto,
        del caso contrario te devuelve un mensaje con el error
        """

        if not self.is_a_correct_number():
            print('El numero es incorrecto')
            return False

        if not self.is_a_correct_letter():
            print('La letra es incorrecta')
            return False

        calculated_letter = Dni_letter().get_letter_by_dni(self.__get_number())
        if self.__get_letter() != calculated_letter:
            print(
                f'La letra no concuerda con el numero, devería ser {calculated_letter}'
                )
            return False

        return True

    def __repr__(self) -> str:
        return self.dni

    def is_a_correct_letter(self) -> bool:
        """
        Devuelve un booleano de si la letra 
        esta en la lista de posibles letras o no
        """
        return Dni_letter().does_letter_exists(self.__get_letter())

    def is_a_correct_number(self) -> bool:
        """
        Devuelve un booleano de si el numero
        del dni es correcto recibiendo el dni
        completo con el numero
        """
        number = self.__get_number()
        return number.isdigit() and self.__is_correct_number_lenght(number)

    # -------------------------A PARTIR DE AQUI LOS METODOS SERÍAN PRIVADOS-------------------------

    def __get_number(self) -> str:
        """
        Devuelve el numero del dni
        """
        return self.dni[:-1]

    def __get_letter(self) -> str:
        """
        Devuelve la letra del dni
        """
        return self.dni[-1]

    def __is_correct_number_lenght(self,number:str) -> bool:
        """
        Devuelve si el largo del numero del dni
        es del largo que tien que ser
        """
        return len(number) == self.NUMBER_LENGHT

if __name__ == "__main__":
    Dni('5353434435345345n').is_a_correct_dni()
    Dni('77422360r').is_a_correct_dni()
    Dni('39496391ñ').is_a_correct_dni()
