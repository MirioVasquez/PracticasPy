frutas = ['banana','manzana','ciruela','pera','naranja','granada','durazno']
cadena = 'Hola Dalto'
numeros = [10,20,35,48]

#para saltar un valor
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'Me voy a comer una {fruta}')
    

#finalizar el bucle, el "else" tampoco lo ejecuta
for fruta in frutas:
    if fruta == 'manzana':
        break
    print(f'Me voy a comer una {fruta}')
    
print('Bucle terminado')

#recorer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
