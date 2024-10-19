def serie_fibo(num):
    lista = []
    x,y = 0,1
    for i in range(num):
        if y > num: return lista
        else:
            lista.append(y)
            x,y = y,x+y
resultado = serie_fibo(34)
print (resultado)
        