from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime
import random


def generate_uuid():
    return str(uuid4())

def generate_date():
    return str(datetime.now())

def generate_metrica():
   metrica = random.randint(10, 100) 
   return str(metrica)

class Dispositivo(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    #name: str
    metrica: str = Field(default_factory=generate_metrica)
    date: str = Field(default_factory=generate_date)