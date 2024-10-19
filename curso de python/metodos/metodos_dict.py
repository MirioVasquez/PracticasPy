dict = {
    'nombre' : 'lucas',
    'apellido' : 'dalto',
    'subs' : 1000000
}

#devuelve las claves
claves = dict.keys()

#devulve un valor, si no encuentra el valor responde "none", mas no manda error y continua
valor = dict.get('nombre')

#elimina todos los elementos del diccionario
#dict.clear()

#eliminando un elemento del diccionario
dict.pop('subs')

#obteniendo un elemento dict_itemns iterable
dict_iterable = dict.items()

print(dict_iterable)