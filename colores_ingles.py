colores = {"AMARILLO": "Yellow",
           "ROJO": "Red",
           "AZUL": "Blue",
           "VERDE": "Green",
           "NEGRO": "Black",
           "BLANCO": "White",
           "GRIS": "Grey"}
salida = False

while not salida:
    color_usuario = input("¿Que color deseas traducir? (escriba S para salir) ").upper()
    if color_usuario in colores:
        print(colores[color_usuario])
        print("-" * len(colores[color_usuario]))
    elif color_usuario == "S":
        salida = True
        print("¡Hasta luego!")

    else:
        print("Respuesta Incorrecta")
        print("--------------------")