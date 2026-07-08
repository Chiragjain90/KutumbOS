from pydantic import BaseModel

class Cloth(BaseModel):
    id: int
    name: str
    color: str
    category: str
    occasion: str