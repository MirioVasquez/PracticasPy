#frase = input("Porfavor cuentame en que estas pendado: ")
#numpalabras = frase.split(' ')
#conteopalabras = len(numpalabras)
#print(f"has dicho {conteopalabras} palabras")

def fxnt(stxr):
    outp = stxr[0]
    for i in range(1, len(stxr)):
        if stxr[i-1] == " ":
            outp += stxr[i]
    outp = outp.upper()
    return outp

x = input("ingresa un acronimo: ")
print(fxnt(x))