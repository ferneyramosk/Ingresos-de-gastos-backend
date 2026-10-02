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

@app.put("/movimientos/{id}",tags=['Movimiento'])                      # Actualizar base de dato
def movimiento_update(id:int,boby:ModelMovimento):        
    try:
        update_data(id,[boby.date,boby.concept,boby.quantity])
        return {'mensaje':'actualizacion correcta'}
    except Exception as ex:
        print(ex)
        return {'error':'ha fallado la actualizacion'}

@app.delete("/movimientos/{id}",tags=['Movimiento'])                # Borrar item, ver mensaje
def movimiento_borrado(id:int):
    try:
        delete_data(id)
        return {' Mensaje': 'Borrado correcto'}
    except Exception as ex:
        print(ex)
        return {'error': 'Ha fallado el borrado'}

@app.get("/movimientos/ingreos",['movimiento'])
def movimiento_ingresos():
    return mostrar_ingresos()

@app.get("/movimientos/gastos",['movimiento'])
def movimiento_gastos():
    return mostrar_gastos()

