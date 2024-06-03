from f_nombre import fornombre
from f_nacimiento import forborn
from f_direccion import fdireccion2
from f_goals import fgoals
name,surname = fornombre()
x = forborn()
av, numero, distrito = fdireccion2()
dcpt = fgoals()

    

formbio = f'''
- Nombre : {name} {surname}
- Fecha de nacimiento : {x.strftime("%b")} {x.day}, {x.year}
- Direccion : {numero} Av. {av}, {distrito}
- Metas personales : {dcpt}'''

print(formbio)