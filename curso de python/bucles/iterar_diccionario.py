diccionario = {
    'nombre' : 'lucas',
    'apellido' : 'dalto',
    'subs' : 100000
}

#recorriendo el dicc para obtener las claves
for key in diccionario:
    key
    print(f'la clave es: {key}')
    
#recorriendo dicc con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es: {value}')