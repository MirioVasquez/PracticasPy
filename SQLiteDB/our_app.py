import database
from database import val

#x,y,z=val()

#database.add_one(x,y,z)

database.delete_one("rowid = 4")

database.show_all()