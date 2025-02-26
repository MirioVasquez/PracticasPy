class animal:
    def accion(self):
        print("Comer")
    
class mamifero(animal):
    # def accion(self):
    #     print("Amamantar")
    pass
class volador(animal):
    # def accion(self):
    #     print("Volar")
    pass
class murcielago(mamifero,volador):
    pass

murcielago1 = murcielago()
murcielago1.accion()
# Output: amamantar - volar -  comer