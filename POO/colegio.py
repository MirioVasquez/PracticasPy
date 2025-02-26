class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    #Instancias ()
    def nom_estd(self):
        print(f"{self.nombre} tiene {self.edad} años")
        
class estudiante(persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
    #Instancia ()
    def estd(self):
        print(f" y esta en {self.grado} grado")

estudiante1 = estudiante("Carlos",24,"4to")
estudiante1.nom_estd()
estudiante1.estd()

    