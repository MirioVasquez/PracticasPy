
acro = input("ingresa el nombre de una corporacion: ")
acro = acro.upper()
variables = acro.split(" ")
numvar = len(variables)    

lista = []
contador = 0

while contador < numvar:
    letras = variables[contador][0]
    lista.append(letras)
    contador += 1
    
final = ''.join(lista)
print(final)