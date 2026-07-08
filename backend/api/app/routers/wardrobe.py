from fastapi import APIRouter
from schemas.wardrobe import Cloth

router = APIRouter(prefix="/wardrobe", tags=["Wardrobe"])

wardrobe_db = []
@router.get("/")
def get_clothes():
    return wardrobe_db
@router.post("/")
def add_cloth(cloth: Cloth):
    wardrobe_db.append(cloth)

    return {
        "message": "Cloth added successfully",
        "cloth": cloth
    }
@router.delete("/{id}")
def delete_cloth(id: int):

    for cloth in wardrobe_db:
        if cloth.id == id:
            wardrobe_db.remove(cloth)
            return {"message": "Deleted"}

    return {"message": "Not Found"}
@router.get("/color/{color}")
def search_by_color(color: str):

    return [
        cloth
        for cloth in wardrobe_db
        if cloth.color.lower() == color.lower()
    ]
@router.get("/occasion/{occasion}")
def search_by_occasion(occasion: str):

    return [
        cloth
        for cloth in wardrobe_db
        if cloth.occasion.lower() == occasion.lower()
    ]