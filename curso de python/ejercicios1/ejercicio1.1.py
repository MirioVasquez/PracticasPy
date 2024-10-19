#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - round(dalto_curso / otros_cursos_max,3) * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio * 100
tiempo_vacio_dalto = 100 - round(dalto_curso / crudo_dalto,3) * 100

#mostrando la diferencia de duracion
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio')
print("------------------------------------------------------------------------")

#mostrando la cantidad de espacios vacios que se remueven 
print(f'Por lo general se elimina un {tiempo_vacio_promedio}% del crudo en la edicion')
print(f'Pero Dalto ahorra un {tiempo_vacio_dalto}%')
print("------------------------------------------------------------------------")

#mostrando diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de otros cursos')
print("------------------------------------------------------------------------")
