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
@router.delete("/{name}")
def delete_family(name: str):
    global family_db

    for member in family_db:
        if member.name == name:
            family_db.remove(member)
            return {
                "message": "Family member deleted successfully"
            }

    return {
        "message": "Member not found"
    }