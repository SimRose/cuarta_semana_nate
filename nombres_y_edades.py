censo = dict()
salida = False
while not salida:
    accion = input("Que deseas hacer? (Añadir edad [A] / Consultar censo [C] / Salir [S]) ").upper()

    if accion == "A":
        print("Vamos a añadir una edad al censo")
        print("---------------------------------")
        nombre = input("Nombre:  ").upper()
        edad = input("Edad (dd/mm/aaaa): ")
        censo[nombre] = edad

    elif accion == "C":
        print("Vamos a consultar el censo")
        print("--------------------------")
        nombre = input("De quien deseas consultar la edad? ").upper()
        print(nombre.capitalize())
        print(censo[nombre])

    elif accion == "S":
        salida = True
        print("¡Hasta pronto!")