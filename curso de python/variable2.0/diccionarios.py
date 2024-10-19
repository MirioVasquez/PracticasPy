#creando diccionarios con dict()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser claves por que son mutables
diccionario = {frozenset(["dalto",'rancio']):'jajaja'}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys('nombre')

print(diccionario)