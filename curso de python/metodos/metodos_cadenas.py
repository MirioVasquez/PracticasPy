cadena1 = 'hoajkajgamyavbhahk'
cadena2 = 'Bienvenido maquinola'

resultado = cadena1.upper()

resultado = cadena1.lower()

resultado = cadena1.capitalize()

#buscar una cadena en otra cadena, si no coincide da -1
busqueda_find = cadena1.find('D')

#buscamos una cadena en otra cadena, si no coincide da error
#busqueda_index = cadena1.index('D')

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count('la ma')

#contamos cuantos caracteres tiene una cadena. len no es un metodo, es una funcion
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith('Ho')

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith('la ')

#remplaza un pedazo de la cadena dada, por otra
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split('a')

print(contar_caracteres)