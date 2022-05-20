from fastapi import FastAPI, status, HTTPException
from typing import List

from .db import metadata, database, db_engine, Product
from .Schemas import ProductRequest, ProductResponse

metadata.create_all(db_engine)

app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()
    

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/product', response_model=List[ProductResponse], tags=['Product'])
async def get_product():
    query = Product.select()
    return await database.fetch_all(query=query)

@app.post('/product', status_code= status.HTTP_201_CREATED, response_model=ProductResponse, tags=['Product'])
async def insert_product(data:ProductRequest):
    query = Product.insert().values(barcode=data.barcode, name=data.name, price=data.price)
    last_record_id = await database.execute(query)
    
    return {**data.dict(), 'id': last_record_id}

@app.get('/product/{id}', response_model=ProductResponse, tags=['Product'])
async def get_detail(id:int):
    query = Product.select().where(id == Product.c.id)
    detail = await database.fetch_one(query=query)
    
    if not detail:
        raise HTTPException(404, detail='Product Not Found')
    
    return {**detail}