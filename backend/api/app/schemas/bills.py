from pydantic import BaseModel

class Bill(BaseModel):
    id: int
    category: str
    amount: float
    merchant: str
    date: str