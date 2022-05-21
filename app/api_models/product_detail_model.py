from pydantic import BaseModel
from datetime import datetime


class ProductDetailResponse(BaseModel):
    id: int
    barcode: str
    name: str
    price: int
    created_at: datetime
