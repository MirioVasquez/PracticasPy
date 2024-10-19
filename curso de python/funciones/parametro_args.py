#forma optima de sumar valores con *arg, no pueden haber mas valores despues del arg
def suma(nombre, *numeros):
    return f'{nombre}, la suma de tus numeros es {sum(numeros)}'
    
resultado = suma("Lucas",5,6,8,1,32)

#print(resultado)

#usanto el *arg despues

def sumatotal(numeros):
    return sum([*numeros])
resulta2 = sumatotal([3,5,8,4,9])

#print(resulta2)