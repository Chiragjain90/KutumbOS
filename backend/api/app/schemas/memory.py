from pydantic import BaseModel

class Memory(BaseModel):
    id: int
    user: str
    key: str
    value: str