from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

user_list = [
    User(id=1,name="Edwin",surname="Cano",email="ed@ca.com",age=25),
    User(id=2,name="Martin",surname="Cano",email="ma@ca.com",age=32),
    User(id=3,name="Gael",surname="Cano",email="ga@ca.com",age=14),
    User(id=5,name="Gael",surname="Cano",email="ga@ca.com",age=14)
]

User1 = User(id=3,name="Gael",surname="Cano",email="ga@ca.com",age=14)

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
 
        