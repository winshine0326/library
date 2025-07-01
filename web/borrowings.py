from fastapi import APIRouter
from pydantic import BaseModel

from service import borrowings as service

class BorrowIn(BaseModel):
    borrower: str
    title: str


router = APIRouter(prefix="/borrows")

@router.post("")
def borrow_book(borrow : BorrowIn) -> bool:
    return service.borrow_book(borrow.borrower, borrow.title)