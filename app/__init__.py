from fastapi import FastAPI, status, HTTPException, Response
from typing import List
from app.api import api_router

from .db import metadata, database, db_engine, Product
from .Schemas import ProductRequest, ProductResponse

metadata.create_all(db_engine)

app = FastAPI()

app.include_router(api_router)
