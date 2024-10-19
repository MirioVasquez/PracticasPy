frase = input("Decime una frase y te calculo cuanto tardarias en decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)


if cantidad_de_palabras < 20:
    print(f"dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
else: 
    print('para flaco tampoco pedi un testamento')
    print(f'Dalto diria esas {cantidad_de_palabras} palabras en {cantidad_de_palabras*0.35} segundos')