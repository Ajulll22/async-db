from fastapi import status, HTTPException, Response
from typing import List
from fastapi import APIRouter

from app.db import database
from app.models.product import Product
from app.Schemas import ProductRequest, ProductResponse
from app.api.product.get_product import get_product, GetProductResponse
from app.api.product.insert_product import insert_product, InsertProductResponse
from app.api.product.detail_product import get_detail, GetProductDetailResponse
from app.api.product.update_product import update_product, UpdateProductResponse


api_router = APIRouter()


@api_router.on_event('startup')
async def startup():
    await database.connect()


@api_router.on_event('shutdown')
async def shutdown():
    await database.disconnect()


api_router.add_api_route('/v1/product', get_product,
                         methods=['GET'], tags=['Product'], response_model=GetProductResponse)


api_router.add_api_route('/v1/product', insert_product,
                         methods=['POST'], tags=['Product'], response_model=InsertProductResponse)


api_router.add_api_route('/v1/product/{id}', get_detail,
                         methods=['GET'], tags=['Product'], response_model=GetProductDetailResponse)


api_router.add_api_route('/v1/product/{id}', update_product,
                         methods=['PUT'], tags=['Product'], response_model=UpdateProductResponse)


@api_router.delete('/product/{id}', status_code=204)
async def delete_product(id: int):
    query = Product.delete().where(Product.c.id == id)
    await database.execute(query)

    return Response(status_code=204)
