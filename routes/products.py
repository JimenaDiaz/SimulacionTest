from fastapi import APIRouter
from schemas.simulacion_dis import Dispositivo
from schemas.producer import Producer
from redis_cloud.crud import delete_hash, get_hash, save_hash


routes_product = APIRouter()

#fake_db=Producer()
#print ('***', fake_db)
#     
fake_db = []

@routes_product.post("/create", response_model=Dispositivo)
def create(product: Dispositivo):
    try:
        fake_db.append(product.dict())

        save_hash(key=product.dict()["id"], data=product.dict())
       
        return product
    except Exception as e:
        return e

@routes_product.get("/get/{id}")
def get(id: str):
    try:
        data = get_hash(key=id)
        return list(filter(lambda field: field["id"] == id, fake_db))[0]
    except Exception as e:
        return e

@routes_product.delete("/delete/{id}")
def get(id: str):
    try:
        keys = Dispositivo.__fields__.keys()
        delete_hash(key=id, keys=keys)
        product = list(filter(lambda field: field["id"] != id, fake_db))
        if len(product) != 0:
            fake_db.remove(product)
        return{
            "message":"success"
        }

    except Exception as e:
        return e