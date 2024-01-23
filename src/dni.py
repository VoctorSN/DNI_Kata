
if __name__ == '__main__':
    from Letras import Letra
else:
    from src.Letras import Letra

class Dni:
    LARGO_DNI=8

    def check_dni(self,dni:str) -> bool:
        if not self.check_numero(dni):
            return 'El numero es incorrecto'
        if not self.check_letra(dni):
            return 'La letra es incorrecta'
        if self.obtener_letra(dni) != Letra.get_Letra_by_DNI(dni):
            return 'La letra no concuerda con el numero'

    def obtener_numero(self,dni:str) -> str:
        return dni[:-1]

    def obtener_letra(self,dni:str) -> str:
        return dni[-1]

    def check_letra(self,dni):
        return  Letra.is_Letra_in_Tabla(self.obtener_letra(dni))

    def check_numero(self,dni:str) -> bool:
        numero = self.obtener_numero(dni)
        return numero.isdigit() and self.check_longitud_numero(numero)

    def check_longitud_numero(self,numero:str) -> bool:
        return len(numero) == self.LARGO_DNI
