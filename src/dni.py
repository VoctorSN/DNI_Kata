
if __name__ == '__main__':
    from letras import Letra
else:
    from src.letras import Letra

class Dni:
    """Clase dni, almacena las constantes y las funciones/metodos
    necesarios para chekear si un dni puede existir o no"""
    LARGO_DNI=8

    def __init__(self,dni:str) -> None:
        self.dni = dni

    def check_dni(self) -> bool:
        """
        Devuelve si el dni es correcto,
        del caso contrario te devuelve un mensaje con el error
        """

        if not self.check_numero():
            print('El numero es incorrecto')
            return False

        if not self.check_letra():
            print('La letra es incorrecta')
            return False

        letra_real = Letra().get_letra_by_dni(self.obtener_numero())
        if self.obtener_letra() != letra_real:
            print(
                f'La letra no concuerda con el numero, devería ser {letra_real}'
                )
            return False

        return True

    def __repr__(self) -> str:
        return self.dni

    # -------------------------A PARTIR DE AQUI LOS METODOS SERÍAN PRIVADOS-------------------------

    def obtener_numero(self) -> str:
        """
        Devuelve el numero del dni
        """
        return self.dni[:-1]

    def obtener_letra(self) -> str:
        """
        Devuelve la letra del dni
        """
        return self.dni[-1]

    def check_letra(self) -> bool:
        """
        Devuelve un booleano de si la letra 
        esta en la lista de posibles letras o no
        """
        return Letra().is_letra_in_tabla(self.obtener_letra())

    def check_numero(self) -> bool:
        """
        Devuelve un booleano de si el numero
        del dni es correcto recibiendo el dni
        completo con el numero
        """
        numero = self.obtener_numero()
        return numero.isdigit() and self.check_longitud_numero(numero)

    def check_longitud_numero(self,numero:str) -> bool:
        """
        Devuelve si el largo del numero del dni
        es del largo que tien que ser
        """
        return len(numero) == self.LARGO_DNI

if __name__ == "__main__":
    Dni('5353434435345345n').check_dni()
    Dni('77422360r').check_dni()
    Dni('39496391ñ').check_dni()
