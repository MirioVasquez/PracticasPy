class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    #Instancias (situacion)
    def trabajar(self):
        if self.nacionalidad == "peruano" or self.nacionalidad == "peruana":
            print(f"El empleado {self.nombre} es de nacionalidad peruana y puede trabajar")
        else:
            print(f"El empleado {self.nombre} es de nacionalidad {self.nacionalidad} y necesita un sponsor para trabajar")

class contratado(persona):
    def __init__(self, nombre, edad, nacionalidad, puesto, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.puesto = puesto
        self.salario = salario
    #Instancia (categoria)
    def trabajar1(self):
        print(f"El empleado {self.nombre} trabaja como {self.puesto} y gana {self.salario} al mes")

# Funcion para ingresar datos del posible empleado
def form_datos():
    while True:
        try:
            Nombre = input("Ingresa tu nombre: ")
            if Nombre.isalpha() == False:
                raise ValueError
        except ValueError:
            print("Ingresa un nombre valido")
            continue
        else:
            break
    while True:
        try:
            Edad = input("Ingresa tu edad: ")
            if int(Edad) == False:
                raise ValueError
        except ValueError:
            print("Ingresa una edad valida")
            continue
        else:
            break
    Nacionalidad = input("Cual es tu nacionalidad: ")
    return (Nombre, Edad, Nacionalidad)

Nombre, Edad, Nacionalidad = form_datos()
empleado1 = contratado(Nombre.capitalize(), int(Edad), Nacionalidad.lower(), "Ingeniero de sistemas", 2000)
empleado1.trabajar()
empleado1.trabajar1()


