def fgoals():
    while True:    
        try:
            metas = input("Cuentanos tus metas: ")
            metas = metas.capitalize()
            if len(metas) < 20:
                raise ValueError
        except ValueError:
            print("Explaya un poco mas en tu respuesta porfavor")
        else:
            break
    return(metas)
    