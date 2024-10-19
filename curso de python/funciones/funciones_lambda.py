numeros = [1,2,3,4,5,6,7,8,9]

#creando multiplicacion lambda por 2
multidos = filter(lambda x:x%2 == 0,numeros)

print(list(multidos))
