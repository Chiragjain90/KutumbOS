from fastapi import APIRouter
from schemas.bills import Bill

router = APIRouter(prefix="/bills", tags=["Bills"])

bills_db = []
@router.get("/")
def get_bills():
    return bills_db
@router.post("/")
def add_bill(bill: Bill):
    bills_db.append(bill)

    return {
        "message": "Bill added successfully",
        "bill": bill
    }
@router.delete("/{id}")
def delete_bill(id: int):

    for bill in bills_db:
        if bill.id == id:
            bills_db.remove(bill)
            return {"message": "Bill deleted"}

    return {"message": "Bill not found"}
@router.get("/total")
def total_expense():

    total = sum(bill.amount for bill in bills_db)

    return {
        "total_expense": total
    }