from app.models.product import Product
from app.db import database

from fastapi import Response, HTTPException


async def delete_product(id: int):
    query = Product.select(Product.c.id).where(id == Product.c.id)
    check_id = await database.fetch_one(query=query)

    if not check_id:
        raise HTTPException(404, detail='Product Not Found')

    query = Product.delete().where(Product.c.id == id)
    await database.execute(query)

    return Response(status_code=204)
