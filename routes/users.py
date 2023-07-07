### Users API ###

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Inicia el server: python -m uvicorn basicauthuser:app --reload

router = APIRouter(tags={"user"},
                   responses= {404: { "message": "No encontrado" }})


class User(BaseModel):
    id: int
    name: str
    surname: str
    state: str
    age: int


users_list = [User(id=1, name="Duvan", surname="Serrano", state="single", age=19),
              User(id=2, name="Kata", surname="Monroy", state="engaged", age=17),
              User(id=3, name="Camilo", surname="Rojas", state="single", age=18),
              User(id=4, name="Maicol", surname="Rojas", state="engaged", age=36),
              User(id=5, name="Lia", surname="Paez", state="single", age=0.1)]


@router.get("/usersjson")
def usersjson():
    return [{"name": "Duvan", "age": 19, "state": "single" },
            {"name": "kata", "age": 17, "state": "engaged"}]



@router.get("/users")
async def users():
    return users_list

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    

# Path

@router.get("/user/{id}")  
async def user(id: int):
    return search_user(id)

# Query

@router.get("/user/")  
async def user(id: int):
    return search_user(id)

# POST

@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.routerend(user)
    return user

# PUT

@router.put("/user/")
async def user(user: User):

    found = False

    for i, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[i] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return "Usuario Actualizado" , user

# DELETE

@router.delete("/user/{id}")  
async def user(id: int):

    found = False        

    for i, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[i]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}

    return {"message": "Usuario Eliminado"}
