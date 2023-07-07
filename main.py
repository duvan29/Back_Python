from fastapi import FastAPI
from routes import products, users
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"message": "Hello World" }



@app.get("/url")
async def url():
    return {"URL_Curso": "https://duvannew.github.io/lNKLOTH/"}