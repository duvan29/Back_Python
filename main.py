from fastapi import FastAPI
from routes import products, users, jwtauthusers, basicauthusers
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

# Routers
app.include_router(products.router)

app.include_router(users.router)

app.include_router(jwtauthusers.router)

app.include_router(basicauthusers.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=17664

@app.get("/")
def root():
    return {"message": "Hello World" }



@app.get("/url")
async def url():
    return {"URL_Curso": "https://duvannew.github.io/lNKLOTH/"}