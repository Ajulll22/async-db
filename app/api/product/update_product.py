from app.models.product import Product
from app.api_models import BaseResponseModel
from app.db import database

from pydantic import BaseModel
from enum import Enum
from fastapi.exceptions import HTTPException


class is_active_enum(Enum):
    Active = 1
    Inactive = 0


class UpdateProductRequest(BaseModel):
    barcode: str
    name: str
    price: int
    is_active: is_active_enum


class UpdateProductResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 20,
                    'url': '/v1/product/20',
                },
                'meta': {},
                'message': 'Product Updated',
                'success': True,
                'code': 200
            }
        }


async def update_product(id: int, data: UpdateProductRequest):
    query = Product.select(Product.c.id).where(id == Product.c.id)
    check_id = await database.fetch_one(query=query)

    if not check_id:
        raise HTTPException(404, detail='Product Not Found')

    checking = Product.select(Product.c.id).where(
        Product.c.barcode == data.barcode)
    check_barcode = await database.fetch_one(checking)

    if check_barcode:
        raise HTTPException(400, detail='Error Barcode')

    query = Product.update().where(Product.c.id == id
                                   ).values(barcode=data.barcode,
                                            name=data.name,
                                            price=data.price
                                            )
    await database.execute(query)

    return UpdateProductResponse(
        data={
            'id': id,
            'url': f'/v1/product/{id}'
        }
    )
