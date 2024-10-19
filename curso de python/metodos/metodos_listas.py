#creando una lista con list
lista = list([34, 85, 15, False, True])

#decuelcela cantidad de elementos de la lista
resultado = len(lista)

#agregando un elemento a la lista
lista.append(65)

#agregando un elemento a la lista en un indice especifico
lista.insert(2, 'Toma mama')

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista por su indice
lista.pop(1)

#removiendo un elemento de la vista por su valor
lista.remove('Toma mama')

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista (si usamos el parametro reverse = true loordena adescendente)
lista.sort()

#invirtiendolos elemeon de una lista
lista.reverse()

#verificando si un elemento esta en la lista
elemento_encontrado = lista.index(False)

print(lista)

#la fucion (Dir) nos permite ver que podemos hacer con el objeto seleccionado