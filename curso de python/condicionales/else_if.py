ingresos_mensuales = 1200
telefono = 82
deudaDC = 60
intereses = 50
salidas = 300 #casa mas salidas
gastos_mensuales = telefono + deudaDC + intereses + salidas

if ingresos_mensuales >= 1200:
    if gastos_mensuales <= 600:
        print('estas bien')
    else:
        print('deja de gastar')
elif ingresos_mensuales >= 600:
    if ingresos_mensuales - gastos_mensuales < 0:
        print('estas en deficit')
    elif ingresos_mensuales - gastos_mensuales > 100:
        print('estas bien pa, te quedan', ingresos_mensuales - gastos_mensuales) 
    else:
        print('para un poquito solo te quedan', ingresos_mensuales - gastos_mensuales, 'soles')
else:
    print('eres pobre')