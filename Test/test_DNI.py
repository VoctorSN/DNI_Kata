from src.Dni import Dni

def check_numero():
    assert Dni().check_numero('77550032')
    assert Dni().check_numero('3123123123131')
    assert Dni().check_numero('123,1233')

def test_correctos():
    assert Dni().check_dni('77550032N')
    assert Dni().check_dni('77422360J')
    assert Dni().check_dni('39496391D')

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