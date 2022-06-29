from itertools import product
from fastapi import FastAPI 
from routes.products import routes_product
from schemas.producer import Producer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(routes_product, prefix="/simulacion")

