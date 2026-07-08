from fastapi import APIRouter
from schemas.shopping import Product

router = APIRouter(prefix="/shopping", tags=["Shopping"])

shopping_db = []

@router.get("/")
def get_products():
    return shopping_db

@router.post("/")
def add_product(product: Product):
    shopping_db.append(product)
    return {
        "message": "Product added successfully",
        "product": product
    }