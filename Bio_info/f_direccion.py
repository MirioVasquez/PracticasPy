def fdireccion():
    while True:
        try:
            direccion = input("Ingresa el nombre de la avenida donde vives: ")
            numero = input("ingresa el numero de tu domicilio: ")
            ciudad = input("Ingresa el distrito donde vives: ")
            direccion, ciudad = direccion.capitalize(), ciudad.capitalize()
            if len(direccion) < 5:
                raise ValueError
            if len(ciudad) < 5:
                raise ValueError
        except ValueError:
            print("Vuelve a intentarlo")
            continue
        else:
            break
    return(direccion, numero, ciudad)

def fdireccion2():
    while True:
        try:
            direccion = input("Ingresa la avenida, numero y distrito donde vives: ")
            direccion, numero, ciudad = direccion.split(",")
            direccion, numero, ciudad = direccion.strip(), numero.strip(), ciudad.strip()
            direccion, ciudad = direccion.capitalize(), ciudad.capitalize()
        except ValueError:
            print("Vuelve a intentarlo")
            continue
        else:
            break
    return(direccion, numero, ciudad)


    