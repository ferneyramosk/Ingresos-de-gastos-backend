from fastapi import FastAPI
from consultas import *
from pydantic import BaseModel

app = FastAPI()

class ModelMovimento(BaseModel):
    date:str
    concept:str
    quantity:float

@app.get("/movimientos",tags=['Movimiento'])
def index():
    return select_all()

@app.get("/movimientos/{id}",tags=['Movimiento'])
def movimiento_by_id(id:int):
    return select_by_id(id)

@app.post("/movimientos",tags=['Movimiento'])
def movimiento_registro(body:ModelMovimento):
    try:
        insert_data( [body.date,body.concept,body.quantity] )
        return {'mensaje':'registro correcto'}
    
    except Exception as ex:
        print(ex)
        return {'error': 'ha fallado el registro'}                 # model_dump convierte la lista en dict
