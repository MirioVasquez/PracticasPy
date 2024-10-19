
def saludar (nombre,sexo):
    nombre = input('Ingresa tu nombre porfavor: ')
    sexo = input('Eres hombre, mujer, o no quisieras especificar? ')
    sexo = sexo.lower()
    if sexo == "hombre":
        adjetivo = 'señor'
    elif sexo == "mujer":
        adjetivo = "señorita"
    else:
        adjetivo = "señor@"

    print(f'Hola {adjetivo} {nombre}, muy buenos dias.')
  
saludar('','') 

def crear_contrasena_random(num):
    num = input('Ingrese un numero: ')
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 3
    c2 = num - 5
    c3 = num 
    contrasena = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*3}'
    contrasena1 = f'{chars[c1+1]}{chars[c2+1]}{chars[c3+1]}{num*3}'
    return contrasena,contrasena1

password, primer_numero = crear_contrasena_random(0)

print(f'Tu contrasena es: {password}')
print(f'Y tu otra contrasena es: {primer_numero}')    


