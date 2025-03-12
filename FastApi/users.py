#BaseModel = library to handle classes | HTTPException = library to handle exeption in status code
from fastapi import FastAPI, HTTPException
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
            return None
    elif isinstance(x,str):
        users = filter(lambda user: user.name == x, user_list)
        try:
            return list(users)[0]
        except:
            return None
    else:
        return None

@app.get("/user", status_code=200, response_model=list)
async def user():
    return user_list

# Path
@app.get('/user/{id}', status_code=200, response_model=User)
async def userid(id: int):
    if search_user(id) == None:
        raise HTTPException(status_code=404, detail="User not found")
    return search_user(id)
    
# Query    
@app.get('/user/', status_code=200, response_model=User)
async def username(name: str):
    if search_user(name) == None:
        raise HTTPException(status_code=404, detail="User not found")
    return search_user(name)

@app.post('/user', status_code=201)
async def newuser(user: User):
    if search_user(user.id):  # ✅ Check if the function returns a user
        raise HTTPException(status_code=422, detail="User already exists")
    
    user_list.append(user)
    return {"detail": "User created"}
        
@app.put('/user',status_code=202)
async def upuser(user: User):
    for i, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[i] = user  # ✅ Update the user
            return {"detail": "User has been updated"}  # ✅ Exit immediately after update

    raise HTTPException(status_code=304, detail="User has not been updated")  # ✅ Only runs if no match was found
    
@app.delete('/user/{id}',status_code=202)
async def popuser(id: int):
    for i, saved_user in enumerate(user_list):
        if saved_user.id == id:
            user_list.pop(i)  # ✅ Removes and returns the user
            return {"detail": "User has been deleted"}

    raise HTTPException(status_code=204,detail="User has not been deleted")