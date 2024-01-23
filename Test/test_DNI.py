from src.dni import Dni
import random
    

    def prettyFormatter(condition, message):
        print(f"{Colors.OKGREEN} {message} {Colors.ENDC}"
                  if condition
                  else f"{Colors.FAIL} {message} {Colors.ENDC}")

    ### Casos test ALEATORIOS ###

    casosTest = []
    numeroCasos = 25

    for i in range(1, numeroCasos + 1):
        caso = ""
        for j in range(1, 9):
            # random.randrange(start, stop[, step])
            # numeroAleatorio = random.randint(0, 9)
            # ASCII 48-57 = 0-9    65-90 = A-Z   58 = ":"
            # generamos un numero aleatorio entre 48 y 58
            caracterAscii = random.randrange(48, 58 + 1, 1)
            # convertimos el numero ASCII a caracter. 
            # chr() toma el argumento como codigo ASCII de un caracter
            caso = caso + chr(caracterAscii)
        # en la ultima posicion añado una letra A-Z
        caso = caso + chr(random.randrange(65, 90 + 1, 1))
        casosTest = casosTest + [caso]

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
        prettyFormatter(dni.getLetraSana(), dni.obtenerLetra())