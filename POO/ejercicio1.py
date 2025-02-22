class estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    #Instancia (estudiar)
    def estudiar(self):
        print(f"El alumno {self.nombre} esta estudiando")

def formdatos():
    Nombre = input("Ingresa tu nombre: ")
    Edad = input("Ingresa tu edad: ")
    Grado = input("Ingresa tu grado de estudios: ")
    return (Nombre, Edad, Grado)

Nombre, Edad, Grado = formdatos()

estudiante1 = estudiante(Nombre, Edad, Grado)

while True:
    try:
        trigger = input("Que te gustaria hacer? ")
        if trigger.lower() == "estudiar":
            estudiante1.estudiar()
        else:
            raise ValueError
    except ValueError:
        print("Quisiste decir, 'Estudiar'?")
        continue
    else:
        break
