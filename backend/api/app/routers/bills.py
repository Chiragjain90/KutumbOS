from fastapi import APIRouter
from schemas.bills import Bill

router = APIRouter(prefix="/bills", tags=["Bills"])

bills_db = []