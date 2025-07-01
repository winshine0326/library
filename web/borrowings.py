from typing import List

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

@router.get("/month/{borrow_month}")
def get_books_by_month(borrow_month : str) -> List[dict]:
    return service.get_books_by_month(borrow_month)

