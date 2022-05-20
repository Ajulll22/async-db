from pydantic import BaseModel


class ProductRequest(BaseModel):
    barcode:str
    name:str
    price:int
    
class ProductResponse(ProductRequest):
    id:int