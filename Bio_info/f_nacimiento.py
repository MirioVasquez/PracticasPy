from datetime import date

def forborn():
    while True:
        try:
            Holebitrh = input("Ingresa tu fecha de nacimiento en formato DD/MM/AAAA: ")
            day, month, year = map(int,Holebitrh.split('/'))
            dayborn = date(year, month, day)
        except ValueError:
            print('Vuelve a intentarlo')
            continue
        else:
            break
    return(dayborn)
    