#creando un conjunto con set
conjunto = set(['dato1','dato2'])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1','dato2'])
conjunto2 = {conjunto1,'dato3'}

#print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {2,4,7,8}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)


print (resultado)