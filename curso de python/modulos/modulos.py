#importando un modulo y asignandole el nombre 'm_saludar'
#import modulo_saludar as m_saludar

#desde ese modulo importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludo_normal

#creamos las variables con saludos
saludo = saludo_normal('Lucas')

#mostramos resultado
print(saludo)

#para ver las propiedades y metodos del namespace
#print(dir(m_saludar))

#accedemos al nombre    
print(__name__)

#accedemos al nombre del modulo llamado
#print(m_daludar.__name__)