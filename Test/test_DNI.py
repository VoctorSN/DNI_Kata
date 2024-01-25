from src.dni import Dni

def test_repr():
    assert repr(Dni('77550032n')) == '77550032n'

def test_check_numero():
    assert Dni('77550032n').check_numero()
    assert not Dni('3123123123131n').check_numero()
    assert not Dni('123,1233m').check_numero()

def test_check_letra():
    assert Dni('77550032n').check_letra()
    assert not Dni('3123123123131ñ').check_letra()
    assert not Dni('123,1233').check_letra()

def test_dni_correctos():
    assert Dni('77550032N').check_dni()
    assert Dni('77422360J').check_dni()
    assert Dni('39496391D').check_dni()

def test_dni_incorrectos():
    assert not Dni('5353434435345345n').check_dni()
    assert not Dni('77422360r').check_dni()
    assert not Dni('39496391ñ').check_dni()

"""
    print("\n## CASOS TEST ALEATORIOS ##\n")

    print(casosTest)

    for testString in casosTest:
        dni = Dni(testString)
        print(dni.getDni())
        dni.checkCIF()
        # print("dni --->", dni.getNumeroSano())
        # print("Letra --->", dni.getLetraSana())
        # print("La letra es", dni.obtenerLetra())
        prettyFormatter(dni.getNumeroSano(), dni.getDni())
        prettyFormatter(dni.getLetraSana(), dni.obtenerLetra())

    ### Casos test OK ###

    casosTest = [  # casos OK
        "78484464T",
        "72376173A",
        "01817200Q",
        "95882054E",
        "63587725Q",
        "26861694V",
        "21616083Q",
        "26868974Y",
        "40135330P",
        "89044648X",
        "80117501Z",
        "34168723S",
        "76857238R",
        "66714505S",
        "66499420A",
    ]

    print("\n #### CASOS OK #### \n")

    for testString in casosTest:
        dni = Dni(testString)
        print(dni.getDni())
        dni.checkCIF()
        # print("dni --->", dni.getNumeroSano())
        # print("Letra --->", dni.getLetraSana())
        # print("La letra es", dni.obtenerLetra())
        prettyFormatter(dni.getNumeroSano(), dni.getDni())
        prettyFormatter(dni.getLetraSana(), dni.obtenerLetra())"""