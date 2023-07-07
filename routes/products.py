from fastapi import APIRouter, HTTPException


router =  APIRouter(prefix="/products", 
                    tags={"products"},
                    responses= {404: { "message": "No encontrado" }})


products_list = [ "Producto 1", "Producto 2", "Producto 3","Producto 4" ]

@router.get("/")
def usersjson():
    return [{"name": "Duvan", "age": 19, "state": "single" },
            {"name": "kata", "age": 17, "state": "engaged"}]

