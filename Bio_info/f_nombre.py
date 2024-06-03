def fornombre():
    while True:
        try:
            Holename = input("Ingresa tu primer nombre y apellido: ")
            name, surname = Holename.split(' ')
            name, surname = name.capitalize(), surname.capitalize()
            if len(name) < 3:
                raise ValueError
            if len(surname) < 3:
                raise ValueError
        except ValueError:
            print('Vuelve a intentarlo')
            continue
        else:
            break
    return(name,surname)

