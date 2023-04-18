from typing import List
from fastapi import APIRouter
from config.db import conn, collection
from schemas.pronostico import pronosticoEntity, pronosticosEntity
from models.pronostico import Pronostico
from services import scrappy
api = APIRouter()


@api.get('/api')
def verify():
    return "Ok, it's working"


@api.get('/api/pronostico')
def get_pronostico():
    return pronosticosEntity(collection.find())


@api.get('/api/scrappy')
async def get_data():
    data = list({str(diccionario): diccionario for diccionario in scrappy.libertad_place}.values())
    return data


@api.post('/api/pronostico')
def save_pronostico(pronostico: Pronostico):
    new_pronostico = dict(pronostico)
    del new_pronostico["id"]
    id = collection.insert_one(new_pronostico).inserted_id
    data = collection.find_one({"_id": id})
    return pronosticoEntity(data)

# Desde aca me sirve para el scrappy
@api.post('/api/insert_all')
async def save_pronostico_all(pronosticos: List[Pronostico]):
    for item in pronosticos:
        del (item.dict())["id"]
    result = collection.insert_many([pronostico.dict() for pronostico in pronosticos])

    return {"inserted_ids": str(result.inserted_ids)}


@api.delete('/api/pronostico')
async def delete_pronostico():
    result = collection.delete_many({})
    return {"Se han eliminado ", result.deleted_count, "Elementos"}
