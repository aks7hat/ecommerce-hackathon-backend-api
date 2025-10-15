from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    product_id: str
    name: str
    description: str
    category: str
    price: float
    image_url: str

class SearchResponse(BaseModel):
    results: List[str]

class CartItem(BaseModel):
    product_id: str
    quantity: int = 1

class CartResponse(BaseModel):
    user_id: str
    cart: List[CartItem]

class CheckoutResponse(BaseModel):
    message: str
