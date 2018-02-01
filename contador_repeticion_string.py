contador = dict()
salida = False

while not salida:
    string = input("Escriba la oración a analizar ( escriba S para salir) : ")

    if string == "S":
        salida = True
        print("¡Hasta luego!")
        print("-------------")
    else:
        for palabra in string:
            if palabra in contador:
                contador[palabra] += 1
            else:
                contador[palabra] = 1

        for indice in contador:
            print("{}: {}".format(indice, contador[indice]))
