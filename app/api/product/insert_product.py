from app.models.product import Product
from app.db import database
from app.api_models import BaseResponseModel

from pydantic import BaseModel
from fastapi.exceptions import HTTPException


class InsertProductRequest(BaseModel):
    barcode: str
    name: str
    price: int


class InsertProductResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 20,
                    'url': '/v1/product/20',
                },
                'meta': {},
                'message': 'Product Created',
                'success': True,
                'code': 200
            }
        }


async def insert_product(data: InsertProductRequest):
    checking = Product.select(Product.c.id).where(
        Product.c.barcode == data.barcode)
    check_barcode = await database.fetch_one(checking)

    if check_barcode:
        raise HTTPException(400, detail='Error Barcode')

    query = Product.insert().values(barcode=data.barcode,
                                    name=data.name, price=data.price)
    last_record_id = await database.execute(query)

    return InsertProductResponse(
        data={
            'id': last_record_id,
            'url': f'/v1/product/{last_record_id}'
        }
    )
