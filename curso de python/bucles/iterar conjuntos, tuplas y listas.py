
animales = ['perro','gato','loro','cocodrilo']
numeros = [10,62,12,72]

#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')
    
#recorriendo la lista numeros y multiplicando por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)    

#recorriendo dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'recorrienda lista 1: {numero}')    
    print(f'recorrienda lista 2: {animal}')
    
#forma no optima de recorrer una lista. No funciona con conjuntos
for num in range(len(numeros)):
    print(numeros[num])    
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#desempaquetar tupla (solo indice)
for num,i in enumerate(numeros):
    print(num)
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual {numero}')
else:
    print('el bucle termino')
    
#todo lo anterior funciona tambien con tuplas, listas y conjuntos  

           
    