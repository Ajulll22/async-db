from app.models.product import Product
from app.db import database
from app.api_models import BaseResponseModel
from app.api_models.product_model import ProductResponse


class GetProductResponse(BaseResponseModel):
    class Config:
        schema_extra = {
            'example': {
                'data': [
                    {
                        'id': 10,
                        'barcode': '12345',
                        'name': 'Product 1',
                        'price': 100000
                    },
                    {
                        'id': 20,
                        'barcode': '6789',
                        'name': 'Product 2',
                        'price': 200000
                    },
                ],
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def get_product():
    query = Product.select()
    product_list = await database.fetch_all(query=query)
    result = []

    for product in product_list:
        result.append(
            ProductResponse(
                id=product.id,
                barcode=product.barcode,
                name=product.name,
                price=product.price
            )
        )

    return GetProductResponse(
        data=result
    )
