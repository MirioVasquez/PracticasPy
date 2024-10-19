
def obtenercomp(cantidad):
    totalumnos = []
    cantidad = input('Cuantos alumnos hay? ')
    cantidad = int(cantidad)

    for i in range(cantidad):
        nombre = input('Ingresa tu nombre porfavor: ')
        edad = input('Ingresa tu edad porfavor: ')
        compa = (nombre,edad)
        totalumnos.append(compa)
    totalumnos.sort(key= lambda x:x[1])
    asistente = totalumnos [0][0]
    profesor = totalumnos [-1][0]
    
    return asistente,profesor
    
x,y = obtenercomp(0)
print(f'El profesor sera {y} y su asistente {x}')