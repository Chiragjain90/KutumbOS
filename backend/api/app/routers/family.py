from fastapi import APIRouter
from schemas.family import FamilyMember

router = APIRouter(prefix="/family", tags=["Family"])

family_db = []

@router.get("/")
def get_family():
    return family_db

@router.post("/")
def add_family(member: FamilyMember):
    family_db.append(member)
    return {
        "message": "Family member added successfully",
        "member": member
    }