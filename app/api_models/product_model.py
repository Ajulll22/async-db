from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    barcode: str
    name: str
    price: int
