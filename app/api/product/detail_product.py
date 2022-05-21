from app.models.product import Product
from app.db import database
from app.api_models import BaseResponseModel
from app.api_models.product_detail_model import ProductDetailResponse

from fastapi.exceptions import HTTPException


class GetProductDetailResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'id': 10,
                    'barcode': '12345',
                    'name': 'Product 1',
                    'price': 100000,
                    'created_at': '2022-05-20 21:00'
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def get_detail(id: int):
    query = Product.select().where(id == Product.c.id)
    detail = await database.fetch_one(query=query)

    if not detail:
        raise HTTPException(404, detail='Product Not Found')

    return GetProductDetailResponse(
        data=ProductDetailResponse(
            id=detail.id,
            barcode=detail.barcode,
            name=detail.name,
            price=detail.price,
            created_at=detail.created_at
        )
    )
