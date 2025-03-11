from fastapi import FastAPI
#library to handle classes
from pydantic import BaseModel

#Creating a class
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

app = FastAPI()

#creando paquete de usuarios con la clase User
user_list = [
    User(id=1,name="Edwin",surname="Cano",email="ed@ca.com",age=25),
    User(id=2,name="Martin",surname="Cano",email="ma@ca.com",age=32),
    User(id=3,name="Gael",surname="Cano",email="ga@ca.com",age=14)
]

@app.get("/userjson")
async def userjson():
    return [
        {"name":"Edwin", "surname":"Cano", "email":"ed@ca.com", "age":"25"}, {"name":"Martin", "surname":"Cano", "email":"ma@ca.com", "age":"32"}, {"name":"Gael", "surname":"Cano", "email":"ga@ca.com", "age":"14"}
        ]

def search_user(x):
    if isinstance(x,int):
        users = filter(lambda user: user.id == x, user_list)
        try:
            return list(users)[0]
        except:
            return {"error":"404 id not found"}
    elif isinstance(x,str):
        users = filter(lambda user: user.name == x, user_list)
        try:
            return list(users)[0]
        except:
            return {"error":"404 name not found"}
    else:
        return {"error":"404 parameter not found"}


@app.get("/user")
async def user():
    return user_list

# Path
@app.get('/user/{id}')
async def userid(id: int):
    return search_user(id)
    
# Query    
@app.get('/user/')
async def username(name: str):
    return search_user(name)

@app.post('/user')
async def newuser(user: User):
    if search_user(user.id):  # ✅ Check if the function returns a user
        return {"error": "409 User already exists"}
    
    user_list.append(user)
    return {"success": "200 User added"}
        
@app.put('/user')
async def upuser(user: User):
    for i, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[i] = user  # ✅ Update the user
            return {"success": "200 User has been updated"}  # ✅ Exit immediately after update

    return {"error": "409 User has not been updated"}  # ✅ Only runs if no match was found
    
@app.delete('/user/{id}')
async def popuser(id: int):
    for i, saved_user in enumerate(user_list):
        if saved_user.id == id:
            user_list.pop(i)  # ✅ Removes and returns the user
            return {"success": "200 User has been deleted"}

    return {"error": "400 User not found"}