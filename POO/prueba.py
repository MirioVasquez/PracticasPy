class persona:
    def __init__(self,nombre,edad,nacionalidad):
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
    def __init__(self,nombre,edad,nacionalidad,puesto,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.puesto = puesto
        self.salario = salario
    #Instancia (categoria)
    def trabajador(self):
        print(f"El empleado {self.nombre} trabaja como {self.puesto} y gana {self.salario} al mes")
        
class freelancer():
    def __init__(self,horas,salarioxhora):
        self.horas = horas
        self.salarioxhora = salarioxhora
    #Instancia (categoria)
    def freelancer(self):
        print(f"Este empleado trabaja como freelancer y gana {self.salarioxhora}$ por hora, trabaja un total de {self.horas} horas al dia")

class planilla(contratado, freelancer):
    def __init__(self, nombre,edad,nacionalidad,puesto,salario,horas,salarioxhora):
        contratado.__init__(self,nombre,edad,nacionalidad,puesto,salario)
        freelancer.__init__(self,horas,salarioxhora)
    #Instancia (categoria)
    def popurri(self):
        print(f"El empleado {self.nombre} trabaja como {self.puesto} y gana {self.salario} al mes, tambien trabaja como freelancer y gana {self.salarioxhora}$ por hora, trabaja un total de {self.horas} horas al dia")

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
            Edad = int(input("Ingresa tu edad: "))
        except ValueError:
            print("Ingresa una edad válida")
            continue
        else:
            break
    Nacionalidad = input("Cual es tu nacionalidad: ")
    return (Nombre, Edad, Nacionalidad)


# Datos del empleado
Nombre, Edad, Nacionalidad = form_datos()
planilla1 = planilla(Nombre.capitalize(),int(Edad),Nacionalidad.lower(),"Ingeniero de sistemas",2000,8,20)

planilla1.trabajar()
planilla1.trabajador()
planilla1.freelancer()
planilla1.popurri()



