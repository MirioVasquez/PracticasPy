# class celular():
#     marca = "Samsung"
#     modelo = "s23"
#     camara = "48mp"

#celular1 = celular()
#print(celular1.modelo)

class phone:
    #Creando el objeto
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    # Creando los metodos del objeto
    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.marca} {self.modelo}')
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.marca} {self.modelo}')

celular1 = phone('samsung','s23','48mp')
celular2 = phone('apple','15 pro','96mp')

celular1.llamar()
celular2.cortar()