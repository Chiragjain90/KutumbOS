from pydantic import BaseModel

class FamilyMember(BaseModel):
    name: str
    age: int
    relation: str